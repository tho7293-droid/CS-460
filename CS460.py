# Study groups and their preferred rooms
group_preferences = {
    "GroupA": ["Room1", "Room2", "Room3"],
    "GroupB": ["Room2", "Room3", "Room1"],
    "GroupC": ["Room1", "Room3", "Room2"],
}

# Rooms and their preferred groups
room_preferences = {
    "Room1": ["GroupB", "GroupA", "GroupC"],
    "Room2": ["GroupA", "GroupC", "GroupB"],
    "Room3": ["GroupC", "GroupB", "GroupA"],
}

# Implement Gale-Shapley Algorithm
def gale_shapley(group_pref, room_pref):
    free_groups = list(group_pref.keys())
    group_match = {}
    room_match = {}
    next_proposal = {group: 0 for group in free_groups}
    room_rank = {}
    for room, preferences in room_pref.items():
        room_rank[room] = {}
        for rank, group in enumerate(preferences):
            room_rank[room][group] = rank
    while free_groups: #Case 2: The room is already matched with another group.
        group = free_groups.pop(0)  # Remove the first unmatched group from the free_groups list.
        room = group_pref[group][next_proposal[group]]  # Get the next room on this group's preference list to propose to.
        next_proposal[group] += 1  # Move to the next preference. If this proposal is rejected, the group will propose to the next room on its preference list the next time it gets a chance.
        #If the room is free (not currently matched with any group), then the algorithm immediately matches the group to that room
        if room not in room_match: #Case 1: The room is free. The room accepts the proposal because it isn't matched with anyone.
            room_match[room] = group
            group_match[group] = room
        else: #The room is already matched with another group. This gets the group that is currently assigned to the room.
            current_group = room_match[room]
            if room_rank[room][group] < room_rank[room][current_group]: # If the new group has higher priority than the room switches to the new group.
                room_match[room] = group
                group_match[group] = room
                del group_match[current_group]
                free_groups.append(current_group)
            else: #If not the reject the new group proposal.
                free_groups.append(group)
    return group_match

matches = gale_shapley(group_preferences, room_preferences)

print("Final Matches:")
for group, room in matches.items():
    print(group, "->", room)