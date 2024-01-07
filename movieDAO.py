# This is the Data Access object (DAO) file for Data Prepresentation 2023/24 project Type A

import mysql.connector

import dbconfig as cfg

class MovieDAO:
    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.host=       cfg.mysql['host']
        self.user=       cfg.mysql['user']
        self.password=   cfg.mysql['password']
        self.database=   cfg.mysql['database']

    # makes a connection with the cursor
    def getcursor(self): 
        self.connection = mysql.connector.connect(
            host=       self.host,
            user=       self.user,
            password=   self.password,
            database=   self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def createDbTable(self):
        cursor = self.getcursor()
        sql = "CREATE TABLE movie (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, Category VARCHAR(255), Title VARCHAR(255), Director VARCHAR(255), Actor VARCHAR(255), Year INT)"
        cursor.execute(sql)
        self.closeAll()

    def closeAll(self):
        self.connection.close()
        self.cursor.close()
         
    def create(self, values):
        cursor = self.getcursor()
        # using below in order to avoid sql injection.
        sql="insert into movie (Category, Title, Director, Actor, Year) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    def getAll(self):
        cursor = self.getcursor()
        sql="select * from movie"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray

    def findByID(self, id):
        cursor = self.getcursor()
        sql="select * from movie where id = %s"
        values = (id,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def update(self, values):
        cursor = self.getcursor()
        sql="update movie set Category= %s,Title=%s, Director=%s, Actor=%s, Year=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        
    def delete(self, id):
        cursor = self.getcursor()
        sql="delete from movie where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll()
        
        print("delete done")

    def getUniqueValues(self):
        cursor = self.getcursor()
        sql = "select distinct Year from movie"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        returnArray = []
        for result in results:
            returnArray.append(result)
        self.closeAll()
        return returnArray
 
    def findByYear(self, year):
        cursor = self.getcursor()
        sql="select * from movie where Year = %s"
        values = (year,)
        cursor.execute(sql, values)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        self.closeAll()
        return returnArray

    def convertToDictionary(self, result):
        colnames=['id','Category','Title', "Director", 'Actor', 'Year']
        item = {}
        
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        
        return item
        
movieDAO = MovieDAO()