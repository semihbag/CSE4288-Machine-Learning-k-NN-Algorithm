import math

# euclidean distance calculator 
def euclidean(current_instance, test_instance):
    
    # initial distance is zero
    distance = 0
    for item in current_instance:
        if item == 'Day' and item == 'PlayTennis':
            continue
        distance += (current_instance[item] - test_instance[item]) ** 2

    return math.sqrt(distance)


# manhattan distance calculator
def manhattan(current_instance, test_instance):
    pass