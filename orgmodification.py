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


emp1 = Employee(1, True)
emp2 = Employee(2, True)
emp3 = Employee(3, False)
emp4 = Employee(4, True)
emp5 = Employee(5, False)
emp6 = Employee(6, True)
emp7 = Employee(7, True)

emp1.reportees = [emp2, emp3, emp4]
emp2.reportees = [emp5, emp6]
emp3.reportees = [emp7]

orgmodification(emp1)
for e in emp1.reportees:
    print(e.empid) 



#             E1 
#        E2    N3   E4
#       E5 N6   E7 
