#The Shopping List Maker

#Task 1:Write a function that lets the user add items to a list
#Task 2:Include a function to remove items from the list
#Task 3:Add a function that prints out the entire list in a formatted way

    
def add(grocery_list, items):
                grocery_list.append(items)
                print(grocery_list)
            
        
def remove(grocery_list, items):   
            grocery_list.remove(items)
            print(grocery_list)
            
def print_list(grocery_list):
        for item in grocery_list:
            print(item)
      
            
items = input("Enter your items: ").lower()    
action = input("Are you adding or removing an item? (add/remove) " ).lower()
ask = input("Would you like to continue? (yes/no): ")
grocery_list = []

while ask == "yes":
    if action == "add":          
        add(grocery_list, items)
    elif action == "remove":
        remove(grocery_list, items)
    items = input("Enter your items: ").lower()    
    action = input("Are you adding or removing an item? (add/remove) " ).lower()
    ask = input("Would you like to continue? (yes/no): ")


print_list(grocery_list)
        
        

