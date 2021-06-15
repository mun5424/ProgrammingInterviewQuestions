#Given an interface monarchy, implement its methods
from typing import Collection
import heapq

class Person:
    def __init__(self, name, age = 0):
        self.name = name
        self.isAlive = True 
        self.age = age
        self.children = []
    

class Monarchy:
    def __init__(self):
        self.root = None 
        self.monarchs = {} 
        setattr(Person, "__lt__", lambda self, other: self.age <= other.age)

    def birth(self, child, parent, age = 0):
        person = Person(child) 
        if not parent and not self.root:
            self.root = person 
        else:
            if parent not in self.monarchs:
                print('parent not found')
            
            heapq.heappush(self.monarchs[parent].children, person)
        
        self.monarchs[child] = person
    
    def death(self, name):
        if name not in self.monarchs:
            print('person not found')
        else:
            person = self.monarchs[name]
            if not person.isAlive:
                print(name, ' was already dead') 
            else:
                person.isAlive = False
    
    def _preorder(self, node, lst):
        if node:
            if node.isAlive:
                lst.append(node.name)
            for i in range(len(node.children)-1,-1,-1 ):
                self._preorder(node.children[i], lst)         

    def getOrderOfSuccession(self):
        res = [] 
        self._preorder(self.root, res)
        print(res) 


monarch = Monarchy() 
monarch.birth('King', None)
monarch.birth('Andy', 'King', 16)
monarch.birth('Bob', 'King', 32)
monarch.birth('Catherine', 'King')
monarch.birth('Matthew', 'Andy')
monarch.birth('Alex', 'Bob')
monarch.birth('Asha', 'Bob')

print(monarch.monarchs['King'].children[0].name)
print(monarch.monarchs['King'].children[1].name)
print(monarch.monarchs['King'].children[2].name)

#monarch.getOrderOfSuccession()


monarch.getOrderOfSuccession()
