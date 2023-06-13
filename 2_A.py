#2.SORUMUN A SIKKI :

P_yes = 9/14  # P(buys_computer = "yes")
P_no = 5/14  # P(buys_computer = "no")

P_age_yes = 2/9  # P(age = "genc" | buys_computer = "yes")
P_age_no = 3/5  # P(age = "genc" | buys_computer = "no")

P_income_yes = 4/9  # P(income = "medium" | buys_computer = "yes")
P_income_no = 2/5  # P(income = "medium" | buys_computer = "no")

P_student_yes = 6/9  # P(student = "yes" | buys_computer = "yes")
P_student_no = 1/5  # P(student = "yes" | buys_computer = "no")

P_credit_rating_yes = 6/9  # P(credit_rating = "fair" | buys_computer = "yes")
P_credit_rating_no = 2/5  # P(credit_rating = "fair" | buys_computer = "no")

X_age = "genc"
X_income = "medium"
X_student = "yes"
X_credit_rating = "fair"

P_X_yes = P_age_yes * P_income_yes * P_student_yes * P_credit_rating_yes

P_X_no = P_age_no * P_income_no * P_student_no * P_credit_rating_no

P_X_yes *= P_yes

P_X_no *= P_no

print("P(X|buys_computer = 'yes') * P(buys_computer = 'yes'): ", P_X_yes)
print("P(X|buys_computer = 'no') * P(buys_computer = 'no'): ", P_X_no)

if P_X_yes > P_X_no:
    print("X örneği 'buys_computer = yes' sınıfına aittir.")
else:
    print("X örneği 'buys_computer = no' sınıfına aittir.")
