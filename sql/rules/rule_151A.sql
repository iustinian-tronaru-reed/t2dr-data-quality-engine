SELECT
    Unique_Referral_ID,
    '151A' AS RuleCode,
    'Weight_Not_Between_35_And_300' AS RuleDescription,
    'Contacts' AS DatasetName
FROM stg_contacts
WHERE Weight IS NOT NULL
  AND CAST(Weight AS REAL) NOT BETWEEN 35 AND 300
  AND CAST(Weight AS TEXT) NOT LIKE '%999%';
