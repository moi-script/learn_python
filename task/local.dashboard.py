# The Project: Local Finance Dashboard
# Instead of just a basic "expense list," this project requires you 
# to build a system that categorizes spending, saves data locally, and generates a visual summary.

# 1. Key Features to Implement
# Data Persistence: Store transactions in a CSV
# or SQLite database (no API needed, just local storage).



# CRUD Operations: Create, Read, Update, and Delete transactions.

# Data Analysis: Use Pandas to calculate monthly averages and spending by category.
# Visualization: Use Matplotlib or Seaborn to generate pie charts of your spending.
# Interactive Menu: Build this using a Library like Typer 
# (for a professional CLI) or Tkinter/PyQt (for a windowed app).

# 2. Why this is "Intermediate"
# It moves beyond basic syntax and forces you to think about Data Modeling. You have to decide how to handle dates, 
# how to ensure the user doesn't enter "abc" for a price, and how to represent that data visually.




# category , timestamp

# month , year

# combined all computed result to specific month (sum all amount)



# average 

# it ask user to inter a choice

# choices like -> number 1, 2, 3, or type e to exit 
import logging
import sqlite3
from datetime import datetime

logging.basicConfig(level=logging.ERROR)

# init database
def initDb(): 
    with sqlite3.connect("app.db") as conn :
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS "transaction" (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT NOT NULL,
                price INTEGER,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()



# get user input from cli
def getUserTransaction() :
    transact = {
        "type" : "",
        "price" : ""  
    }
    
    i =0
    lt = len(transact)
    ltKeys = list(transact.keys())
    while lt > 0 :
        ins = input(f"Enter your {ltKeys[i]} : ")
        if i != 0 :
            try : 
                transact[ltKeys[i]] = int(ins)
                return transact
            except :
                logging.error(f"Unable to convert {ltKeys} to integer input is {ins} ")    
                break
        transact[ltKeys[i]] = ins
        
        lt -= 1
        i += 1
    return transact
        


# db business logic 
def post_user_transaction (type, price) :
     try : 
         with sqlite3.connect("app.db") as conn :
             cursor = conn.cursor()
             cursor.execute("INSERT INTO 'transaction' (category, price) VALUES (?, ?) ", (type, price))
             conn.commit()
             
             print(f"Successfully updated user trnasation")
     except Exception as e :
         logging.error(f"Post error {e}") 
        
        
def get_all_users():
    with sqlite3.connect("app.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM 'transaction'")
        return cursor.fetchall()







# filters 

def filter_by_category (dbContents, type):
    return filter(lambda a : a == type, dbContents)

def filter_by_date(dbContents, type) :
    return filter(lambda a : a == type, dbContents)
    
    
def dateFormat(date_input) :
    date_obj = datetime.strptime(date_input, "%Y-%m-%d %H:%M:%S")
    
    year = date_obj.strftime("%y")     # 26
    day = date_obj.strftime("%d")    # Output: 27
    month_num = date_obj.strftime("%m")      # Output: 02    
    
    return {
        "month_num" : month_num,
        "year" : year,
        "day" : day
        
    }
# print(dateFormat("2026-02-26 16:27:16"))



# cli control
def userCli(choice) :
    match int(choice) :
        case 1 :
            # print(1)
            transaction = getUserTransaction()
            post_user_transaction(**transaction)
        case 2 : 
            print(2)
            transactionList = get_all_users()
            print(transactionList)
        case 3 :
            print(3)
        case _ :
            print("Not matched")

# question loops
def userLoop() :
    while True :
        user_input = input("""
        1. Create a transaction
        2. Read user transaction
                           """)
        
        try :
            if user_input.isdigit() :
                # print("Valid input")
                userCli(user_input)
            else :
                raise Exception("Not a valid input -> " + user_input)
        except Exception as e :
            logging.error(f"Error occured : {e}")
            break
            
            
initDb()
userLoop()


# getUserTransaction()