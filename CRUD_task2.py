#!/usr/bin/env python
# coding: utf-8

# In[6]:


#created the connection between mongodb and python .
import pymongo
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')


# In[8]:


#database named monogotask has been created and stored as db.
db = client["mongotask"]


# In[36]:


#new collection named tele_dir is created and stored in tele_dir.
tele_dir = db.tele_dir


# In[35]:


#to show list of collections in database
db.list_collection_names()


# In[19]:


#created a document,for inserting into the tele_dir collection . 
telephone_directory = [{"_id":1,
                       "first_name" :"Tharunesh",
                       "lat_name"   :"M",
                       "countrycode":"+91",
                       "phonenumber":int(8778278970),
                       "address"    :"#41,periyakovil st,viruthunagar",
                       "location"   :{"city":"viruthunagar","state"  :"TamilNadu",
                                      "country":"India"}},
                       {"_id":2,
                       "first_name" :"Rohit",
                       "lat_name"   :"M",
                       "countrycode":"+91",
                       "phonenumber":int(9789877553),
                       "address"    :"#42,periyakovil st,gundur",
                       "location"   :{"city":"gundur",
                                      "state"  :"AndhraPradesh",
                                      "country":"India"}},
                       {"_id":3,
                       "first_name" :"Lokesh",
                       "lat_name"   :"K",
                       "countrycode":"+91",
                       "phonenumber":int(9788278970),
                       "address"    :"#41,periyakovil st,yangotok",
                       "location"   :{"city":"yangotok",
                                      "state"  :"Sikkim",
                                      "country":"India"}},
                       {"_id":4,
                       "first_name" :"Raj Kumar",
                       "lat_name"   :"S",
                       "countrycode":"+91",
                       "phonenumber":int(877827098),
                       "address"    :"#41,pampa st,cochin",
                       "location"   :{"city":"cochin",
                                      "state"  :"Kerala",
                                      "country":"India"}},
                         {"_id":5,
                       "first_name" :"Rokesh",
                       "lat_name"   :"M",
                       "countrycode":"+91",
                       "phonenumber":int(9788278989),
                       "address"    :"#41,Anna st,arakkonam",
                       "location"   :{"city":"arakkonam",
                                      "state"  :"TamilNadu",
                                      "country":"India"}},
                         {"_id":6,
                       "first_name" :"vinish",
                       "lat_name"   :"K",
                       "countrycode":"+91",
                       "phonenumber":int(9788278971),
                       "address"    :"#41,karunesh st,yangotok",
                       "location"   :{"city":"yangotok",
                                      "state"  :"Sikkim",
                                      "country":"India"}},
                         {"_id":7,
                       "first_name" :"Anish",
                       "lat_name"   :"S",
                       "countrycode":"+91",
                       "phonenumber":int(9788278790),
                       "address"    :"#41,periyakovil st,yangotok",
                       "location"   :{"city":"yangotok",
                                      "state"  :"Sikkim",
                                      "country":"India"}},
                         {"_id":8,
                       "first_name" :"Ayesha",
                       "lat_name"   :"K",
                       "countrycode":"+91",
                       "phonenumber":int(9788728970),
                       "address"    :"#41,mount st,yangotok",
                       "location"   :{"city":"kozehodu",
                                      "state"  :"kerala",
                                      "country":"India"}},
                         {"_id":9,
                       "first_name" :"sudha",
                       "lat_name"   :"K",
                       "countrycode":"+91",
                       "phonenumber":int(9799278970),
                       "address"    :"#41,peacock st,karana",
                       "location"   :{"city":"karna",
                                      "state"  :"karnataka",
                                      "country":"India"}},
                         {"_id":10,
                       "first_name" :"Teja",
                       "lat_name"   :"K",
                       "countrycode":"+91",
                       "phonenumber":int(9787258970),
                       "address"    :"#41,rayasema st,kadapa",
                       "location"   :{"city":"kadapa",
                                      "state"  :"AndhraPradesh",
                                      "country":"India"}},
                         {"_id":11,
                       "first_name" :"Prem",
                       "lat_name"   :"M",
                       "countrycode":"+91",
                       "phonenumber":int(8788278970),
                       "address"    :"#41,periyakovil st,theni",
                       "location"   :{"city":"theni",
                                      "state"  :"TamilNadu",
                                      }},
                         {"_id":12,
                       "first_name" :"Jeni",
                       "lat_name"   :"J",
                       "countrycode":"+91",
                       "phonenumber":int(6388278970),
                       "address"    :"#41,poda st,poovana",
                       "location"   :{"city":"poovana",
                                      "state"  :"karnataka",
                                      }},]


