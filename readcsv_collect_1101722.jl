using CSV
using DataFrames
using PrettyTables

# Load your data
file_path = "C:\\Users\\USER\\Desktop\\Marchine Learning\\readcsv_collect\\data_with_classes.csv"
df = CSV.read(file_path, DataFrame)

# Initial matrices to hold data for each class
# Start with empty arrays
global matclass1 = []
global matclass2 = []
global matclass3 = []

# Initialize through each row of the DataFrame
for row in eachrow(df)
    global matclass1, matclass2, matclass3
    # print(row)
    # Extract data as an array, excluding the Class column
    data = Matrix(DataFrame(row[1:5]))
    temp = []
    for i in 1:(length(data))
        push!(temp, row[i])
    end
    temp = convert(Vector{Float64}, temp)
    # print(temp)
    if row[6] == 1
        push!(matclass1, temp)
    elseif row[6] == 2
        push!(matclass2, temp)
    elseif row[6] == 3
        push!(matclass3, temp)
    end
end

print("matclass1 : ", matclass1)
println()
print("matclass2 : ", matclass2)
println()
print("matclass3 : ", matclass2)