from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["ebook_reader"]

users = db["users"]
word_history = db["word_history"]
book_history = db["book_history"]
