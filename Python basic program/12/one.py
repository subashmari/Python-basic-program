import mysql.connector
# Create the connection object
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd =
"",database="subashdb")
# Creating the cursor object
cur = myconn.cursor()
# Executing the query
cur.execute("select * from Websites")
# Fetching the rows from the cursor object
result = cur.fetchall()
print("Websites Details are :")
# Printing the result
for x in result:
 print(x);
# Commit the transaction
myconn.commit()
# Close the connection
myconn.close()
