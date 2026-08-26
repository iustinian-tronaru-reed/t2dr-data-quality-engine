# T2DR Data Quality Engineering

## Overview

This project is a simplified recreation of a data-quality validation process used for T2DR error reporting.

It loads the three T2DR MDS datasets in CSV format into SQLite, redacted to not include personal or customer identification information.
It executes SQL validation rules and stores the resulting errors in a dimensional model.

## Pipeline

1. Extract source CSV data with Python and Pandas
2. Load data into SQLite staging tables
3. Create dimensional warehouse tables using SQL DDL
4. Populate dimensions using SQL DML
5. Execute validation rules stored as separate SQL files
6. Combine the validation results
7. Load the results into FactError

## Dimensional Model

The central fact table is FactError.
The grain is 1 validation error per record per validation run.

Dimenstions:

- DimRule
- DimDataset
- DimDate
- DimReferral
- DimProgramme

## Running the Pipeline

From the repository root:

	python src/run_pipeline.py

Individual stages can also be run separately:

	python src/build_database.py
	python src/create_warehouse.py
	python src/load_dimensions.py
	python src/run_validations.py
	python src/load_fact_errors.py

## Testing

Three test embbeded in a test_ file, run: python -m pytest -v

Test 1: all required tables exist
Test 2: staging rows match fact rows
Test 3: every foreign key points to a valid dim record
