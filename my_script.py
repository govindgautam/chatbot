import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load .env file
load_dotenv()

# Fetch API Key
openai_api_key = os.getenv("OPENAI_API_KEY")  # ✅ Corrected Variable Name

# Debugging Step (Check if API Key is Loaded)
if openai_api_key is None:
    print("❌ ERROR: OPENAI_API_KEY not found! Check your .env file.")
else:
    print("✅ OpenAI API Key loaded successfully.")

# Initialize OpenAI LLM
Open_llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=openai_api_key
)