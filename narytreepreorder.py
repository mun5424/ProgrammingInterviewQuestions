#Given an interface monarchy, implement its methods
from typing import Collection


class Person:
    def __init__(self, name):
        self.name = name
        self.isAlive = True 
        self.children = []
    

class Monarchy:
    def __init__(self):
        self.root = None 
        self.monarchs = {} 
    
    def birth(self, child, parent):
        person = Person(child) 
        if not parent and not self.root:
            self.root = person 
        else:
            if parent not in self.monarchs:
                print('parent not found')
            self.monarchs[parent].children.append(person)
        
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
            for c in node.children:
                self._preorder(c, lst)         

    def getOrderOfSuccession(self):
        res = [] 
        self._preorder(self.root, res)
        print(res) 


monarch = Monarchy() 
monarch.birth('King', None)
monarch.birth('Andy', 'King')
monarch.birth('Bob', 'King')
monarch.birth('Catherine', 'King')
monarch.birth('Matthew', 'Andy')
monarch.birth('Alex', 'Bob')
monarch.birth('Asha', 'Bob')

#monarch.getOrderOfSuccession()

monarch.death('King') 

monarch.getOrderOfSuccession()
