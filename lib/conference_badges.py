def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badgeList = []
    for name in names:
        badgeList.append(badge_maker(name))
    return badgeList

def assign_rooms(names):
    roomNum = 1
    newList = []
    while roomNum <= 8:
        for name in names:
            newList.append(f"Hello, {name}! You'll be assigned to room {roomNum}!")
            roomNum += 1
    return newList

def printer(names):
    # for name in names:
    for element in batch_badge_creator(names):
        print(element)
        
    for element in assign_rooms(names):
        print (element)

    # return None
