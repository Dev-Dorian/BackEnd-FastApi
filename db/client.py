# Download community version: https://www.mongodb.com/try/download
# Installation: https://www.mongodb.com/docs/manual/tutorial
# MongoDB connection module: pip install pymongo
# Execution: sudo mongod --dbpath "/path/to/the/database/"
# Connection: mongodb://localhost


from pymongo import MongoClient

# Local DataBase
# db_client = MongoClient().local

# Remote Database
db_client = MongoClient(
    "mongodb+srv://USERNAME:PASSWORD@cluster0.qni8zkl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").testUsers
