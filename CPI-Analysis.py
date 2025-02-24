# Importing pandas library into code
import pandas as pd

#List of province file names
file_names = [
    "Canada.CPI.1810000401.csv",
    "ON.CPI.1810000401.csv",
    "QC.CPI.1810000401.csv",
    "BC.CPI.1810000401.csv",
    "AB.CPI.1810000401.csv",
    "MB.CPI.1810000401.csv",
    "SK.CPI.1810000401.csv",
    "NS.CPI.1810000401.csv",
    "NB.CPI.1810000401.csv",
    "NL.CPI.1810000401.csv",
    "PEI.CPI.1810000401.csv"
]

# Empty list to store all dataframes
dfs = []

# Read each file into a dataframe and store it in the list
for file in file_names:
    df = pd.read_csv(file)   # Load the data from each csv file and store in a dataframe
    jurisdiction = file.split(".")[0]  # Extract the jurisdiction only from the file name
    df["Jurisdiction"] = jurisdiction # add a new column in the dataframe for jurisdiction    
    dfs.append(df) # append the dfs list with the updated dataframe

# Combine all data into a single DataFrame, ensuring indexes are sequential
combined_df = pd.concat(dfs, ignore_index=True)

# QUESTION 1: Adjust the headings/melt the combined dataframe
combined_df = combined_df.melt(id_vars=["Item", "Jurisdiction"], 
                               var_name="Month", 
                               value_name="CPI")

# Output the melted dataframe to a test csv file to ensure the new dataframe was combined and transformed successfully
combined_df.to_csv('output.csv')

# QUESTION 2: print first 12 lines of the new data frame
print(combined_df.head(12))

# QUESTION 3: Report average month-to-month change in food, shelter, and all-items excl. food and energy
# for Canada and each of the provinces up to 1 decimal place
def calculate_monthly_changes(df):

    categories = ['Food', 'Shelter', 'All-items excluding food and energy'] # Create list of required categories
    results = {} # Create empty dictionary to store results for each jurisdiction

    # Loop through every unique jurisdiction filtering the DataFrame to include only rows for that jurisdiction
    for jur in df['Jurisdiction'].unique():
        jur_df = df[df['Jurisdiction'] == jur] 
        jur_results = {}

        #loop through every required category within the current jurisdiction
        for cat in categories:
            cat_df = jur_df[jur_df['Item'] == cat] # filter jur_df to include only the rows where the 'Item' column matches the current category
            changes = cat_df['CPI'].pct_change() * 100 #calculate the % change between consecutive rows in the 'CPI' column for the current category
            jur_results[cat] = round(changes.mean(), 1) # Calculate avg monthly % change for the current category
        results[jur] = jur_results # Add the category results for the current jurisdiction to the results dictionary
    return results

monthly_changes = calculate_monthly_changes(combined_df)  # Calculate monthly CPI changes
print("\nQuestion 3: Average month-to-month % changes")

# Print Question 3 results: jurisdiction and category percentage changes
for jur, changes in monthly_changes.items(): #Loop through each jur and its associated category results (changes) in the monthly_changes dictionary
    print(f"{jur}:")  # Print current jurisdiction name

    for cat, val in changes.items():  
        print(f"  {cat}: {val}%")  #Print the category and its associated average monthly change


# Question 4: What province experienced the highest average change in the above categories?
def find_highest_changes(changes_dict):
    max_changes = {}

    #Loop through every required category to report
    for cat in ['Food', 'Shelter', 'All-items excluding food and energy']:
        max_jur = max(changes_dict.items(), key=lambda x: x[1][cat])[0]  # Find the jur with the highest avg % change for the current category
        max_val = changes_dict[max_jur][cat] # Retrieve highest average % change value for the current category in the jurisdiction
        max_changes[cat] = (max_jur, max_val)  # Store the jurisdiction and value of the highest change for the current category in the results dictionary
    return max_changes

highest_changes = find_highest_changes(monthly_changes) # Call the function to get the highest changes and store the result
print("\nQuestion 4: Highest average changes") 
for cat, (jur, val) in highest_changes.items(): 
    print(f"{cat}: {jur} ({val}%)")  # Print the category, jurisdiction, and the percentage of the highest change

# Question 5: Compute the annual change in CPI for services across Canada and all provinces
def calculate_annual_service_change(df):
    services_df = df[df['Item'] == 'Services'] # Filter the dataframe to include only rows for 'Services'
    results = {}
    
    # Loop through every unique jurisdiction filtering the DataFrame to include only rows for that jurisdiction
    for jur in services_df['Jurisdiction'].unique(): 
        jur_df = services_df[services_df['Jurisdiction'] == jur] # Filter the dataframe to include only rows for the current jurisdiction
        jan_val = jur_df[jur_df['Month'] == '24-Jan']['CPI'].iloc[0] # Get CPI value for January in the current jurisdiction
        dec_val = jur_df[jur_df['Month'] == '24-Dec']['CPI'].iloc[0] # Get CPI value for December in the current jurisdiction
        annual_change = ((dec_val - jan_val) / jan_val) * 100  # Calculate the annual % change from January to December
        results[jur] = round(annual_change, 1) # Store the annual change for the current jurisdiction
    
    return results

annual_services = calculate_annual_service_change(combined_df) # Calculate and store annual CPI changes for 'Services' across all jurisdictions
print("\nQuestion 5: Annual % change in Services")
for jur, change in annual_services.items(): # Print each jurisdiction's annual change
    print(f"{jur}: {change}%")

# Question 6: What region experienced the highest inflation in services?
max_services_jur = max(annual_services.items(), key=lambda x: x[1])[0] # Find jurisdiction with highest CPI change
max_services_val = annual_services[max_services_jur] # Get highest change value for that jurisdiction
print(f"\nQuestion 6: Highest inflation in services") # Output results
print(f"{max_services_jur}: {max_services_val}%")