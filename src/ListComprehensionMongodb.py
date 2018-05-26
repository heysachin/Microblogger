

# Created by Sachin Dev on 26/05/18


import pymongo

uri = "mongodb://127.0.0.1:27017"

client = pymongo.MongoClient(uri)
database = client['demo']
collection = database['demo']

# students=collection.find({})
students=[student['name'] for student in collection.find({'name':"Sachin Dev. S"})]
print (students)

students=[student for student in collection.find({})]

print (students)
