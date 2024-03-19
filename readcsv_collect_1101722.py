import pandas as pd

# Load your data
file_path = "C:\\Users\\USER\\Desktop\\Marchine Learning\\readcsv_collect\\data_with_classes.csv"
df = pd.read_csv(file_path)

# Initial lists to hold data for each class
matclass1 = []
matclass2 = []
matclass3 = []

# Initialize through each row of the DataFrame
for index, row in df.iterrows():
    temp = []
    # Extract data as an array, excluding the Class column
    data = row.iloc[:5].values
    for value in data:
        temp.append(value)
    temp = list(map(float, temp))
    if row['Class'] == 1:
        matclass1.append(temp)
    elif row['Class'] == 2:
        matclass2.append(temp)
    elif row['Class'] == 3:
        matclass3.append(temp)

print("matclass1 : ", matclass1)
print()
print("matclass2 : ", matclass2)
print()
print("matclass3 : ", matclass2)