#The logic for connecting to and performing necesary queries on the database
import mysql.connector

class db_worker:
    #the constructor
    def __init__(self):
        self.connect()

    #inserts s_id and Timestamp into the database
    def add_entry(self, s_id):
        cursor = self.db.cursor()
        sql_statement = "INSERT INTO card_swipes VALUES ('{}', CURRENT_TIMESTAMP)".format(s_id)
        cursor.execute(sql_statement)
        self.db.commit()

    #searches for records in the database based on the applied filters   
    def search_db(self, s_id = None, date = None, start_hour = None, start_minute = None, end_hour = None, end_minute = None):

        
        query = "SELECT * FROM Card_Swipes" #the start of the query
        where_clauses = [] #a list of clauses that will be added to the WHERE section

        
        if s_id != None: #if filtering by student ID
            where_clauses.append("s_id = " + str(s_id)) 
        if date != None: #if filtering by date
            where_clauses.append("DATE(swipe_time) = DATE('" + str(date) + "')")
        if start_hour != None: #if filtering by time range
            where_clauses.append(" (EXTRACT(Hour FROM swipe_time) > " + str(start_hour) + " OR (EXTRACT(Hour FROM swipe_time) = " + str(start_hour) + " AND EXTRACT(Minute FROM swipe_time) >= " + str(start_minute) + ")) ")
            where_clauses.append(" (EXTRACT(Hour FROM swipe_time) < " + str(end_hour) + " OR (EXTRACT(Hour FROM swipe_time) = " + str(end_hour) + " AND EXTRACT(Minute FROM swipe_time) <= " + str(end_minute) + ")) ")
        #if at least one where clause is present
        if len(where_clauses) != 0:
            query += " WHERE "
            #add all the where clauses to the query separated by "AND"
            for i in range(len(where_clauses)):
                query += where_clauses[i]
                if i != len(where_clauses) - 1:
                    query += " AND "

        #order results from most to least recent
        query += " ORDER BY swipe_time DESC;"
        cursor = self.db.cursor()
        cursor.execute(query)
        result = cursor.fetchall() #return a list of all result tuples
        return result
        


    #connect to the database
    def connect(self):
          #the login information is hardcoded
          self.db = mysql.connector.connect(
          host="localhost",
          user="root",
          password="admin",
          database = "new_schema"
            )
