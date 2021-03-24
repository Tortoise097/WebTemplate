# How to setup MongoDB daemon

## Install MongoDB

https://docs.mongodb.com/manual/administration/install-community/

you shall have a directory now, at least containing `mongo`, `mongod`, `mongos`

## goto the directory which contains the app called `mongod`

Yes, the 'd' at the end of mongod means daemon.

## add a mongodb.conf file

```
dbpath = /Users/dee_why/Documents/db/var/mongodb
logpath = /Users/dee_why/Documents/db/var/log/mongodb/mongodb.log
logappend = true
port = 27017
bind_ip = 0.0.0.0
fork = true
# for safety
auth = true
```

three things that you should edit on the above example when you want to apply it to your own development

* dbpath : should be any empty directory that you planned to store your data
* logpath : should be an empty file named mongodb.log (create it on your own)
* bind_ip : 0.0.0.0 is safe&easy_to_use for developers, but not safe enough(we have auth=true to protect the data), you can change it.

## then use the command line in the directory that contains `mongod` and `mongodb.conf`

`mongod -f mongodb.conf`

## to see whether we success use the following command

`ps aux | grep -v grep | grep mongod`

if you see a line like this:

`dee_why          89284   0.2  0.1  5555888  17500   ??  S    Sun10PM  10:50.48 mongod -f mongodb.conf`

Congratulations !

## how to shut down a mongodb daemon

first goto the. Directory of `mongo`

```shell
./mongo
use admin
db.shutdownServer()
exit
```



