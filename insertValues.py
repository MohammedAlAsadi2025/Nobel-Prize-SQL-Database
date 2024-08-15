import pandas as pd

# Function to generate INSERT statements for Prize table
def generate_prize_statements(data):
    statements = []
    for _, row in data.iterrows():
        statement = "INSERT INTO Prize (Id, prizeName, description, amountAwarded, dateAwarded) VALUES ('{}', '{}', '{}', {}, '{}');".format(row[12], row[2], row[9], row[5], row[7])
        statements.append(statement)
    return statements

# Function to generate INSERT statements for Laureate table
def generate_laureate_statements(data):
    ids = data[12].unique()
    statements = ["INSERT INTO Laureate (Id) VALUES ('{}');".format(id_) for id_ in ids]
    return statements

# Function to generate INSERT statements for Organisation table
def generate_organisation_statements(data):
    statements = []
    for _, row in data.iterrows():
        statement = "INSERT INTO Organisation (Id, orgName, orgCountry, dateFounded) VALUES ('{}', '{}', '{}', '{}');".format(row[12], row[36], row[41], row[38])
        statements.append(statement)
    return statements

# Function to generate INSERT statements for Individual table
def generate_individual_statements(data):
    statements = []
    for _, row in data.iterrows():
        statement = "INSERT INTO Individual (Id, firstName, lastName, gender, birthDate) VALUES ('{}', '{}', '{}', '{}', '{}');".format(row[12], row[15], row[16], row[19], row[21])
        statements.append(statement)
    return statements

# Function to generate INSERT statements for Country table
def generate_country_statements(data):
    statements = []
    for _, row in data.iterrows():
        statement = "INSERT INTO Country (Id, birthCountry, deathCountry) VALUES ('{}', '{}', '{}');".format(row[12], row[25], row[32])
        statements.append(statement)
    return statements

# Load the CSV file without headers
data = pd.read_csv("complete.csv", header=None)
# Filter data for only organizations and individuals
org_data = data[data[45] == "Organization"].head(50)
ind_data = data[data[45] == "Individual"].head(150)

# Generate all INSERT statements
all_statements = (generate_prize_statements(org_data) +
                  generate_laureate_statements(org_data) +
                  generate_organisation_statements(org_data) +
                  generate_prize_statements(ind_data) +
                  generate_laureate_statements(ind_data) +
                  generate_individual_statements(ind_data) +
                  generate_country_statements(ind_data))

# Save the statements to a file
with open("insert_statements.sql", "w") as f:
    for stmt in all_statements:
        f.write(stmt + "\n")

print("SQL statements saved to insert_statements.sql")
