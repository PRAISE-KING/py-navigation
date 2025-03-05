
# Defined using curly brackets - {}
# stores info that come as key value pairs e.g name : john .......name is the key while john is the value

customer = {
    "name" : "praizking",
    "age" : 40,
    "verified" : True
}

# to update a value or add a key and value
customer["age"] = 35
print(customer.get("age"))

# adds a key and value
customer['Birth_date'] = '8 feb 2002'
print(customer)

# can also be printed as
print(customer["age"])

# incase the key word is not in the dictionary using the get() method will give it as none eg
print(customer.get("birthdate"))

# instead of none we can choose a default response value to get e.g in this case we'll get "not there" as the response
print(customer.get('birth_time ' , 'not there'))



# print a code that takes a phone no. and translates into words

phone = input('Phone > ')

wording = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

output = " "

for num in phone:
    output += wording.get(num , " ! ") + " "
print(output)
# output is set to blank space but after itteration the output adds the phone number but gets the value of the number in the dictionary to words
# ! mark is used to show the emptyness of the number in the dictionary


# marks and remarks for every grade

marks = int(input( "marks : "))

if marks >= 80:
    grade = 'A'
elif marks >=75:
    grade = "A-"
elif marks >= 70:
    grade = "B+"
elif marks >= 65:
    grade = "B"
elif marks >= 60:
    grade = "B-"
elif marks >= 55:
    grade = "C+"
elif marks >= 50:
    grade = "C"
elif marks <= 49:
    grade = "Other"

for grades in grade:
    grade_remarks = {
        "A" : "Excellent",
        "A-" : "Greater",
        "B+" : "Great",
        "B" : "Very good",
        "B-" : "good",
        "C+" : "Good trial",
        "C" : "can do better",
        "Other" : "Pull up your socks"
    }
    remarks = " "

    for remark in grade:
        remarks += grade_remarks.get(remark , "empty mark")
print(f'{grade} {remarks}')



# EMOJI CONVERTER
# here we use the split metthod to separate each words from the sentence treating it as single word
# we use word as default to return the other words if no emoji is assigned to them
# the space is added to space the emoji when returned

message = input('> ')
words = message.split(' ')

emoji = {
    ':)': 'smile emoji',
    ':(': 'sad emoji'
}

output = ' '
for word in words:
    output += emoji.get(word, word) + ' '
print(output)

