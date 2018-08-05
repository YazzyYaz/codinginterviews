def powerset_of_set(aset):
    set_list = [x for x in aset]
    final_set = set() 
    for catchnum in range(len(set_list)):
        print(catchnum)
        for index in range(catchnum, len(set_list)):
            b = "{}".format(set_list[index:])
            if b not in final_set:
                final_set.add(b)
    return final_set

def powerset_of_set(aset):
    set_list = [x for x in aset]
    for item in set_list:
        dfs

aset = set(['x', 'y', 'z'])
print(powerset_of_set(aset))
