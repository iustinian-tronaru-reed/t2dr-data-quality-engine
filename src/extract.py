import pandas as pd

referrals = pd.read_csv("data/referrals.csv")
contacts = pd.read_csv("data/contacts.csv")
health_incidents = pd.read_CSV("data/health_incidents.csv")

print("Referrals")
print(referrals.shape)

print("Contacts")
print(contacts.shape)

print("Health Incidents")
print(health_incidents.shape)
