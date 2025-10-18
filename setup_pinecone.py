"""
Pinecone Vector Database Setup Script
Sets up Pinecone index for furniture recommendations with semantic search
"""

import os
import pinecone
from sentence_transformers import SentenceTransformer
import pandas as pd
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_pinecone():
    """Initialize Pinecone and create index for furniture recommendations"""
    
    # Get Pinecone credentials
    api_key = os.getenv('PINECONE_API_KEY')
    environment = os.getenv('PINECONE_ENVIRONMENT')
    index_name = os.getenv('PINECONE_INDEX_NAME', 'furniture-recommendations')
    
    if not api_key or not environment:
        logger.error("Please set PINECONE_API_KEY and PINECONE_ENVIRONMENT in your .env file")
        return False
    
    try:
        # Initialize Pinecone
        pinecone.init(api_key=api_key, environment=environment)
        logger.info(f"Connected to Pinecone environment: {environment}")
        
        # Create index if it doesn't exist
        if index_name not in pinecone.list_indexes():
            logger.info(f"Creating Pinecone index: {index_name}")
            pinecone.create_index(
                name=index_name,
                dimension=384,  # sentence-transformers/all-MiniLM-L6-v2 dimension
                metric='cosine'
            )
            logger.info(f"Index {index_name} created successfully")
        else:
            logger.info(f"Index {index_name} already exists")
        
        return True
        
    except Exception as e:
        logger.error(f"Error setting up Pinecone: {e}")
        return False

def populate_pinecone_index():
    """Populate Pinecone index with furniture embeddings"""
    
    try:
        # Load sentence transformer model
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        logger.info("Loaded sentence transformer model")
        
        # Load furniture data
        df = pd.read_csv('data/intern_data_ikarus.csv')
        logger.info(f"Loaded {len(df)} furniture items")
        
        # Connect to Pinecone index
        index_name = os.getenv('PINECONE_INDEX_NAME', 'furniture-recommendations')
        index = pinecone.Index(index_name)
        
        # Process and upsert data in batches
        batch_size = 100
        for i in range(0, len(df), batch_size):
            batch = df.iloc[i:i+batch_size]
            
            # Create embeddings for product descriptions
            texts = []
            for _, row in batch.iterrows():
                text = f"{row.get('title', '')} {row.get('description', '')} {row.get('category', '')}"
                texts.append(text)
            
            # Generate embeddings
            embeddings = model.encode(texts)
            
            # Prepare vectors for upsert
            vectors = []
            for idx, (_, row) in enumerate(batch.iterrows()):
                vector = {
                    'id': str(row.get('uniq_id', f'item_{i+idx}')),
                    'values': embeddings[idx].tolist(),
                    'metadata': {
                        'title': row.get('title', ''),
                        'price': str(row.get('price', '')),
                        'category': row.get('category', ''),
                        'description': row.get('description', '')
                    }
                }
                vectors.append(vector)
            
            # Upsert to Pinecone
            index.upsert(vectors=vectors)
            logger.info(f"Upserted batch {i//batch_size + 1}/{(len(df)-1)//batch_size + 1}")
        
        logger.info("Successfully populated Pinecone index with furniture data")
        return True
        
    except Exception as e:
        logger.error(f"Error populating Pinecone index: {e}")
        return False

if __name__ == "__main__":
    logger.info("Starting Pinecone setup...")
    
    # Setup Pinecone
    if setup_pinecone():
        logger.info("Pinecone setup completed successfully")
        
        # Populate index
        populate_choice = input("Do you want to populate the index with furniture data? (y/n): ")
        if populate_choice.lower() == 'y':
            populate_pinecone_index()
    else:
        logger.error("Pinecone setup failed")