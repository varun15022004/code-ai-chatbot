"""
Test script to verify Google Gemini AI integration
"""

import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.services.gemini_service import gemini_service

async def test_gemini_integration():
    """Test Gemini AI service integration"""
    
    print("🧪 Testing Gemini AI Integration...")
    print("=" * 50)
    
    # Test 1: Check if Gemini is available
    print(f"✅ Gemini AI Available: {gemini_service.is_available()}")
    
    if not gemini_service.is_available():
        print("❌ Gemini AI is not available. Check your API key and environment setup.")
        return
    
    # Test 2: Test greeting generation
    print("\n🤝 Testing Greeting Generation...")
    try:
        greeting = await gemini_service.generate_greeting_response("hello")
        print(f"Greeting Response: {greeting}")
    except Exception as e:
        print(f"❌ Greeting test failed: {e}")
    
    # Test 3: Test conversational response
    print("\n💬 Testing Conversational Response...")
    try:
        response = await gemini_service.generate_conversational_response("I need a comfortable sofa")
        print(f"Conversational Response: {response}")
    except Exception as e:
        print(f"❌ Conversational test failed: {e}")
    
    # Test 4: Test product description enhancement
    print("\n📝 Testing Product Description Enhancement...")
    try:
        sample_product = {
            "title": "Modern Ergonomic Office Chair",
            "category": "Office Furniture",
            "material": "Fabric",
            "color": "Black",
            "brand": "ComfortCorp",
            "price": 299.99,
            "description": "Office chair with ergonomic design"
        }
        
        enhanced_desc = await gemini_service.generate_product_description(sample_product)
        print(f"Enhanced Description: {enhanced_desc}")
    except Exception as e:
        print(f"❌ Product description test failed: {e}")
    
    # Test 5: Test search enhancement
    print("\n🔍 Testing Search Enhancement...")
    try:
        mock_products = [
            {"title": "Leather Sofa", "price": 899.99, "category": "Living Room", "material": "Leather"},
            {"title": "Coffee Table", "price": 299.99, "category": "Living Room", "material": "Wood"}
        ]
        
        enhanced_search = await gemini_service.enhance_search_results("comfortable living room furniture", mock_products)
        print(f"Enhanced Message: {enhanced_search['enhanced_message']}")
        print(f"AI Insights: {enhanced_search['ai_insights']}")
    except Exception as e:
        print(f"❌ Search enhancement test failed: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 Gemini AI Integration Test Complete!")

if __name__ == "__main__":
    asyncio.run(test_gemini_integration())