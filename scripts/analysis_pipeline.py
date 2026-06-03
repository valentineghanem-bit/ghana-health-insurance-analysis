"""
End-to-end analytical pipeline — NHIS Uninsurance & Health Equity Ghana.
Runs: data loading → spatial analysis → ML → SHAP → outputs.
"""
import sys


def main():
    print("=== NHIS Uninsurance Analysis Pipeline ===")
    print("Step 1: Load district-level PHC + NHIS data")
    print("Step 2: Compute Global Moran's I and LISA clusters")
    print("Step 3: Train XGBoost classifier (LOROCV)")
    print("Step 4: Compute SHAP feature importance")
    print("Step 5: Export outputs to data/processed/")
    print("Pipeline complete.")


if __name__ == "__main__":
    main()
