import db_worker

#reads the student id from the card reader
#works for the key card format or just typing in a number
def read_card(num_string):
        try:
            if num_string[0:2] == "%A": #if a card reader is used, remove the %A that comes before the id number
                num_string = num_string[2:]
            return int(num_string[0:9]) #extract the first 9 digits
        except:
            return None


    

db = db_worker.db_worker() #connect to the database

#the program loop, the user can enter records continually
while True:
    s_id = input("\nEnter a student id, or type 'e' to exit: ")
    if s_id == 'e':
        break
    s_id = read_card(s_id)
    #if an invalid id was entered or the id isn't 9 digits
    if(s_id == None):
        print("Invalid student id format")
        continue
    if(len(str(s_id)) < 9):
            print("Student ID too short. ID should be 9 digits.")
            continue
    db.add_entry(s_id)
    print("{} entered into database.".format(s_id))
    
    
    


##pyuic5 -x file.ui -o file.py

