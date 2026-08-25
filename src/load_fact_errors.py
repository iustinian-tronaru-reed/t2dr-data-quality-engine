import sqlite3
from pathlib import Path


database_path = Path("database/t2dr.db")

dml_path = Path(
    "sql/warehouse/load_fact_errors.sql"
)


con = sqlite3.connect(database_path)

con.execute("PRAGMA foreign_keys = ON")


with open(dml_path, "r") as file:
    sql = file.read()


con.executescript(sql)

con.commit()


fact_count = con.execute(
    "SELECT COUNT(*) FROM FactError"
).fetchone()[0]


print(f"FactError rows: {fact_count}")


con.close()

print("FactError loaded.")
