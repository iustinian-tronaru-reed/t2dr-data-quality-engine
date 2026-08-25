# Warehouse Design

## Overview

The database contains 2 layers:

1. A staging layer where source data is loaded from CSVs
2. A dimensional model layer containing validation errors and descriptive dimensions 

## Staging Tables

stg_referrals

stg_contacts

stg_health_incidents

## Dimensional Model

### FactError

ErrorKey	| Primary Key
RuleKey		| Foreign Key
DatasetKey	| Foreign Key
DateKey		| Foreign Key
ReferralKey	| Foreign Key
ProgrammeKey	| Foreign Key
ErrorCount	| Measure

Grain: 1 row = 1 validation error per record per validation run

### DimRule

RuleKey | Primary Key
RuleCode
RuleDescription

### DimDataset

DatasetKey | Primary Key
DatasetName

### DimDate

DateKey | Primary Key
FullDate
MonthName
MonthNumber
YearNumber

### DimReferral

ReferralKey | Primary Key
ReferralID
ReferralDate

### DimProgramme

ProgrammeKey | Primary Key
ProgrammeName
