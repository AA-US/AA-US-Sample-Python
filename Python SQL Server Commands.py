#Install libs
import pandas as pd
import pyodbc # lib to connect to ODBC DB's


#Create a connection to database & validating connection

# One way to connect - default instance & windows authentication
servername = "localhost"
db = "TestingPython"

# Exception Handling
try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + servername + '; DATABASE='+ db + ';Trusted_Connection=yes')

    cursor=conn.cursor()

    print()
    print("Successfully connected to SQL Server.")
    print()

    cursor.close()
    conn.close()

except pyodbc.Error as ex:
    print()
    print("Exception: ",ex)    
    print("Closing program...")
    print()
    exit()

print()

# Second way _ named instance 
#conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=putservername/putinstancename;Database=put database name;Trusted_Connection=yes;')

#Connect, run query close cursor and connection


servername = "localhost"
db = "TestingPython"

# Exception Handling
try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + servername + '; DATABASE='+ db + ';Trusted_Connection=yes')

    cursor=conn.cursor()

    cursor.execute("SELECT @@VERSION as version")

    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.version)

    print()
    print("Successfully connected to SQL Server.")
    print()

    cursor.close()
    conn.close()

except pyodbc.Error as ex:
    print()
    print("Exception: ",ex)
    cursor.close()
    connection.close()
    print("Closing program...")
    print()
    exit()

print()


# Running a simple query and printing results on screen


servername = "localhost"
db = "TestingPython"
try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + servername + '; DATABASE='+ db + ';Trusted_Connection=yes')
    cursor=conn.cursor()

    # SELECT Query - No User Parameter
    # Execute query
    cursor.execute("SELECT * FROM employees")
   

    print("[Query 1 Results...]")
    while 1:
        row = cursor.fetchone()
        if not row:
            break
        print(row.name,row.username,row.password,row.email, row.roleid)

    cursor.close()
    conn.close()    

except pyodbc.Error as ex:
    print("Exception: ",ex)
    cursor.close()
    conn.close()
    print("Closing program...")
    print()
    exit()

print()


# Run Select and load to dataframe

servername = "localhost"
db = "TestingPython"

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + servername + '; DATABASE='+ db + ';Trusted_Connection=yes')

sql = """
Select name , 
count(employeeid)as NOs From employees
group by name 

"""

df = pd.read_sql(sql,conn)
df.head()
