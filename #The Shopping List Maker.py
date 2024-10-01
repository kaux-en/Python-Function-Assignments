#The Shopping List Maker

#Task 1:Write a function that lets the user add items to a list
#Task 2:Include a function to remove items from the list
#Task 3:Add a function that prints out the entire list in a formatted way

input("Press enter then add your items.").lower()
input("When finished, type 'done'").lower()

grocery_items = []
    
    
while True:
    items = input()
    if items == "done":
        print("Your grocery list is complete!")
        break

    if items == "remove":
        input("Enter item you want to remove:" )
        remove_item = input()
        print(grocery_items.remove(remove_item))

    if items != "done":
        grocery_items.append(items) 
    print(grocery_items, sep='-')

 
        
        

