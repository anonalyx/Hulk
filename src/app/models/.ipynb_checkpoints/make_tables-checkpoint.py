import sqlite3

def connect(db_filename):
    # Adds .db to filename if necessary
    if db_filename[-3:] != '.db':
        db_filename += '.db'
        
    conn = sqlite3.connect(db_filename)
    c = conn.cursor()
    
    return conn, c

def create(table):
    # Adds .txt to filename if necessary
    if table[-4:] != '.txt':
        table += '.txt'

    command = open(table, "r")
    c.execute(command.read())
    command.close()

def insert(value, table):
    command = "INSERT INTO " + table + " VALUES ("
    
    col_count = c.execute(
        "SELECT count() FROM PRAGMA_TABLE_INFO('" + table + "');"
    )
    
    col_count = col_count.fetchall()
    col_count = col_count[0][0]
    
    for i in range(col_count - 1):
        command += "?, "
    
    command += "?);"
    #print(command)
    
    c.execute(command, value)
    conn.commit()

def drop(table):
    command = "DROP TABLE IF EXISTS " + table
    c.execute(command)

def drop_all():
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")

    for table in c.fetchall():
        drop(table[0])

def print_database():
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print ("Tables:")
    
    for t in c.fetchall() :
        print ("\t[%s]"%t[0])
        print ("\tColumns of", t[0])
        c.execute("PRAGMA table_info(%s);"%t[0])
        
        for attr in c.fetchall() :
            print ("\t\t", attr)
            
        print()

def print_table(table):
    data = c.execute("SELECT * FROM " + table)

    for row in data:
        print(row)

conn, c = connect("testing_tables")

table_list = [
    "account",
    "body_part",
    "equipment",
    "exercise",
    "favorite"
]

for table in table_list:
    create(table)

print_database()

insertions = {
    "body_part": [
        (0, "Arms", "Bicep Curl"),
        (1, "Back", "Rows"),
        (2, "Legs", "Squats"),
        (3, "Abs", "Sit-Ups"),
        (4, "Cardio", "Running")
    ],
    
    "equipment": [
        (0, "None"),
        (1, "Dumbells"),
        (2, "Single Dumbell"),
        (3, "Body Weight")
    ],
    
    "exercise": [
        (0, "Bicep Curl", "Curls dumbbells from a standing position", 
         "Arms", "Dumbells"),
        
        (1, "Rows", "Pulls dumbbells towards the chest while bending over", 
         "Back", "Dumbells"),
        
        (2, "Squats", "Lowers body by bending at the hips and knees", 
         "Legs", "Body Weight"),
        
        (3, "Sit-Ups", 
         "Lifts upper body towards knees while lying on the ground", 
         "Abs", "Body Weight"),
        
        (4, "Running", "Fast-paced movement using legs and feet", 
         "Cardio", "None")
    ],
    
    "account": [
        (0, "user1", "user1@example.com"),
        (1, "user2", "user2@example.com"),
        (2, "user3", "user3@example.com")
    ],
    
    "favorite": [
        (0, "user1", "Bicep Curl"),
        (1, "user2", "Rows"),
        (2, "user3", "Squats")
    ]
}

for table, value_list in insertions.items():
    for value in value_list:
        insert(value, table)
        
    print("\n" + table)
    print_table(table)

drop_all()
