from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Connected ✅")
except Exception as e:
    print("Error:", e)

db = client["genai_db"]
collection = db["responses"]

data = {"name": "Narmatha"}
collection.insert_one(data)

print("Data inserted 🚀")