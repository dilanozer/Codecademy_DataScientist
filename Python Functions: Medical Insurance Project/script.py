# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  output_message = "The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars."
  return output_message,estimated_cost

# calculate between two insurance cost function
def diff_insurance_cost(first_cost, second_cost):
  difference = first_cost - second_cost
  return "The difference in insurance cost is " + str(difference) + " dollars."

print(diff_insurance_cost(5469.0, 687.0))
# Estimate Maria's insurance cost
maria_insurance_cost = calculate_insurance_cost(name = "Maria", age = 28, sex = 0,bmi = 26.2, num_of_children = 3, smoker = 0)
print(maria_insurance_cost)
# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(name = "Omar", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)
print(omar_insurance_cost)
# Estimate Dilan's insurance cost
dilan_insurance_cost = calculate_insurance_cost(name = "Dilan", age = 23, sex = 0, bmi = 20.1, num_of_children = 0, smoker = 0)
print(dilan_insurance_cost)
