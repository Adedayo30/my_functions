def power_list(a_list):
    """The function print the aubaet of a list"""
    pow_set =[[]] #The list that holds the subset
    for elem in a_list: 
        for sub in pow_set:
            pow_set = pow_set + [list(sub) + [elem]]
    return pow_set


print(power_list([1,2,3]))
