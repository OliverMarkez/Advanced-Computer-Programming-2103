name = input ("Enter your Father's name: ")
birthplace = input ("Enter birthplace: ")
import datetime

birth_date = int(input("Enter birthdate (DD): "))
birth_month = int(input("Enter birthmonth (MM): "))
birth_year = int(input("Enter birthyear (YYYY): "))

today = datetime.date.today()
age = today.year - birth_year - ((today.month, today.day) < (birth_month, birth_date))

print ("He is", age, "years old.") 

english = float(input("Enter grades for English: "))
filipino = float(input("Enter grades for Filipino: "))
science = float(input("Enter grades for Science: "))
math = float(input("Enter grades for Math: "))
araling_panlipunan = float(input("Enter grades for Araling Panlipunan: "))
physical_education = float(input("Enter grades for Physical Education: "))

num_grades = 6
sum_grades = english + filipino + science + math+ araling_panlipunan + physical_education
avg_grade = sum_grades / num_grades

print ("The average grade is:", avg_grade) 