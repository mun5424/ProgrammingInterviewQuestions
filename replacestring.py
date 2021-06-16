# given hashmap and its values, replace a string with #
def replacestring(map, s):
    lst = s.split('#') 
    for i,v in enumerate(lst):
        if v in map:
            lst[i] = map[v]
    
    return ''.join(lst) 


map = {'user':'Charlie', 'city':'LA'}
s = 'mynameis#user#city' 

print(replacestring(map,s))
