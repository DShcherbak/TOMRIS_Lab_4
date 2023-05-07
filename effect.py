from commands import Command, CommandType, Condition, ConditionType, flip

# intersect 2 lists of conditions, removing mutually exclusive
def intersect(a, b):
    c = []
    for condition in a:
        if condition.lhs < condition.rhs:
            c.append(flip(condition))  
        else:
            c.append(condition)
    a = c

    c = []
    for condition in b:
        if condition.lhs < condition.rhs:
            c.append(flip(condition))  
        else:
            c.append(condition)
    b = c




# check if 2 lists of conditions are equal
def equal(a,b):
    if len(a) != len(b):
        return False
    
    c = []
    for condition in a:
        if condition.lhs < condition.rhs:
            c.append(flip(condition))  
        else:
            c.append(condition)
    a = c

    c = []
    for condition in b:
        if condition.lhs < condition.rhs:
            c.append(flip(condition))  
        else:
            c.append(condition)
    b = c

    for i in range(len(a)):
        if a[i].lhs != b[i].lhs:
            return False 
        if a[i].rhs != b[i].rhs:
            return False 
        if a[i].operator != b[i].operator:
            return False
    
    return True

# return 
def ef(N, condition, operator):
    new_values = [condition]
    for 
