food_items = ["celery", "carrots", "spinach", "potatoes", "tomatoes", "milk"]

print([(x,y) for x in range(10) for y in range(10) if x%2 == 0 and y%2 == 0])