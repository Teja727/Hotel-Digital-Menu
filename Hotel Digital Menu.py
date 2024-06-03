def choose_items(items):
    selected_items = []
    while True:
        for idx, item in enumerate(items, start=1):
            print(f"{idx}. {item}")
        choice = int(input("Choose an item by number (or enter 0 to finish): "))
        if choice == 0:
            break
        elif 1 <= choice <= len(items):
            selected_items.append(items[choice - 1])
            print(f"You selected: {items[choice - 1]}")
        else:
            print("Invalid choice, please try again.")
    return selected_items

Hotal_menu = int(input("Enter \n1.Veg Menu \n2.Non-Veg Menu: "))
if Hotal_menu == 1:
    # Veg Menu
    while True:
        Veg_items = int(input("Enter \n1.Breakfast \n2.Appetizers \n3.Soups \n4.Salads \n5.Sides \n6.Desserts \n7.Beverages \n8.Main Courses \n9.Exit: "))
        Customer_menu = []

        if Veg_items == 1:
            # Breakfast items
            breakfast_items = [
                "Vegetable Omelette (with no meat)",
                "Pancakes/Waffles (with fruit toppings)",
                "Toast with Avocado or other spreads",
                "Fruit Salad",
                "Yogurt with Granola",
                "Smoothies",
                "Oatmeal/Porridge (with fruits and nuts)",
                "Vegetarian Sausages or Patties",
                "Idli/Dosa (Indian breakfast items)",
                "Paratha/Poori with Bhaji (Indian bread with vegetable curry)"
            ]
            print("Breakfast Menu: ")
            selected_items = choose_items(breakfast_items)
            Customer_menu.extend(selected_items)

        elif Veg_items == 2:
            # Appetizer items
            Appetizers = [
                "Spring Rolls (vegetable)",
                "Bruschetta (with tomatoes and basil)",
                "Vegetable Samosas",
                "Stuffed Mushrooms",
                "Caprese Salad (tomato, mozzarella, and basil)"
            ]
            print("Appetizers Menu: ")
            selected_items = choose_items(Appetizers)
            Customer_menu.extend(selected_items)

        elif Veg_items == 3:
            # Soup items
            Soups = [
                "Tomato Soup",
                "Minestrone Soup",
                "Vegetable Soup",
                "Lentil Soup",
                "Mushroom Soup"
            ]
            print("Soups menu: ")
            selected_items = choose_items(Soups)
            Customer_menu.extend(selected_items)

        elif Veg_items == 4:
            # Salad items
            Salads = [
                "Greek Salad (without meat)",
                "Caesar Salad (without chicken)",
                "Garden Salad",
                "Quinoa Salad",
                "Chickpea Salad"
            ]
            print("Salads menu: ")
            selected_items = choose_items(Salads)
            Customer_menu.extend(selected_items)

        elif Veg_items == 5:
            # Side items 
            Sides = [
                "Garlic Bread",
                "Steamed Vegetables",
                "Mashed Potatoes",
                "Rice Pilaf",
                "Couscous"
            ]
            print("Sides menu: ")
            selected_items = choose_items(Sides)
            Customer_menu.extend(selected_items)

        elif Veg_items == 6:
            # Dessert items
            Desserts = [
                "Fruit Tart",
                "Chocolate Mousse",
                "Cheesecake",
                "Sorbet/Ice Cream",
                "Baklava (without honey for vegan option)",
                "Rice Pudding"
            ]
            print("Desserts menu: ")
            selected_items = choose_items(Desserts)
            Customer_menu.extend(selected_items)

        elif Veg_items == 7:
            # Beverage items 
            Beverages = [
                "Fruit Juices",
                "Smoothies",
                "Herbal Teas",
                "Coffee (with plant-based milk options)",
                "Mocktails"
            ]
            print("Beverages menu: ")
            selected_items = choose_items(Beverages)
            Customer_menu.extend(selected_items)

        elif Veg_items == 8:
            # Main Courses items 
            Main_Courses = [
                "Vegetable Stir-fry",
                "Pasta Primavera",
                "Margherita Pizza",
                "Vegetable Curry (with rice or naan)",
                "Stuffed Bell Peppers",
                "Eggplant Parmesan",
                "Vegetarian Lasagna",
                "Paneer Tikka (Indian grilled cheese)",
                "Falafel with Hummus and Pita",
                "Ratatouille"
            ]
            print("Main Courses: ")
            selected_items = choose_items(Main_Courses)
            Customer_menu.extend(selected_items)

        elif Veg_items == 9:
            print("Thanks for your choice")
            print("Your selected items:", Customer_menu)
            break

        else:
            print("Invalid choice, please try again.")

        Customer_Choice = int(input("Enter \n1. Choose More \n2. Exit: "))
        if Customer_Choice == 2:
            print("Thanks for your choice")
            print("Your selected items:", Customer_menu)
            break
