import pymongo

conn = pymongo.MongoClient()

"""
db = conn.example
widgets = db.widgets
widgets.insert({"foo": "bar"})
print db.collection_names()
widgets.insert({"name": "flibnip", "description": "grade-A industrial flibnip", 
                "quantity": 3})
print widgets.find_one({"name": "flibnip"})
doc = db.widgets.find_one({"name": "flibnip"})
doc['quantity'] = 4
db.widgets.save(doc)
print widgets.find_one({"name": "flibnip"})

import json
del doc["_id"]
print json.dumps(doc)
"""

db = conn.bookstore
db.books.insert({
     "title":"Programming Collective Intelligence",
     "subtitle": "Building Smart Web 2.0 Applications",
     "image":"/static/images/Lighthouse.jpg",
     "author": "Toby Segaran",
     "date_added":1310248056,
     "date_released": "August 2007",
     "isbn":"978-0-596-52932-1",
     "description":"Web services for the real world"
     })

db.books.insert({
     "title":"RESTful Web Services",
     "subtitle": "Web services for the real world",
     "image":"/static/images/Tulips.jpg",
     "author": "Leonard Richardson, Sam Ruby",
     "date_added":1311148056,
     "date_released": "May 2007",
     "isbn":"978-0-596-52926-0",
     "description":"Web services for the real world"
     })

# db.books.remove({
#      "image":"/static/images/Tulips.jpg",
#      })
# db.books.remove({
#      "image":"/static/images/Lighthouse.jpg",
#      })
# db.books.remove({
#      "image":"/static/images/Penguins.jpg",
<<<<<<< HEAD
#      })
=======
#      })

import tornado.httpclient
import json
import time

def on_response(response):
    print "on_response"
    body = json.loads(response)
    print body

client = tornado.httpclient.AsyncHTTPClient()
rst = client.fetch("htt;://www.sina.com", callback = on_response)
print rst
time.sleep(10)
>>>>>>> 0fccc59d65457cbf7ad1c457f4939e4eeded1d6e
