import pymongo
from bson import ObjectId

mongo_secret = "dbUserPassword"
db_name = "number_guesser"
client = pymongo.MongoClient(f"mongodb+srv://dbUser:{mongo_secret}@cluster0.ymgtu.mongodb.net/{db_name}?retryWrites=true&w=majority")
db = client.test



from pymongo import MongoClient

try:
    conn = MongoClient()
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

client.database.create_collection("number_guesser")


db = client.database

emp_rec1 = {
        "name":"Mr.Geek",
        "eid":28,
        "location":"delhi"
        }
collection = db.number_guesser

# read image
#db.test.find({"_id" : ObjectId("4ecc05e55dd98a436ddcc47c")})
image = collection.find_one({"_id" : ObjectId("60145ffab4e98eee766893fb")})

image_bytes = image["draw_data"]
import matplotlib.pyplot as plt
from PIL import Image
import io


image = Image.frombytes('RGBA', (28,28), image_bytes, 'raw')
image = image.convert('L')
image.show()
plt.imshow(image_bytes)
plt.show()


collection.insert(emp_rec1)
# Print the new record
cursor = collection.find()
for record in cursor:
    print(record)

myquery = { "name": {"$regex": "^M"} }

x = collection.delete_many(myquery)