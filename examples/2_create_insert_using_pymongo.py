import pymongo
import datetime
username = input('please input your username: ')
password = input('please input your password: ')
my_url = 'mongodb://' + username + ':' + password + '@127.0.0.1:27017/' # if you write the url this way, the MongoDB should be hosted on the local machine and the default port:27017

# connect to the local MongoDB
myclient = pymongo.MongoClient(my_url)

mydb = myclient[username]


# create table & insert data
user_collection = mydb.user_collection # creating a new table (so easy)

post1 = {'id':0, 'username':'example_username', 'email':'example_email@pku.edu.cn', 'pwd':'example_pwd', 'salt':'example_salt'}

post_id_1 = user_collection.insert_one(post1).inserted_id # insertion return a unique object id that we could use to search for it latter

# create table & insert data
task_collection = mydb.task_collection # creating a new table (so easy)

post2 = {'task_id':0, 'task_name':'example_task_name', 'owner':'example_owner', 'created_time':datetime.datetime.utcnow(), 'configspace':'example_configspace', 'status':'processing', 'advisor_type':'SMBO', 'max_run':100, 'surrogate_type':'gp', 'time_liit_per_trial':600}

post_id_2 = task_collection.insert_one(post2).inserted_id # insertion return a unique object id that we could use to search for it latter

# create table & insert data
runhistory_collection = mydb.runhistory_collection # creating a new table (so easy)

post3 = {'runhistory_id':0, 'task_id':'example_task_id', 'user_id':'example_user_id', 'config':'example_config', 'result':'example_result', 'trial_status':'unfinished'}

post_id_3 = runhistory_collection.insert_one(post3).inserted_id # insertion return a unique object id that we could use to search for it latter




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
