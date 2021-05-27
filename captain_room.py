def captain_room(room_list):
    """This function prints captain list which is a unique room that appears once in a list"""
    captain_room = '' 
    #store the list in total_rooms
    total_rooms = room_list 
    #get the unique rooms without repetition of any room
    unique_rooms_num = set(total_rooms) 
    #Remove the unique room from the list of total rooms
    for n in unique_rooms_num:
        total_rooms.remove(n) 
        without_captain_room = total_rooms
        #The original total room list does not contain captain room number anymore
        #check by print(total_rooms)

        #Now, Compare the unique room number: that contains captain number with
        #list without_captain_room
        for i in unique_rooms_num:
            if i not in without_captain_room: 
                captain_room = i
    
    return captain_room

print(captain_room([1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]))
print(captain_room([67,67,1,2,3,4,5,1,2,6,1,2,3,4,5,6,7]))