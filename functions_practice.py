def hello():
    print("Hello User")

def pack(arg1, arg2, arg3):
    return[arg1, arg2, arg3]

def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My lunchbox is empty")
    for food_index in range(len(my_lunch)):
        food = my_lunch[food_index]
        if food_index == 0:
            print(f"First i eat {food}")
        else:
            print(f"Then i eat {food}")

hello()
print(pack(1,2,3))
eat_lunch(["Meat", "Chicken", "corn", "beats"])
eat_lunch([])