# This program is to develop a program to manage a coffee machine. It will use different ingredients (milk, water, coffee, and sugar)
# to prepare different kinds of drinks based on user choice. 

# check the algorithm.txt file for full problem discription and proposed algorithm to solve this problem.

# import the time module 

import time

# define 4 variables to hold initial inventories of the ingredients from the user


print("\n")
print("Enter the initial quantities of the various ingredients:")
print("\n")

milk = int(input("Milk in ml: "))
water = int(input("Water in ml: "))
coffee = int(input("Coffee in g: "))
sugar = int(input("Sugar in g: "))

print("\n")

# display the menu of possible drinks that can be prepared

print("Select a drink you would like")
print("\n")

print("1. Espresso 2. Cafe au lait 3. Cafe with sugar 4. Cafe au lait with sugar")
print("\n")

# let the user enter a number to select choice

choice = int(input("Enter a number corresponding to any drink above you will to drink: "))
print("\n")

# display the users choice

# choices = ['Espresso', 'Cafe au lait', 'Cafe with sugar', 'Cafe au lait with sugar']

# print(f"your choice is:{choices[choice-1]}")
# print("\n")

if choice == 1:
  if water >= 50 and coffee >= 20:
    print("We are preparing your Espresso right now.")

    time.sleep(1.5) # delay for 1.5 seconds
    print("\n")

    print("Hurray, here is your Expresso, enjoy 😋")

      # update the ingredient quantities

    water = water - 50
    coffee = coffee - 20

  else:
    print("Preparing Espresso right now is not possible")

elif choice == 2:
  if (water >= 30 and coffee >= 20) and milk >= 100:
    print("We are preparing your cafe au lait right now")

    time.sleep(1.5) # delay for 1.5 seconds
    print("\n")

    print("Hurray, here is your cafe au lait, enjoy 😋")

      # update the ingredient quantities

    water = water - 30
    coffee = coffee - 20
    milk = milk - 100

  else:
    print("Preparing cafe au lait right now is not possible")

elif choice == 3:
  if water >= 50 and coffee >= 20 and sugar >= 10:
    print("We are preparing your cafe with sugar right now.")

    time.sleep(1.5) # delay for 1.5 seconds
    print("\n")

    print("Hurray, here is your cafe with sugar, enjoy 😋")

      # update the ingredient quantities

    water = water - 50
    coffee = coffee - 20
    sugar = sugar - 10

  else:
    print("Preparing cafe with sugar right now is not possible")

elif choice == 4:
  if water >= 50 and coffee >= 20 and milk >= 100 and sugar >= 10:
    print("We are preparing your cafe au lait with sugar right now.")

    time.sleep(1.5) # delay for 1.5 seconds
    print("\n")

    print("Hurray, here is your cafe au lait with sugar, enjoy 😋")

    # update the ingredient quantities

    water = water - 50
    coffee = coffee - 20
    milk = milk - 100
    sugar = sugar - 10

  else:
    print("Preparing cafe au lait with sugar right now is not possible")

else:
  print("Invalid Choice! 😔")


# check if user wants to see the current stocks

print("\n")
print("Will you like to view the current inventories?")
print("\n")

inventory = int(input("Enter 1 for Yes and 2 for No: "))
print("\n")

if inventory == 1:
  print("Current Quantity of ingredients:")
  print("\n")

  print(f"Water: {water}ml")
  print(f"Sugar: {sugar}g")
  print(f"Coffee: {coffee}g")
  print(f"Milk: {milk}ml")

elif inventory == 2:
  print("Ok, Thank you 🙏")

else:
  print("Enter a valid choice (1 or 2)")

