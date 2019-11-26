import json
import mysql.connector

class MySQL():

    def __init__(self):
        pass

    def create_mysql_db_object(self,host, username, password, port, dbname):
        """
        This creates mysql db object
        """
        try:
            mydb = mysql.connector.connect(host=host, user=username,passwd=password,database=dbname,port=port, autocommit=True )
            return mydb
        except Exception as e:
            print("unable to connect to mysql " + str(e))
            exit(1)

    def load_db_meta(self):
        """
        This loads mysql data from json file
        """
        f = open('/home/harsh.s/orderfood/orderfood/db/db_details.json','r')
        try:
            db_meta = json.load(f)
        except Exception as e:
            print("Unable to load json file " + str(e))
            exit(1)
        f.close()
        return db_meta

    #TODO This function should be modified to strictly use Select query, It is preferrable to use an ORM 
    def getData(self, mydb, query):
        """
        This functions just get the data from db, should be used only for select query
        """
        mycursor = mydb.cursor()
        mycursor.execute(query)
        data = mycursor.fetchall()
        mycursor.close()
        return data

    #TODO seperate all the three operations, better to use and their verification, use an ORM 
    def cudOperations(self, mydb, query):
        """
        This function will be used to insert data into db
        """
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mycursor.close()
