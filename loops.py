# for loop

# for <temporary variable> in <collection>:
# <action>

#A for keyword indicates the start of a for loop.
#A <temporary variable> that is used to represent the value of the element in the collection the loop is currently on.
#An in keyword separates the temporary variable from the collection used for iteration.
#A <collection> to loop over. In our examples, we will be using a list.
#An <action> to do anything on each iteration of the loop.

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
 
for ingredient in ingredients:
  print(ingredient)
  
# In this example:
# ingredient is the <temporary variable>.
# ingredients is our <collection>.
# print(ingredient) was the <action> performed on every iteration using the temporary variable of ingredient.

# Some things to note about for loops:
# Temporary Variables:
# A temporary variable’s name is arbitrary and does not need to be defined beforehand. Both of the following code snippets do the exact same thing as our above example:

for i in ingredients:
  print(i)
  
for item in ingredients:
 print(item)
 
# Programming best practices suggest we make our temporary variables as descriptive as possible. 
# Since each iteration (step) of our loop is accessing an ingredient it makes more sense to call our temporary variable ingredient rather than i or item.

# using range in loops
# Use the range() function in a for loop to print() out the provided promise variable five times.
promise = "I will finish the python loops module!"

for temp in range(5):
  print(promise)
  
# While loops

count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1
  
# count is initialised with value of 0. The conditional statement is count being less than or equal to 3, which is true at the initial interation of the loop, so the loop body executes.
# When this first iteration is finished, Python returns to the top of the loop and checks the conditional again. As count is now equal to 1, the conditional is still true, so the loop executes again.
# This continues until the count variable becomes 4, at which point the conditional is no longer true, so the loop stops.

# Elegant loop:

count = 0
while count <= 3: print(count); count += 1

# Let’s write a while loop that counts down from 10 to 0(inclusive). Once our loop is finished we will commemorate our accomplishment by printing "We have liftoff!".

countdown = 10
print("Starting while loop")
while countdown >= 0:
  print(countdown)
  countdown -= 1
print("We have liftoff!")

# While loops: lists

# We are going to write a while loop to iterate over the provided list python_topics.

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0
while index < length:
  print("I am learning about", python_topics[index])
  index += 1
  
# Loop control: break

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

# Due to the break statement, the loop will stop iterating over the list once the dog_breed that matches the dog_breed_I_want.

# Loop control: continue

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
  if i <= 0:
    continue
  print(i)

# continue checks that the if statement is true for the current element, then continues the loop if so. This code will print all the positive ints.

# Nested loops

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  for element in location:
    scoops_sold += element
print(scoops_sold)

# This code will first loop through the sales_data list, then will loop through each element in the list and add the element values to the scoops sold variable.

# List comprehensions. Advantage of Python is ability to write simple, clean code. List comprehensions allow you to solve a problem using a for loop on one line, like this:

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [num + 10 for num in grades]
print(scaled_grades)

# This will add 10 to each of the numbers in the grades list.
# Comprehensions can incorporate conditional logic. If we wanted to only double negative numbers in a list, this comprehension code would do it simply:

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

# This creates a new list of every height that is over 161:

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

# Comprehensions review

# Your code below:
# Create a list called single_digits that consists of the numbers 0-9 (inclusive).
single_digits = range(10)

# Before the loop, create a list called squares. Assign it to be an empty list to begin with.
squares = []

# Create a for loop that goes through single_digits and prints out each one.
for digit in single_digits:
    # Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.
  squares.append(digit * digit)
  print(digit)
print(squares)
# Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.
cubes = [third * third * third for third in single_digits]
print(cubes)