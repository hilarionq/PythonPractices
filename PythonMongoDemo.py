import pymongo
import datetime
from pymongo import MongoClient
import pprint


client = MongoClient('mongodb://localhost:27017') # Using the MongoDB URI format

db = client['test-database']

collection = db['test-collection']

post = {
    "author" : "Mike", 
    "text" : "My first blog post!",
    "tags" : ['mongodb', 'python', 'pymongo'],
    "date" : datetime.datetime.utcnow()
}

# inserting a document
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# list all own collections

db.collection_names(include_system_collections=False)

# printing the firs record
import pprint

pprint.pprint(posts.find_one())

# getting a record that's fulfill a condition
pprint.pprint(posts.find_one({"author" : "Mike"}))

# getting an empty outcome
pprint.pprint(posts.find_one({"author" : "Eliot"}))

# getting a record by id
from bson.objectid import ObjectId
pprint.pprint(posts.find_one({"_id" : post_id}))

# getting a empty record by the same id as str
post_id_as_str = str(post_id)
pprint.pprint(posts.find_one({"_id" : post_id_as_str}))

# getting a record from str id through converting it in ObjectId
pprint.pprint(posts.find_one({"_id" : ObjectId(post_id_as_str)}))

#bulk inserts

new_posts = [{"author": "Mike",
     "text": "Another post!",
     "tags": ["bulk", "insert"],
     "date": datetime.datetime(2009, 11, 12, 11, 14)},
    {"author": "Eliot",
     "title": "MongoDB is fun",
     "text": "and pretty easy too!",
     "date": datetime.datetime(2009, 11, 10, 10, 45)}]

result = posts.insert_many(new_posts) # instead of using isert_one we use insert_many
result.inserted_ids

# Counting

posts.count()



















