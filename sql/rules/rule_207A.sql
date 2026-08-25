SELECT
    Unique_Referral_ID,
    '207A' AS RuleCode,
    'NULL_Date_of_Session_or_Engagement' AS RuleDescription
FROM stg_health_incidents
WHERE TRIM(
    COALESCE(Date_of_Session_or_Engagement, '')
) = '';
