import sqlite3
import pandas as pd
from pathlib import Path

con = sqlite3.connect("database/t2dr.db")

rules_path = Path("sql/rules")

all_errors = []

for rule in rules_path.glob("*.sql"):

    
    with open(rule, "r") as file:
        query = file.read()
        
    errors = pd.read_sql_query(query, con)
    
    all_errors.append(errors)
    
if all_errors:
    
    fact_errors = pd.concat(all_errors, ignore_index=True)
    
    print("\nTotal Errors")
    print(len(fact_errors))
    
else:
    
    fact_errors = pd.DataFrame()
    
    print("No validation errors found.")
    
con.close()