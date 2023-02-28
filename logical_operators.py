
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
else:
    print("Not eligable for loan")


# and
# or
# not
high_income = False
good_credit = True
student = True

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
