# Week 1.2, Session 1: Task 4

fruit = {"apple", "orange", "tomato"}
vegetable = {"leek", "tomato", "potato"}

# What do you think will be printed here?

both = fruit.intersection(vegetable)
print(both)
#just tomato, as it is the only element common to both sets

# Why does the following code diplay five items?

food = fruit.union(vegetable)
print(food)
#tomato appears twice, so is not repeated. All other elements present are shown

# Add an item to fruit
fruit.add('banana')
print(fruit)

# Remove an item from vegetables
vegetable.discard('leek')
print(vegetable)
# Find and display symmetric difference of the two sets

print(fruit.symmetric_difference(vegetable))