# 2D Lists, negative indicies

class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]

print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

# Modifying 2D Lists

incoming_class = [["Kenny", "American", 9], ["Tanya", "Ukrainian", 9], ["Madison", "Indian", 7]]
print(incoming_class)

incoming_class[2][2] = 8
print(incoming_class)

incoming_class[-3][-3] = "Ken"
print(incoming_class)

# Another example

first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)
customer_data = [["Ainsley", "Small", True], ["Ben", "Large", False], ["Chani", "Medium", True], ["Depak", "Medium", False]]
print(customer_data)
customer_data[2][2] = False
customer_data[1].remove(False)
new_customers = [["Amit", "Large", True], ["Karim", "X-Large", False]]
customer_data_final = customer_data + new_customers
print(customer_data_final)

# Consectutive lists: range

number_list = range(9)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))

# Slicing lists

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

print(beginning)

middle = suitcase[2:4]
print(middle)

# Slicing 2:

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 

last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

# .count method:

votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)
# This prints the amount of times Jake appears in the list.

# Sorting lists with reverse

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)

addresses.sort()
print(addresses)

print(sorted_cities)

# Sorting lists with sorted

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

games_sorted = sorted(games)
print(games)
print(games_sorted)

# Remove 5th element in list with pop:

removed_item = list.pop(4)

# Use pop to remove last item in list. Eg:

pizza_and_prices.pop()

# zip()
# The zip() function allows us to quickly combine associated data-sets without needing to rely on multi-dimensional lists. While zip() can work with many different scenarios, we are going to explore only a single one in this article.

#Use zip() to create a new variable called names_and_dogs_names that combines owners and dogs_names lists into a zip object.
#Then, create a new variable named list_of_names_and_dogs_names by calling the list() function on names_and_dogs_names.
#Print list_of_names_and_dogs_names.

owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]

names_and_dogs_names = zip(owners, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)