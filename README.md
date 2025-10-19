# AI-Powered Furniture Recommendation & Analytics Platform

## 🏠 Project Overview
A full-stack AI application leveraging ML, NLP, CV, and GenAI to create an intelligent furniture discovery system. Users can search products via natural language queries and get semantically similar products with AI-generated descriptions.

## 🔧 Features
- **Chat-Style Product Discovery**: Natural language search with conversational interface
- **AI-Generated Descriptions**: Creative product descriptions using GenAI
- **Semantic Search**: Vector database powered search using Pinecone
- **Analytics Dashboard**: Business insights with interactive charts
- **Dark Theme UI**: Modern navy/indigo design with responsive layout
- **Context-Aware Conversations**: Maintains chat history and context
- **Multi-Modal AI**: Combines text and image embeddings

## 🛠 Tech Stack

### Backend
- **FastAPI**: High-performance API server
- **Pinecone**: Vector database for semantic search
- **LangChain**: GenAI integration
- **Transformers**: NLP models for embeddings
- **PyTorch**: Computer vision models

### Frontend  
- **React**: Modern UI framework
- **React Router**: Client-side routing
- **Tailwind CSS**: Utility-first styling
- **Dark Theme**: Navy/indigo gradient design

### AI Models
- **Google Gemini AI**: Advanced conversational AI and content generation
- **Sentence Transformers**: Text embeddings for semantic search
- **Pinecone**: Vector database for similarity matching
- **OpenAI/GPT**: Creative description generation (optional)
- **Hugging Face Models**: Various NLP tasks

## 📁 Project Structure
```
D:\aarushi project final\
├── backend/                 # FastAPI server
│   ├── main.py             # Main FastAPI application
│   ├── models/             # AI models
│   ├── routes/             # API endpoints
│   ├── utils/              # Helper functions
│   └── requirements.txt    # Python dependencies
├── frontend/               # React application
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Page components
│   │   └── utils/          # Frontend utilities
│   ├── public/
│   └── package.json        # Node dependencies
├── notebooks/              # Jupyter notebooks
│   ├── EDA.ipynb          # Data analysis
│   └── ModelTraining.ipynb # Model training
├── data/                   # Dataset files
│   └── intern_data_ikarus.csv
└── README.md              # This file
```

## 🚀 Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- Git

### Backend Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your API keys
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

### Environment Variables
Create `.env` file in backend directory:
```env
PINECONE_API_KEY=your_pinecone_key
PINECONE_ENVIRONMENT=your_pinecone_env
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_key  # Optional
HUGGINGFACE_TOKEN=your_hf_token # Optional
```

## 📊 API Endpoints

### Search Endpoint
```
POST /api/search
{
  "query": "modern comfortable chair",
  "session_id": "user_session",
  "max_results": 8
}
```

### Analytics Endpoint
```
GET /api/analytics
```

## 🎨 User Experience

### Product Discovery Page
- Chat-style interface with conversation history
- Natural language queries like "Show me modern beds under $500"
- AI responses with product cards including:
  - High-quality images
  - AI-generated descriptions
  - Price and category badges
  - "View Details" buttons

### Analytics Dashboard  
- KPI cards (total products, categories, average price)
- Interactive charts for category distribution
- Price range analysis
- Material and color insights

## 🤖 AI Features

### Core Intelligence
- ✅ Natural language understanding
- ✅ Context retention during chat
- ✅ Semantic search with embeddings
- ✅ Content-based recommendations
- ✅ Query understanding (price, color, material, style)

### Furniture-Specific Features
- ✅ Category-based filtering (chairs, tables, storage, etc.)
- ✅ Material filtering (wood, metal, fabric)
- ✅ Price range recommendations
- ✅ Style matching (modern, rustic, minimalist)
- ✅ Room-based suggestions

### Personalization
- ✅ Learning user preferences
- ✅ Complementary item suggestions
- ✅ Wishlist functionality
- ✅ Comparison features

## 🎯 Example Conversations

```
User: "I want a modern sofa under $500."
Bot: "Here are 3 modern sofas under $500 👇"
      [Shows product cards with AI descriptions]

User: "Show me only grey ones."
Bot: "Sure! Filtering to grey modern sofas..."
      [Updates results with grey sofas]

User: "Add the second one to my wishlist."
Bot: "✅ Added Grey 3-Seater Modern Sofa to your wishlist. 
      Want a matching coffee table?"
```

## 🔧 Development Commands

### Backend
```bash
# Run FastAPI server
uvicorn main:app --reload

# Run tests
pytest

# Format code
black .
```

### Frontend
```bash
# Start development
npm start

# Build for production
npm run build

# Run tests
npm test
```

## 📱 Deployment

### Backend (Railway/Heroku)
```bash
# Build and deploy
railway deploy
```

### Frontend (Vercel/Netlify)
```bash
# Build and deploy
vercel --prod
```

## 🎨 Design System

### Color Palette
- **Background**: Navy to indigo gradient (#0a1f44 → #1a2a6c)
- **Cards**: Dark blue (#1e2b4d)
- **Text**: Light (#f0f4f8)
- **Accent**: Professional blue (#00bfff)

### Typography
- Clean, readable fonts optimized for dark theme
- Clear hierarchy with appropriate sizing
- High contrast for accessibility

## 🔒 Security & Performance
- CORS configuration for frontend-backend communication
- Environment variable protection for API keys
- Caching for frequent queries
- Image lazy loading
- Responsive design optimization

## 🤝 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 🚀 Deployment

This project is ready for deployment on various platforms:

### Quick Deploy Options:
- **Railway** (Backend) + **Vercel** (Frontend) - Recommended
- **Heroku** - Traditional PaaS
- **Docker** - Any container platform
- **DigitalOcean** - App Platform

### One-Click Deploy:
```bash
# With Docker
docker-compose up --build

# Manual setup
chmod +x start_production.sh
./start_production.sh
```

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## 🔧 Environment Variables

Copy `.env.example` files and configure:
- `PINECONE_API_KEY` - For semantic search
- `GEMINI_API_KEY` - For AI responses
- `FRONTEND_URL` - Your frontend domain

## 📄 License
This project is licensed under the MIT License - see LICENSE file for details.
