from langchain_google_genai import GoogleGenerativeAIEmbeddings
from google import genai

embeddings = GoogleGenerativeAIEmbeddings(
    model = "models/embedding-001",
    google_api_key = "AIzaSyD0I7tw8w9wo3c7BFebS9PeJimi_GJWkT0"
    )

client = genai.Client(api_key = "AIzaSyD0I7tw8w9wo3c7BFebS9PeJimi_GJWkT0")

model = client.models