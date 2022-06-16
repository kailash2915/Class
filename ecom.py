import pymongo
#Pymongo - ORM (Object relational mapping)
try:
    #to establish the connection between mongodb and python and we keep a variable to assign the connection link, where pymongo.MongoClinet("link") is the default syntax to establish thr connection.
    connection = pymongo.MongoClient("mongodb+srv://kailash_96:808438KsK@cluster0.artsc.mongodb.net/E-commerce?retryWrites=true&w=majority");
    #to open the database we need to go into the connection and mention the db name and assign it to a variable.
    myDb = connection["E-commerce"]
    print(myDb.list_collection_names())
    if "Products" in myDb.list_collection_names():
        #to open  the collection from the database we already opened and assigned it in a variable.
        collection = myDb["Products"]
        collection1= myDb["Kids Section"]
        print("Collection found")
        data={"name":"Iphone 13","Price":"$2000","Make Year":"2021","previous version":["iphone 12","iphone 11"]}
        car={"brand":"BMW","Price":"$60000"}
        collection.insert_one(car)
        bathSet = {"Brand":"Johnson and Johnsons", "Soap":3, "Powder":1,"Cerelac":"1 kg"}
        collection1.insert_one(bathSet)
        print("s")
        try:
            collection.insert_one(data)
            for i in collection.find():
                print(i)
        except Exception as e:
            print ("Insert",e);
        
except Exception as e:
    print (e);