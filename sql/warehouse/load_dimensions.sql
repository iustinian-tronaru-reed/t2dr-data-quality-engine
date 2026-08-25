INSERT INTO DimRule
(
    RuleCode,
    RuleDescription
)
SELECT
    '113A',
    'NULL_GP_Notified_of_Referral_Receipt'
WHERE NOT EXISTS
(
    SELECT 1
    FROM DimRule
    WHERE RuleCode = '113A'
);


INSERT INTO DimRule
(
    RuleCode,
    RuleDescription
)
SELECT
    '207A',
    'NULL_Date_of_Session_or_Engagement'
WHERE NOT EXISTS
(
    SELECT 1
    FROM DimRule
    WHERE RuleCode = '207A'
);


INSERT INTO DimDataset
(
    DatasetName
)
SELECT 'Referrals'
WHERE NOT EXISTS
(
    SELECT 1
    FROM DimDataset
    WHERE DatasetName = 'Referrals'
);


INSERT INTO DimDataset
(
    DatasetName
)
SELECT 'Contacts'
WHERE NOT EXISTS
(
    SELECT 1
    FROM DimDataset
    WHERE DatasetName = 'Contacts'
);


INSERT INTO DimDataset
(
    DatasetName
)
SELECT 'Health Incidents'
WHERE NOT EXISTS
(
    SELECT 1
    FROM DimDataset
    WHERE DatasetName = 'Health Incidents'
);


INSERT INTO DimProgramme
(
    ProgrammeName
)
SELECT 'T2DR - Stoke and Staffordshire'
WHERE NOT EXISTS
(
    SELECT 1
    FROM DimProgramme
    WHERE ProgrammeName = 'T2DR - Stoke and Staffordshire'
);


INSERT INTO DimReferral
(
    ReferralID,
    ReferralDate
)
SELECT DISTINCT
    stg.Unique_Referral_ID,
    stg.Date_of_Referral
FROM stg_referrals stg
WHERE stg.Unique_Referral_ID IS NOT NULL
  AND NOT EXISTS
  (
      SELECT 1
      FROM DimReferral dim
      WHERE dim.ReferralID = stg.Unique_Referral_ID
  );


INSERT INTO DimDate
(
    DateKey,
    FullDate,
    MonthName,
    MonthNumber,
    YearNumber
)
SELECT
    CAST(STRFTIME('%Y%m%d', 'now', 'localtime') AS INTEGER),
    DATE('now', 'localtime'),
    CASE STRFTIME('%m', 'now', 'localtime')
        WHEN '01' THEN 'January'
        WHEN '02' THEN 'February'
        WHEN '03' THEN 'March'
        WHEN '04' THEN 'April'
        WHEN '05' THEN 'May'
        WHEN '06' THEN 'June'
        WHEN '07' THEN 'July'
        WHEN '08' THEN 'August'
        WHEN '09' THEN 'September'
        WHEN '10' THEN 'October'
        WHEN '11' THEN 'November'
        WHEN '12' THEN 'December'
    END,
    CAST(STRFTIME('%m', 'now', 'localtime') AS INTEGER),
    CAST(STRFTIME('%Y', 'now', 'localtime') AS INTEGER)
WHERE NOT EXISTS
(
    SELECT 1
    FROM DimDate
    WHERE DateKey =
        CAST(STRFTIME('%Y%m%d', 'now', 'localtime') AS INTEGER)
);
