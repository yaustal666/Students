def find_lost_item(item_list, target_item):
    for i in range(len(item_list)):
        if item_list[i] == target_item:
            return i
    return -1

def lin(item_list, target_item):
    for i, value in enumerate(item_list):
        if value == target_item:
            return i
    return -1