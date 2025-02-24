# FINE3300-CPI-Analysis

This repository contains my code for Assignment 2 in FINE 3300. This program processes and analyzes Consumer Price Index (CPI) data for Canada and its provinces obtained from multiple CSV files. It performs data transformation and provides insight into the monthly and annual CPI changes across various categories and jurisdictions in Canada.

## Program Description

The script reads CPI data from CSV files (e.g., `ON.CPI.1810000401.csv`), combines them into a single DataFrame, and transforms the data for analysis. It answers 6 specific questions:

1. Combine the 11 data frames into one data frame with column headings: Item, Month, Jurisdiction,
CPI.
2. Print the first 12 lines of your new data frame
3. For Canada and each of the provinces, report the average month-to-month change in food, shelter,
All-items excluding food and energy. Report your numbers as a percent up to one decimal place.
4. Which province experienced the highest average change in the above categories?
5. Compute the annual change in CPI for services across Canada and all provinces. Report your numbers
as a percent up to one decimal place.
6. Which region experienced the highest inflation in services?

## Inputs

- **CSV Files**: CPI data files for Canada and 10 provinces:
  - `Canada.CPI.1810000401.csv`
  - `ON.CPI.1810000401.csv` (Ontario)
  - `QC.CPI.1810000401.csv` (Quebec)
  - `BC.CPI.1810000401.csv` (British Columbia)
  - `AB.CPI.1810000401.csv` (Alberta)
  - `MB.CPI.1810000401.csv` (Manitoba)
  - `SK.CPI.1810000401.csv` (Saskatchewan)
  - `NS.CPI.1810000401.csv` (Nova Scotia)
  - `NB.CPI.1810000401.csv` (New Brunswick)
  - `NL.CPI.1810000401.csv` (Newfoundland and Labrador)
  - `PEI.CPI.1810000401.csv` (Prince Edward Island)

Each file contains CPI data with an 'Item' column (e.g., Food, Shelter, Services) and monthly CPI values.

## Outputs

- **Console Output**: Results for the questions, including DataFrame previews, percentage changes, and highest change identifications.
- **CSV File**: `output.csv` containing the combined and melted DataFrame