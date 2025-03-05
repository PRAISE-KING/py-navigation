 # AND - both arguments should be true
 # OR - atleast one to be true
 # NOT - gives the opposite of the argument.....if true will give it as false and vice vursa



                     # .........exercise 1.........
# write a program that if an applicant has high income (OR,AND,NOT) good credit and doesnt have a criminal record then is eligible for a loan
# the applicant must have at least high income or good record but must not have a criminal record
# but if has criminal record then must have good credit and high income

# ..................................AND.....................................
high_income = False
good_credit = False
has_criminal_record = False

name = input('Your name please: ')

if high_income and good_credit and not has_criminal_record:
    print(f'Hello {name} you are eligible for our loan 1')

# .................................OR................................

elif high_income or good_credit and not has_criminal_record:
    print(f'Hello {name} you are eligible for our loan 2')

# because has criminal record is set as false then the not operator gives it as true which makes him elligible for the loan
elif good_credit and high_income or not has_criminal_record:
    print(f'Hello {name} you are eligible for our loan 3')

else:
    print(f'Sorry {name} you are not eligible for any loan')