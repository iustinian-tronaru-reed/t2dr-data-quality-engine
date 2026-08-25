CREATE TABLE IF NOT EXISTS FactError
(
    ErrorKey INTEGER PRIMARY KEY AUTOINCREMENT,
    RuleKey INTEGER,
    DatasetKey INTEGER,
    DateKey INTEGER,
    ReferralKey INTEGER,
    ProgrammeKey INTEGER,
    ErrorCount INTEGER DEFAULT 1,

    FOREIGN KEY (RuleKey)
        REFERENCES DimRule(RuleKey),

    FOREIGN KEY (DatasetKey)
        REFERENCES DimDataset(DatasetKey),

    FOREIGN KEY (DateKey)
        REFERENCES DimDate(DateKey),

    FOREIGN KEY (ReferralKey)
        REFERENCES DimReferral(ReferralKey),

    FOREIGN KEY (ProgrammeKey)
        REFERENCES DimProgramme(ProgrammeKey)
);
