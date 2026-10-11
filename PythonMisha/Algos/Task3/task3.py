def find_apartment(door_list, target_door):
    step = 5

    # if len(door_list) < 50:
    #     step = 5
    # else:
    #     step = len(door_list) // 10

    left = 0
    right = 0

    while len(door_list) - left >= step:
        next_step = left + step
        if door_list[next_step] == target_door:
            return next_step
        if door_list[next_step] > target_door:
            right = next_step
            break
        else:
            left = next_step

    if right == 0:
        right = len(door_list)

    for i in range(left, right):
        if door_list[i] == target_door:
            return i

    return -1