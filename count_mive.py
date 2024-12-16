def count_mive(list1):
    mive_ha = {}
    
    for i in list1:
        if i in mive_ha:
            mive_ha[i] += 1
        else:
            mive_ha[i] = 1
    
    return mive_ha

print(count_mive(['sib', 'holo', 'anar', 'anar', 'anar', 'moz', 'moz', 'sib']))