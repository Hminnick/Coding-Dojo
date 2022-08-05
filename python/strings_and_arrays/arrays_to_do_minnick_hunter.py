import random

def shuffle(arr):
    for i in range(len(arr)):
        rand_index = random.randint(0,len(arr)-1)
        temp = arr[i]
        arr[i] = arr[rand_index]
        arr[rand_index] = temp

def skyline_heights(building_heights):
    max_building_height=0
    visible_buildings=[]
    for building_height in building_heights:
        if building_height > max_building_height:
            visible_buildings.append(building_height)
            max_building_height = building_height
    return visible_buildings

def zip_it(arr1, arr2):
    larger_arr = arr1 if len(arr1)> len(arr2) else arr2
    new_arr=[]
    for i in range(len(larger_arr)):
        if i <= (len(arr1))-1:
            new_arr.append(arr1[i])
        if i <= (len(arr2))-1:
            new_arr.append(arr2[i])
    return new_arr