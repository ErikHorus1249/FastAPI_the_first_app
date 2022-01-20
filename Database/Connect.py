from pymongo import MongoClient

MONGODB_URL=f'mongodb+srv://plum:q6Ur6p62KgDr5!Y@cluster0.p0gju.mongodb.net/**test**?retryWrites=true&w=majority'
client = MongoClient(MONGODB_URL)
conn = client.get_database("test")
