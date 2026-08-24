SELECT
    Unique_Referral_ID,
    '113A' AS RuleCode,
    'NULL_GP_Notified_of_Referral_Receipt' AS RuleDescription
FROM stg_referrals
WHERE GP_notified_of_referral_receipt IS NULL