# In[ ]:


# inserting the above created document.
#tele_dir.insert_one(telephone_directory)


# In[20]:


if isinstance(telephone_directory,list):
    tele_dir.insert_many(telephone_directory)
else:
    tele_dir.insert_one(telephone_directory)


# In[21]:


#query the one data from the collection tele_dir
tele_dir.find_one()


# In[27]:


#finding by skipping first document _id =0 and limited the document to 3:
skipped = tele_dir.find().skip(1).limit(3)


# In[28]:


for i in skipped:
    print (i)


# In[42]:


#sorting the based on id:
sort=tele_dir.find().sort('_id',-1).limit(3)


# In[43]:


for i in sort:
    print(i)


# In[52]:


#sorting based on state: here in this sorting done in descending order first lower case letter and upper case
sort_state = tele_dir.find().sort('location.state',-1)


# In[53]:


for i in sort_state:
    print(i)


# In[58]:


# querying out state name staring with lowercase ka
reg=tele_dir.find({'location.state':{'$regex':'^ka'}})


# In[59]:


for i in reg:
    print(i)


# In[62]:


not_exists=tele_dir.find({'location.country':{'$exists':False}})


# In[63]:


for i in not_exists:
    print(i)


# In[64]:


#update,country to location:
up_country = tele_dir.update_many({'location.country':{'$exists':False}},{'$set':{"location.country":"India"}})


# In[67]:


#checking after update 
up_check = tele_dir.find({'location.country':{'$exists':False}})    


# In[69]:


#no output will be generated
for i in up_check:
    print(i)


# In[73]:


#to confrim again id 11 and 12 does not had country fields: have a look with In[63] to check the updated
check_upA = tele_dir.find({'$and':[{'_id':{'$in':[11,12]}}]})


# In[74]:


for i in check_upA:
    print(i)


# In[75]:


#lets delete one:
tele_dir.delete_one({})


# In[76]:


#_id = 0 is deleted by delete_one 
tele_dir.find_one()


# In[77]:


#lets insert id = 0 again
telephone_directory={'_id': 0,
              'first_name': 'Thamizhiniyan',
                'lat_name': 'A.T',
             'countrycode': '+91',
             'phonenumber': 8778295795,
                 'address': '#40,karuppukovil,viruthunagar',
                'location': {'state': 'TamilNadu', 'country': 'India'}}


# In[78]:


tele_dir.insert_one(telephone_directory)


# In[85]:


a = tele_dir.find().sort('_id',1)


# In[86]:


for i in a:
    print(i)


# In[91]:


# lets look at the keys first:
allKeys= tele_dir.find_one()
for key in allKeys:
    print(key)


# In[101]:


# lets rename the lat_name in the telephone directory
rename=tele_dir.update_many({'_id':{'$exists':True}},
                            {'$rename':{'lat_name':"last_name"}}
                            )


# In[102]:


allKeys= tele_dir.find_one()
for key in allKeys:
    print(key)


# In[108]:


#add gender to telephone directory:
set_gender = tele_dir.update_many({'_id':{'$exists':True}},
                     {'$set':{'gender':'male'}})


# In[111]:


for i in tele_dir.find():
    print(i)


# In[114]:


for i in tele_dir.aggregate([{'$project':{'first_name':1}}]):
    print(i)


# In[115]:


change_gender = tele_dir.update_many({'_id':{'$in':[8,9,12]}},{'$set':{'gender':'female'}})


# In[117]:


for i in tele_dir.aggregate([{'$project':{'first_name':1,'gender':1}}]):
    print(i)


# In[ ]:




