"""
Google Gemini AI Service for Enhanced Furniture Recommendations
Provides AI-powered product descriptions, conversational responses, and smart suggestions
"""

import os
import logging
import google.generativeai as genai
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv
import asyncio
import json

# Load environment variables
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)

class GeminiService:
    """Service for integrating Google Gemini AI with furniture recommendations"""
    
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.model = None
        self.initialized = False
        
        if self.api_key:
            try:
                genai.configure(api_key=self.api_key)
                # Try different model names based on available models
                try:
                    self.model = genai.GenerativeModel('models/gemini-2.5-flash')
                    logger.info("Using Gemini 2.5 Flash model")
                except:
                    try:
                        self.model = genai.GenerativeModel('models/gemini-flash-latest')
                        logger.info("Using Gemini Flash Latest model")
                    except:
                        try:
                            self.model = genai.GenerativeModel('models/gemini-pro-latest')
                            logger.info("Using Gemini Pro Latest model")
                        except:
                            raise Exception("No compatible Gemini models found")
                self.initialized = True
                logger.info("Gemini AI service initialized successfully")
            except Exception as e:
                logger.error(f"Failed to initialize Gemini AI: {e}")
                self.initialized = False
        else:
            logger.warning("GEMINI_API_KEY not found in environment variables")
    
    def is_available(self) -> bool:
        """Check if Gemini AI service is available"""
        return self.initialized and self.model is not None
    
    async def generate_product_description(self, product: Dict[str, Any]) -> str:
        """Generate an enhanced, creative description for a furniture product"""
        if not self.is_available():
            return product.get('description', 'No description available')
        
        try:
            # Create a detailed prompt for product description
            prompt = f"""
            As a creative furniture copywriter, write an engaging and attractive product description for this furniture item:
            
            Product Details:
            - Title: {product.get('title', 'Unknown')}
            - Category: {product.get('category', 'Furniture')}
            - Material: {product.get('material', 'Various materials')}
            - Color: {product.get('color', 'Multiple colors')}
            - Brand: {product.get('brand', 'Quality brand')}
            - Price: ${product.get('price', 'Contact for pricing')}
            - Original Description: {product.get('description', 'Quality furniture piece')}
            
            Write a compelling, friendly, and informative description that:
            1. Highlights the key features and benefits
            2. Appeals to emotions and lifestyle
            3. Mentions comfort, style, and functionality
            4. Is around 2-3 sentences long
            5. Uses enthusiastic but professional tone
            
            Focus on how this piece can enhance someone's home and lifestyle.
            """
            
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            enhanced_description = response.text.strip()
            
            if enhanced_description:
                logger.info(f"Generated enhanced description for product: {product.get('title', 'Unknown')}")
                return enhanced_description
            else:
                return product.get('description', 'Beautiful furniture piece perfect for your home.')
                
        except Exception as e:
            logger.error(f"Error generating product description with Gemini: {e}")
            return product.get('description', 'Quality furniture item for your home.')
    
    async def generate_conversational_response(self, user_query: str, products: List[Dict[str, Any]] = None) -> str:
        """Generate a conversational AI response for user queries"""
        if not self.is_available():
            return "I'm here to help you find great furniture! What are you looking for today?"
        
        try:
            # Create context about available products
            product_context = ""
            if products and len(products) > 0:
                product_context = f"\nI found {len(products)} relevant products including:\n"
                for i, product in enumerate(products[:3]):  # Show top 3
                    product_context += f"- {product.get('title', 'Unknown item')} (${product.get('price', 'N/A')})\n"
            
            prompt = f"""
            You are an enthusiastic and helpful AI furniture shopping assistant. A customer has asked: "{user_query}"
            
            {product_context}
            
            Respond in a friendly, conversational way that:
            1. Acknowledges their question/request
            2. Shows enthusiasm about helping them find furniture
            3. If products were found, briefly mention what you found
            4. Asks a follow-up question to help them better
            5. Uses emojis sparingly but appropriately
            6. Keeps response to 2-3 sentences
            7. Sounds natural and human-like
            
            Be helpful, positive, and engaging while staying professional.
            """
            
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            ai_response = response.text.strip()
            
            if ai_response:
                logger.info(f"Generated conversational response for query: {user_query}")
                return ai_response
            else:
                return "I'm excited to help you find the perfect furniture! What style or type of piece are you looking for?"
                
        except Exception as e:
            logger.error(f"Error generating conversational response with Gemini: {e}")
            return "I'm here to help you discover amazing furniture! What can I help you find today? 😊"
    
    async def enhance_search_results(self, query: str, products: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Enhance search results with AI-generated insights and descriptions"""
        if not self.is_available():
            return {
                "enhanced_message": f"Found {len(products)} products matching your search for '{query}'",
                "products": products,
                "ai_insights": None
            }
        
        try:
            # Generate AI insights about the search results
            if products:
                product_summary = []
                for product in products[:5]:  # Analyze top 5
                    product_summary.append({
                        "title": product.get('title', 'Unknown'),
                        "category": product.get('category', 'Furniture'),
                        "price": product.get('price', 0),
                        "material": product.get('material', 'Unknown')
                    })
                
                insights_prompt = f"""
                Analyze these furniture search results for the query "{query}":
                
                Products found: {json.dumps(product_summary, indent=2)}
                
                Provide brief insights about:
                1. The variety of options available
                2. Price range overview
                3. Popular materials or styles found
                4. A helpful suggestion for the customer
                
                Keep it concise (2-3 sentences) and encouraging.
                """
                
                response = await asyncio.to_thread(self.model.generate_content, insights_prompt)
                ai_insights = response.text.strip()
            else:
                ai_insights = "No products found for this search. Try different keywords or broader terms."
            
            # Generate enhanced message
            conversational_message = await self.generate_conversational_response(query, products)
            
            return {
                "enhanced_message": conversational_message,
                "products": products,
                "ai_insights": ai_insights,
                "gemini_powered": True
            }
            
        except Exception as e:
            logger.error(f"Error enhancing search results with Gemini: {e}")
            return {
                "enhanced_message": f"Found {len(products)} great furniture options for '{query}'! Let me know if you need help choosing.",
                "products": products,
                "ai_insights": "I'm here to help you find the perfect furniture for your space!",
                "gemini_powered": False
            }
    
    async def generate_greeting_response(self, greeting_type: str = "hello") -> str:
        """Generate personalized greeting responses"""
        if not self.is_available():
            return "Hello! 👋 I'm your AI furniture assistant! I'm here to help you find amazing furniture for your home!"
        
        try:
            prompt = f"""
            Generate a warm, enthusiastic greeting response for a furniture shopping assistant AI.
            The user said: "{greeting_type}"
            
            Create a response that:
            1. Returns the greeting warmly
            2. Introduces yourself as an AI furniture assistant
            3. Shows enthusiasm about helping with furniture shopping
            4. Uses 1-2 appropriate emojis
            5. Ends with a question to engage the user
            6. Is 1-2 sentences long
            7. Sounds natural and friendly
            
            Make it sound excited and helpful!
            """
            
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            greeting_response = response.text.strip()
            
            if greeting_response:
                return greeting_response
            else:
                return "Hello there! 🏡 I'm your AI furniture expert, and I'm thrilled to help you find the perfect pieces for your home! What kind of furniture are you looking for today?"
                
        except Exception as e:
            logger.error(f"Error generating greeting with Gemini: {e}")
            return "Hi! 😊 I'm your friendly AI furniture assistant! I love helping people create beautiful spaces. What can I help you find today?"
    
    async def suggest_related_products(self, current_product: Dict[str, Any], all_products: List[Dict[str, Any]]) -> List[str]:
        """Generate suggestions for products that go well with the current product"""
        if not self.is_available():
            return ["Consider matching accessories", "Look for complementary pieces", "Check out similar styles"]
        
        try:
            prompt = f"""
            A customer is looking at this furniture item:
            - {current_product.get('title', 'Furniture item')}
            - Category: {current_product.get('category', 'Unknown')}
            - Style/Material: {current_product.get('material', 'Various')}
            
            Suggest 3 types of furniture or accessories that would complement this item well.
            Focus on:
            1. Functional compatibility (what works well together)
            2. Style coordination
            3. Room completion
            
            Provide just 3 brief suggestions (like "matching coffee table" or "coordinating lamp").
            """
            
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            suggestions_text = response.text.strip()
            
            # Parse suggestions into a list
            suggestions = [s.strip() for s in suggestions_text.split('\n') if s.strip()]
            return suggestions[:3] if suggestions else ["Complementary accessories", "Matching pieces", "Room accents"]
            
        except Exception as e:
            logger.error(f"Error generating product suggestions with Gemini: {e}")
            return ["Related furniture pieces", "Complementary accessories", "Matching decor items"]

# Global instance
gemini_service = GeminiService()

async def get_enhanced_description(product: Dict[str, Any]) -> str:
    """Helper function to get enhanced product description"""
    return await gemini_service.generate_product_description(product)

async def get_conversational_response(query: str, products: List[Dict[str, Any]] = None) -> str:
    """Helper function to get conversational response"""
    return await gemini_service.generate_conversational_response(query, products)

async def enhance_search_with_gemini(query: str, products: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Helper function to enhance search results with Gemini AI"""
    return await gemini_service.enhance_search_results(query, products)