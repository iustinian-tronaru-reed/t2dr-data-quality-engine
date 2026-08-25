import subprocess
import sys


pipeline_steps = [
    "src/build_database.py",
    "src/create_warehouse.py",
    "src/load_dimensions.py",
    "src/run_validations.py",
    "src/load_fact_errors.py"
]


print("Starting T2DR data quality pipeline.")


for step in pipeline_steps:

    print()
    print(f"Running {step}")

    subprocess.run(
        [sys.executable, step],
        check=True
    )


print()
print("Pipeline completed successfully.")
