"""
Script to list available Google Gemini models
"""

import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
if api_key:
    genai.configure(api_key=api_key)
    
    print("🔍 Available Gemini Models:")
    print("=" * 40)
    
    try:
        models = genai.list_models()
        for model in models:
            print(f"📦 {model.name}")
            if hasattr(model, 'supported_generation_methods'):
                print(f"   Methods: {model.supported_generation_methods}")
            print()
    except Exception as e:
        print(f"❌ Error listing models: {e}")
else:
    print("❌ GEMINI_API_KEY not found in environment")