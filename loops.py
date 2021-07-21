food_items = ["celery", "carrots", "spinach", "potatoes", "tomatoes", "milk"]
#printing item in list
for item in food_items:
    print(item)
#printing from a range
for i in range(1,10):
    print(i)
#while loop
i = 1
while i < 10:
    print(i)
    i += 1
#while loop food_items
while i < len(food_items):
    print(food_items[i] + " is a food item in our food_items.")
    i += 1
#infinite loop
i = 0
while True:
    print(i)
    i+1
    #break to stop the loop
    break 
#for loop continue
for item in food_items:
    if item == "potatoes":
      continue
      #pass
    print(item)
#nested loops
for item in food_items:
    for letter in item:
        print(letter)
#list comprehension
numbers = [number for number in range(10)]
print(numbers)
numbers = [number**2 for number in range(10)]
print(numbers)
numbers = [number for number in range(10) if number%2 == 0]
print(numbers)
#nested list comprehension
numbers = [x+y for x in [1,2,3] for y in [4,5,6]]
print(numbers)
numbers = [(x,y) for x in range(10) for y in range(10) if x%2 == 0 and y%2 == 0]
print(numbers)

# list comprehension with condition
list_comprehension = [item for item in food_items if item != "milk"]
print(list_comprehension)





