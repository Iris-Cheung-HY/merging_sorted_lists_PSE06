def merge_lists(list_1, list_2):
    if not list_1:
        return list_2
    elif not list_2:
        return list_1
    
    list_1_pos = 0
    list_2_pos = 0
    new_list = []
    while list_1_pos < len(list_1) and list_2_pos < len(list_2):

        item_1 = list_1[list_1_pos]
        item_2 = list_2[list_2_pos]

        if item_1 < item_2:
            new_list.append(item_1)
            list_1_pos += 1
        elif item_1 > item_2:
            new_list.append(item_2)
            list_2_pos += 1
        elif item_1 == item_2:
            new_list.append(item_1)
            new_list.append(item_2)
            list_1_pos += 1
            list_2_pos += 1

    if list_1_pos == len(list_1) and list_2_pos < len(list_2):
        for item in list_2[list_2_pos:]:
            new_list.append(item)

    elif list_1_pos < len(list_1) and list_2_pos == len(list_2):
        for item in list_1[list_1_pos:]:
            new_list.append(item)


    return new_list


        
        