else:
    while True:
        Non_Veg_items = int(input("Enter \n1.Breakfast \n2.Appetizers \n3.Soups \n4.Salads \n5.Sides \n6.Desserts \n7.Beverages \n8.Main Courses \n9.Exit: "))
        Customer_menu = []

        if Non_Veg_items == 1:
            # Breakfast items
            breakfast_items = [
                "Bacon and Eggs",
                "Sausage and Egg Muffin",
                "Ham and Cheese Omelette",
                "Chicken Sausage",
                "Smoked Salmon Bagel",
                "Breakfast Burrito (with bacon or sausage)",
                "Steak and Eggs",
                "Chicken and Waffles"
            ]
            print("Breakfast Menu: ")
            selected_items = choose_items(breakfast_items)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 2:
            # Appetizer items
            Appetizers = [
                "Chicken Wings",
                "Shrimp Cocktail",
                "Beef Nachos",
                "Crab Cakes",
                "Chicken Tenders",
                "Buffalo Wings",
                "Prawn Tempura",
                "Lamb Kebabs"
            ]
            print("Appetizers Menu: ")
            selected_items = choose_items(Appetizers)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 3:
            # Soup items 
            Soups = [
                "Chicken Noodle Soup",
                "Clam Chowder",
                "Beef Stew",
                "Seafood Bisque",
                "Lobster Soup",
            ]
            print("Soups menu: ")
            selected_items = choose_items(Soups)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 4:
            # Salad items 
            Salads = [
                "Caesar Salad (with chicken)",
                "Chicken Salad",
                "Tuna Salad",
                "Shrimp Salad",
                "Cobb Salad (with bacon and chicken)"
            ]
            print("Salads menu: ")
            selected_items = choose_items(Salads)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 5:
            # Side items 
            Sides = [
                "Mashed Potatoes with Gravy",
                "French Fries (served with chicken or fish)",
                "Coleslaw (with bacon bits)",
                "Rice Pilaf (with chicken or shrimp)",
                "Garlic Butter Shrimp"
            ]
            print("Sides menu: ")
            selected_items = choose_items(Sides)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 6:
            # Dessert items 
            Desserts = [
                "Fruit Tart",
                "Chocolate Mousse",
                "Cheesecake",
                "Sorbet/Ice Cream",
                "Baklava (without honey for vegan option)",
                "Rice Pudding",
                "Cheesecake (ensure no gelatin if strict non-veg)",
                "Chocolate Mousse (ensure no gelatin)",
                "Tiramisu (contains eggs)",
                "Bread Pudding (contains eggs)"
            ]
            print("Desserts menu: ")
            selected_items = choose_items(Desserts)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 7:
            # Beverage items 
            Beverages = [
                "Fruit Juices",
                "Smoothies",
                "Herbal Teas",
                "Coffee (with plant-based milk options)",
                "Mocktails",
                "Bloody Mary (contains clam juice)",
                "Milkshakes (contains dairy, eggs)"
            ]
            print("Beverages menu: ")
            selected_items = choose_items(Beverages)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 8:
            # Main Courses items 
            Main_Courses = [
                "Grilled Chicken Breast",
                "Beef Steak",
                "Roast Lamb",
                "Grilled Salmon",
                "Chicken Curry",
                "Beef Stroganoff",
                "Fish and Chips",
                "Pork Chops",
                "Chicken Alfredo Pasta",
                "Seafood Paella"
            ]
            print("Main Courses: ")
            selected_items = choose_items(Main_Courses)
            Customer_menu.extend(selected_items)


        elif Non_Veg_items == 9:
            print("Thanks for your choice")
            print("Your selected items:", Customer_menu)
            break

        else:
            print("Invalid choice, please try again.")

        Customer_Choice = int(input("Enter \n1. Choose More \n2. Exit: "))
        if Customer_Choice == 2:
            print("Thanks for your choice")
            print("Your selected items:", Customer_menu)
            break