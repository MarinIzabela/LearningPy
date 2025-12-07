item1 = "Milk"
item2 = "Bread"
item3 = "Butter"
item4 = "Suggar"
item5 = "Eggs"

milk_available = False
bread_available =False
butter_available = True
suggar_available = True
eggs_available = True

search_item= input("Insert the search item : ").strip().capitalize()
print(search_item)

if(search_item!=item1 and search_item!=item2 and search_item!=item3 and search_item!=item4 and search_item!=item5):
    print("The item is not on the list")

if search_item==item1 and milk_available:
        print("Milk is available ")
if search_item==item1 and not milk_available:
        print("Milk is available ")
if search_item==item2 and bread_available:
    print("Bread is available ")
if search_item==item2 and not bread_available:
    print("Bread is not available ")

if search_item==item3 and butter_available:
    print("Butter is available ")
if search_item==item3 and not butter_available:
    print("Butter is not  available ")
if search_item==item4 and suggar_available:
    print("Suggar is available ")
if search_item==item4 and not suggar_available:
    print("Suggar is not available ")
if search_item==item5 and eggs_available:
    print("Eggs are available ")
if search_item==item5 and not eggs_available:
    print("Eggs are not available ")

