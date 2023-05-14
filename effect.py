from commands import Command, CommandType, Condition, ConditionType, compatible, flip

# intersect 2 lists of conditions, removing mutually exclusive
def intersect(a, b):
    c = []
    for condition in a:
        if condition.lhs < condition.rhs:
            c.append(flip(condition))  
        else:
            c.append(condition)

    for condition in b:
        if condition.lhs < condition.rhs:
            c.append(flip(condition))  
        else:
            c.append(condition)

    marked_delete = {}
    for i in range(len(c)):
        marked_delete[i] = False

    for i in range(len(c)):
        for j in range(len(c)):
            if c[i].operator == c[j].operator:
                if c[i].lhs == c[j].lhs:
                    marked_delete[j] = True
                    print("Removed", c[j].toString(), "because lhs equal to", c[i].toString())
                    if c[i].rhs != c[j].rhs:
                        marked_delete[i] = True
                        print("Removed", c[i].toString(), "because rhs different from", c[j].toString())
                elif c[i].lhs == c[j].rhs:
                    marked_delete[j] = True
                    print("Removed", c[j].toString(), "because lhs equal to", c[i].toString())
                    if c[i].rhs != c[j].rhs:
                        marked_delete[i] = True
                        print("Removed", c[i].toString(), "because rhs different from", c[j].toString())
            
            elif not compatible(c[i].operator, c[j].operator):
                marked_delete[j] = True
                marked_delete[i] = True
                print("Removed", c[i].toString(), c[j].toString(), "because different signs")
    
    result = []
    for i in range(c):
        if not marked_delete[i]:
            result.append(c[i])
    return result




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

# return effect of operator on set of conditions N 
def ef(N, condition, operator):
    new_conditions = [condition]
    for var in operator:
        new_conditions.append(Condition(ConditionType.EQ, var, operator[var]))
    
    return intersect(N, new_conditions)
