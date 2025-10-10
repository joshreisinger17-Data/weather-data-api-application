import sqlite3

#Connects to the DB and queries data from weather table from C4
def weather_data_table():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()
#executes query and fetches rows to store them
    c.execute('''Select * from weather_record''')
    rows = c.fetchall()

    for row in rows:
        print(row)
#Closes connection to DB
    conn.close()
#Call the function
weather_data_table()


