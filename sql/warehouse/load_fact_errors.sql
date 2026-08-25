DELETE FROM FactError

WHERE DateKey IN
(
    SELECT DISTINCT
        dim_date.DateKey

    FROM DimDate dim_date

    INNER JOIN stg_validation_results results
        ON dim_date.FullDate = results.RunDate
);

INSERT INTO FactError
(
    RuleKey,
    DatasetKey,
    DateKey,
    ReferralKey,
    ProgrammeKey,
    ErrorCount
)

SELECT
    dim_rule.RuleKey,
    dim_dataset.Datasetkey,
    dim_date.DateKey,
    dim_referral.ReferralKey,
    dim_programme.ProgrammeKey,
    1

FROM stg_validation_results results

INNER JOIN DimRule dim_rule
    ON results.RuleCode = dim_rule.RuleCode

INNER JOIN DimDataset dim_dataset
    ON results.DatasetName = dim_dataset.DatasetName

INNER JOIN DimDate dim_date
    ON results.RunDate = dim_date.FullDate

INNER JOIN DimReferral dim_referral
    ON results.Unique_Referral_ID = dim_referral.ReferralID

INNER JOIN DimProgramme dim_programme
    ON results.ProgrammeName = dim_programme.ProgrammeName;
