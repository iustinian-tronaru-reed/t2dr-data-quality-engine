import sqlite3
from pathlib import Path


database_path = Path("database/t2dr.db")
dml_path = Path("sql/warehouse/load_dimensions.sql")


con = sqlite3.connect(database_path)

con.execute("PRAGMA foreign_keys = ON")


with open(dml_path, "r") as file:
    sql = file.read()


con.executescript(sql)

con.commit()


dimension_tables = [
    "DimRule",
    "DimDataset",
    "DimDate",
    "DimReferral",
    "DimProgramme"
]


for table in dimension_tables:

    result = con.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()

    print(f"{table}: {result[0]}")


con.close()

print("Dimensions loaded.")
