# Personal advice
## No need to setup a field called 'id' manully
* the inserting process of MongoDB will return a unique ObjectId. By using `bson` you can translate the ObjectId to the value that actually saved in the '_id' field of the file saved in the database.
* draw_back: the ObjectId returned automatically has no order
