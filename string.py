
# python always executes code from the first to the last - first code is executed first then the second and so and so on


# ................................................STRING...............................

# for a string of words to appear in multiple lines , we use triple quotes either single or double ('''  ''') or (""" """)

print("""This is the real me
I won't stop till I get what I want

Take care though...""")


print('''
Come home please
It wont stop 
get her a warm hug too...please''')






# ......................... indexing in string ........................

course = 'I LOVE PYTHON PROGRAMMING'
print(course[5])
# the above code prints the letter in index 5

print(course[-2])
# prints the second letter from the end of the string ....in this case it's N......can replace -2 with any number

print(course[0:8])
# will print the letters from index 0 to the 7th index.....it always excludes the last index when printing this way

print(course[0:])
# will print the whole statement

print(course[:9])
# python assumes the first index to be 0....so will print from index 0 to 9

another_course = course[:]
print(another_course)
# [:] - prints the whole string - acts as a copy paste

name = 'praiseking'
print(name[2:-1])
# this will print the characters from index 2 to the last index excluding it hence typing n





# ..........................formatted string....................(f string)...............................

fname = 'praiz'
lname = 'king'

msg = f'{fname} {lname} is a coder'
print(msg)




# ,,,,,,,,,,,,,,,,,,,,string methods...................................
# a method - function that is tied to only some kind of object

courses = 'Python for beginners'
print(len(courses))
# counts the number of characters in the string
# len() is a general purpose function

# ,,,,,,,,,,,,,,methods below are always case sensitive,,,,,,,,,,,,,,,,,,,,,,,,

print(courses.upper())
# changes to uppercase

print(courses.title())
# changes to lower case but capitalising the first letters of each word

print(courses.lower())
# changes letters to lower case

print(courses.find('f'))
print(courses.find('beginners'))
# gives the index of the place where the character is located


print(courses.replace('begginers' , 'absolute begginers'))
print(courses.replace('b' , 'B'))
# replaces the characters with new character


print('for' in courses)
print('For' in courses)
# checks for availability/existance of a given character in astring
# returns a True or False answer
