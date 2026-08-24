# Source to Target Mapping

## Source Systems

### Referrals

Source File:
referrals.csv

Target Table:
stg_referrals

Primary Key:
Unique_Referral_ID


### Contacts

Source File:
contacts.csv

Target Table:
stg_contacts

Primary Key:
Unique_Referral_ID + Session_Date


### Health Incidents

Source File:
health_incidents.csv

Target Table:
stg_health_incidents

Primary Key:
Unique_Referral_ID + Incident_Date
