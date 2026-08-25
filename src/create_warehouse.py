import sqlite3
from pathlib import Path


database_path = Path("database/t2dr.db")

ddl_files = [
    Path("sql/warehouse/create_dimensions.sql"),
    Path("sql/warehouse/create_fact_error.sql")
]


con = sqlite3.connect(database_path)

con.execute("PRAGMA foreign_keys = ON")


for ddl_file in ddl_files:

    with open(ddl_file, "r") as file:
        sql = file.read()

    con.executescript(sql)

    print(f"Executed {ddl_file.name}")


con.commit()
con.close()

print("Warehouse tables created.")