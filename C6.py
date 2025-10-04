import sqlite3

def weather_data_table():
    conn = sqlite3.connect('weather.db')
    c = conn.cursor()

    c.execute('''Select * from weather_record''')
    rows = c.fetchall()

    for row in rows:
        print(row)

    conn.close()

weather_data_table()


