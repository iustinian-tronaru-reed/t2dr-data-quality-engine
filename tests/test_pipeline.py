import sqlite3
from pathlib import Path

DATABASE_PATH = Path("database/t2dr.db")

def test_required_tables_exist():
    
    con = sqlite3.connect(DATABASE_PATH)
    
    result = con.execute(
        """
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        """
        ).fetchall()
    
    con.close()
    
    existing_tables = {
        row[0]
        for row in result
        }
    
    required_tables = {
        "stg_referrals",
        "stg_contacts",
        "stg_health_incidents",
        "stg_validation_results",
        "DimRule",
        "DimDataset",
        "DimDate",
        "DimReferral",
        "DimProgramme",
        "FactError"
        }
    
    assert required_tables.issubset(existing_tables)
    
def test_validation_results_match_fact_errors():
    
    con = sqlite3.connect(DATABASE_PATH)
    
    validation_count = con.execute(
        """
        SELECT COUNT(*)
        FROM stg_validation_results
        """
        ).fetchone()[0]
    
    fact_count = con.execute(
        """
        SELECT COUNT(*)
        FROM FactError fact
        
        INNER JOIN DimDate date
            ON fact.DateKey = date.DateKey
            
        WHERE date.FullDate = 
        (
            SELECT DISTINCT RunDate
            FROM stg_validation_results
        )
        """
        ).fetchone()[0]
    
    con.close()
    
    assert validation_count == fact_count
    
def test_fact_error_foreign_keys_are_valid():
    
    con = sqlite3.connect(DATABASE_PATH)
    
    unmatched_count = con.execute(
        """
        SELECT COUNT (*)
        FROM FactError fact
        
        LEFT JOIN DimRule rule
            ON fact.RuleKey = rule.RuleKey
            
        LEFT JOIN DimDataset dataset
            ON fact.DatasetKey = dataset.DatasetKey
            
        LEFT JOIN DimDate date
            ON fact.DateKey = date.DateKey
            
        LEFT JOIN DimReferral referral
            ON fact.ReferralKey = referral.ReferralKey
        
        LEFT JOIN DimProgramme programme
            ON fact.ProgrammeKey = programme.ProgrammeKey
            
        WHERE rule.RuleKey IS NULL
            OR dataset.DatasetKey IS NULL
            OR date.DateKey IS NULL
            OR referral.ReferralKey IS NULL
            OR programme.ProgrammeKey IS NULL
        """
        ).fetchone()[0]
    
    con.close()
    
    assert unmatched_count == 0