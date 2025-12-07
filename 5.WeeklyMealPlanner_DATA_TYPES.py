


# Constants
WATER_LITERS_PER_DAY =2
# Predefined meal option for the week
breakfast = "Oar and kefir"
lunch= "Chicken Salad"
dinner_monday ="grilled chicken "
dinner_tuesday ="fish and vegetables"
dinner_wednesday="cream soup"
dinner_thursday ="pizza"
dinner_friday=" pasta"
dinner_saturday="kebab"
dinner_sunday="beef steak"

# Didplay meal plan

print("Day        |      Breakfast|        Lunch|            Dinner|")
print("--------------------------------------------------------------")
print("Monday      |"   +breakfast+ "  | " + lunch+ " |       "+ dinner_monday )
print("Tuesday     |"   +breakfast+"   | " + lunch+ " |        "+ dinner_tuesday )
print("Wednesday   |"   +breakfast+"   | " + lunch+ " |        "+dinner_wednesday )
print("Thursday    |"   +breakfast+ "  | " + lunch+ " |        "+dinner_thursday )
print("Friday      |"   +breakfast+"   | " + lunch+ " |        "+ dinner_friday )
print("Saturday    |"   +breakfast+ "  | " + lunch+ " |        "+ dinner_saturday )
print("Sunday      |"   +breakfast+   "| " + lunch+ " |        "+ dinner_sunday )

# Calculate and display total meals and water requirements
total_meals = 7*3
weekly_water = WATER_LITERS_PER_DAY*7
print("\nSummary :")
print("Total meals planned: " + str(total_meals))
print("Total water requiered for the week : " + str(weekly_water) + " liters")
