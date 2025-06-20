from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google import genai

YOUR_API_KEY = ""

embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/embedding-001",
    google_api_key = YOUR_API_KEY
    )

client = genai.Client(api_key = YOUR_API_KEY)

model = client.models
