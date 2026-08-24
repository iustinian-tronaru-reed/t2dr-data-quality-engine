import sqlite3
from extract import load_data

con = sqlite3.connect("database/t2dr.db")
cur = con.cursor()

referrals, contacts, health_incidents = load_data()

referrals.to_sql(
    "stg_referrals",
    con,
    if_exists="replace",
    index=False
)

contacts.to_sql(
    "stg_contacts",
    con,
    if_exists="replace",
    index=False
)

health_incidents.to_sql(
    "stg_health_incidents",
    con,
    if_exists="replace",
    index=False
)

result_referrals = cur.execute("SELECT COUNT(*) FROM stg_referrals").fetchone()
result_contacts = cur.execute("SELECT COUNT(*) FROM stg_contacts").fetchone()
result_health_incidents = cur.execute("SELECT COUNT(*) FROM stg_health_incidents").fetchone()

print("Referrals")
print(result_referrals[0])

print("Contacts")
print(result_contacts[0])

print("Health Incidents")
print(result_health_incidents[0])

con.commit()
con.close()
