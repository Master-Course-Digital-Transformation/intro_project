def double_list_imperative(l):
    for i in range(0,len(l)):
        l[i] = 2*l[i]
    return l

def double_list_functional(l):
    return [2*x for x in l]

print(double_list_imperative([1,2,3,4,5,6]))
print(double_list_functional([1,2,3,4,5,6]))