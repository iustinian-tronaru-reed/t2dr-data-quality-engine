import pandas as pd

def load_data():
    
    referrals = pd.read_csv("data/referrals.csv")
    contacts = pd.read_csv("data/contacts.csv")
    health_incidents = pd.read_csv("data/health_incidents.csv")
    
    return(referrals, contacts, health_incidents)
