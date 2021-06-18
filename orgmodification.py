# given an n-ary tree with values E and N, modify it so that the tree is only composed of E values.

#             E 
#        E    N   E
#       E N   E 

# will be 

#             E 
#        E    E   E
#        E 
# 
class Employee:
    def __init__(self, empid, isengineer):
        self.empid = empid
        self.isengineer = isengineer
        self.reportees = []


def orgmodification(root): 
    node = root 
    newreportees = []
    for emp in root.reportees:
        newreportees += orgmodification(emp)
    
    if not root.isengineer:
        return newreportees
    root.reportees = newreportees 
    
    return [node]
