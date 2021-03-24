import pymongo
username = input('please input your username: ')
password = input('please input your password: ')
my_url = 'mongodb://' + username + ':' + password + '@127.0.0.1:27017/' # if you write the url this way, the MongoDB should be hosted on the local machine and the default port:27017

myclient = pymongo.MongoClient(my_url)

mydb = myclient[username]

User_collection = mydb.User_collection # creating a new table (so easy)

post = {'id':0, 'username':'example_username', 'email':'example_email@pku.edu.cn', 'pwd':'example_pwd', 'salt':'example_salt'}

post_id = User_collection.insert_one(post).inserted_id # insertion return a unique object id that we could use to search for it latter

# lets see what we've done
import pprint

item = User_collection.find_one({'username':'example_username'})
pprint.pprint(item)

item = mydb.User_collection.find_one({'username':'example_username'})
pprint.pprint(item)

item = myclient[username].User_collection.find_one({'username':'example_username'})
pprint.pprint(item)

# lets use the _id returned by insertion, but becareful, we need to use bson.objectid.ObjectId for preprocessing
from bson.objectid import ObjectId
pprint.pprint(mydb.User_collection.find_one({'_id':ObjectId(post_id)}))
