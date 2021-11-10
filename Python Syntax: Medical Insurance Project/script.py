# create the initial variables below
age = 28
sex = 0 # 0 for female, 1 for male
bmi = 26.2 # body mass index
num_of_children = 3
smoker = 0 # 0 for a non-smoker, 1 for a smoker

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("This person's insurance cost is", insurance_cost, "dollars.")
# Age Factor
age += 4

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in cost of insurance after increasing the age by 4 years is", change_in_insurance_cost, "dollars.")
# BMI Factor
age = 28 # original value
bmi += 3.1

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated insurance cost after increasing BMI by 3.1 is",change_in_insurance_cost,"dollars.")

# Male vs. Female Factor
bmi = 26.2 # original value
sex = 1 # male

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being male instead of female is", change_in_insurance_cost,"dollars.")

# num_of_children factor
sex = 0 # original value
num_of_children += 2

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated of insurance cost after increasing number of children by 2", change_in_insurance_cost,"dollars.")

# smoker factor
num_of_children = 3 # original value
smoker = 1 # smoker

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print("The change in estimated cost for being smoker instead of non-smoker is", change_in_insurance_cost,"dollars.")

