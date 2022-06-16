import sqlite3

def CreateTable():
    try:
        createQuery = 'Create table book (Id INT PRIMARY KEY NOT NULL, Name Text NOT NULL, director Text NOT NULL)'
        dbConn.execute(createQuery)
        print('Created table successfully')
    except:
        print('Could not create the table')

def ReadDataFromTable(tableName,selectColumns='*', whereClause=''):
    print('Values from {} table'.format(tableName))
    selectQuery = "select {columns} from {tblName} {clause}".format(tblName=tableName, columns=selectColumns, clause=whereClause)
    try:
        rows = dbConn.execute(selectQuery)
        for row in rows:
            print(row)
    except:
        print('Could not execute the query ', selectQuery)
def insertData(tableName,val):  
    insert_query = "insert into {} values ({})".format(tableName,val)
    print(insert_query)
    try: 
        dbConn.execute(insert_query)
        dbConn.commit()
    except:
        print("Unable to insert")
try:
    dbConn = sqlite3.connect('sqllite.sqlite3')
    print('Successfully connected to the database')
    ReadDataFromTable('Movies')
    # ReadDataFromTable('book','name, director')
    insertData("Movies",'8,"titanic"')
except:
    print('Error connecting to the database')
finally:
    if(dbConn):
        dbConn.close()