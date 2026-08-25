import sqlite3
import pandas as pd
from datetime import date
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
    
    validation_results = pd.concat(all_errors, ignore_index=True)
    
    validation_results["RunDate"] = date.today().isoformat()
    
    validation_results["ProgrammeName"] = "T2DR - Stoke and Staffordshire"
    
    validation_results.to_sql("stg_validation_results",
                              con,
                              if_exists="replace",
                              index=False)
    
    print("\nTotal Errors")
    print(len(validation_results))
    print("\nValidation results saved to stg_validation_results.")
    
else:
    
    validation_results = pd.DataFrame()
    
    print("No validation errors found.")
    
con.close()