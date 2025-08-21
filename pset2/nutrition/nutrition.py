'''
idea = dict = {item:calorie}
we need to print calorie when item taken as input
print(dict[key])
'''
food =  {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew Melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
        }

item = input("Input: ").lower() #case insensitive and lower

if item in food:
    print("Calories:",food[item])
