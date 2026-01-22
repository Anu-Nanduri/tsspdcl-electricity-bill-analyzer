print("Electricity Bill Analyzer Starting...")
import sqlite3
print("SQLite loaded successfully")

# Hyderabad TSSPDCL tariff rates
def calculate_bill(units):
    if units <= 100:
        return round(units * 3.95, 2)
    elif units <= 200:
        return round(100*3.95 + (units-100)*5.25, 2)
    else:
        return round(100*3.95 + 100*5.25 + (units-200)*7.45, 2)

# Create database
conn = sqlite3.connect('bills.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS usage 
             (month TEXT PRIMARY KEY, units INTEGER)''')

# Add sample Hyderabad household data
data = [('Jan-25', 180), ('Feb-25', 195), ('Mar-25', 210)]
c.executemany("INSERT OR REPLACE INTO usage VALUES (?, ?)", data)
conn.commit()

print("\nHyderabad TSSPDCL Electricity Bill Analyzer")
print("=====================================")
print("\nSample Bills:")
for month, units in c.execute("SELECT * FROM usage"):
    bill = calculate_bill(units)
    print(f"{month}: {units} units = Rs {bill}")

print("\nYour Python + SQL project is WORKING!")
conn.close()
