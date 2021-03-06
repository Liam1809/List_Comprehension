# List Comprehensions
# Let’s say we have scraped a certain website and gotten these words:

# words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
# We want to make a new list, called usernames, that has all of the strings in words with an '@' as the first character. We know we can do this with a for loop:

# words = ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]
# usernames = []

# for word in words:
#   if word[0] == '@':
#     usernames.append(word)
# First, we created a new empty list, usernames, and as we looped through the words list, we added every word that matched our criterion. Now, the usernames list looks like this:

# >>> print(usernames)
# ["@coolguy35", "@kewldawg54", "@matchamom"]
# Python has a convenient shorthand to create lists like this with one line:

# usernames = [word for word in words if word[0] == '@']
# This is called a list comprehension. It will produce the same output as the for loop did:

# ["@coolguy35", "@kewldawg54", "@matchamom"]
# This list comprehension:

# Takes an element in words
# Assigns that element to a variable called word
# Checks if word[0] == '@', and if so, it adds word to the new list, usernames. If not, nothing happens.
# Repeats steps 1-3 for all of the strings in words
# Note: if we hadn’t done any checking (let’s say we had omitted if word[0] == '@'), the new list would be just a copy of words:

# usernames = [word for word in words]
# #usernames is now ["@coolguy35", "#nofilter", "@kewldawg54", "reply", "timestamp", "@matchamom", "follow", "#updog"]

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

# Let’s say we’re working with the usernames list from the last exercise:

# >>> print(usernames)
# ["@coolguy35", "@kewldawg54", "@matchamom"]
# We want to create a new list with the string " please follow me!" added to the end of each username. We want to call this new list messages. We can use a list comprehension to make this list with one line:

# messages = [user + " please follow me!" for user in usernames]
# This list comprehension:

# Takes a string in usernames
# Assigns that string to a variable called user
# Adds “ please follow me!” to user
# Appends that concatenation to the new list called messages
# Repeats steps 1-4 for all of the strings in usernames
# Now, messages contains these values:

# ["@coolguy35 please follow me!", "@kewldawg54 please follow me!", "@matchamom please follow me!"]
# Being able to create lists with modified values is especially useful when working with numbers. Let’s say we have this list:

# my_upvotes = [192, 34, 22, 175, 75, 101, 97]
# We want to add 100 to each value. We can accomplish this goal in one line:

# updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]
# This list comprehension:

# Takes a number in my_upvotes
# Assigns that number to a variable called vote_value
# Adds 100 to vote_value
# Appends that sum to the new list updated_upvotes
# Repeats steps 1-4 for all of the numbers in my_upvotes
# Now, updated_upvotes contains these values:

# [292, 134, 122, 275, 175, 201, 197]

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [round(temperature_in_celsius * 9/5 + 32,1) for temperature_in_celsius in celsius]
print(fahrenheit)

single_digits = range(10)
squares = []
for digit in single_digits:
  squares.append(digit**2)
  print(digit)
print(squares)
cubes = [digit**3 for digit in single_digits]
print(cubes)

# nested list comprehension
#Write your function here
def exponents(bases, powers):
  empty_list = [(base ** power)for base in bases for power in powers]
  return empty_list

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

#  another way is [x for x in [y for y in data]]

# iterate over a list backward
# for i in range(len(list)-1, -1, -1):
# for i in list[::-1]:
