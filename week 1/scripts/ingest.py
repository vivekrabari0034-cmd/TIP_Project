import requests
from pymongo import MongoClient

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client["threat_db"]
collection = db["indicators"]

# Example test IP (we will replace with API later)
ips = ["8.8.8.8", "1.1.1.1"]

for ip in ips:
    if collection.find_one({"ip": ip}) is None:
        collection.insert_one({
            "ip": ip,
            "risk": "high"
        })
        print("Inserted:", ip)
    else:
        print("Duplicate:", ip)

print("Done")
