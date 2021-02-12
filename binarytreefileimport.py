import pickle
import wget
import os
from dateutil.parser import parse
from csv import DictReader
from datetime import datetime
import sys

class Node:
    def __init__(self, value):
        self.value = value #value is the row of data {id: 123, longitude: 2243}
        self.left = None
        self.right = None
    def insert(self, newValue):
        if (self.value == None):
            self.value = newValue
        elif (float(newValue.get('longitude')) > float(self.value.get('longitude'))):
            if (self.left == None):
                self.left = Node(newValue)
            else:
                self.left.insert(newValue)
        elif (float(newValue.get('longitude')) <= float(self.value.get('longitude'))):
            if (self.right == None):
                self.right = Node(newValue)
            else:
                self.right.insert(newValue)
        else:
            if parse(newValue.get('timestamp')) > parse(self.value.get('timestamp')):
                if (self.left == None):
                    self.left = Node(newValue)
                else:
                    self.left.insert(newValue)
            elif (parse(newValue.get('timestamp')) < parse(self.value.get('timestamp'))):
                if (self.right == None):
                    self.right = Node(newValue)
                else:
                    self.right.insert(newValue)

    def findByLongitude(self, longitude):
        # it's at root
        if (float(self.value.get('longitude')) == float(longitude)):
            return self.value
        # look to left
        elif float(longitude) < float(self.value.get('longitude')):
            if (self.right != None and float(self.right.value.get('longitude')) == float(longitude)):
                return self.right.value
            else:
                return self.right.findByLongitude(longitude)
        # look to right
        elif float(longitude) > float(self.value.get('longitude')):
            if (self.left != None and float(self.left.value.get('longitude')) == float(longitude)):
                return self.left.value
            else:
                return self.left.findByLongitude(longitude)

    def pprint(self):
        if self.left:
            self.left.pprint()
        if self.right:
            self.right.pprint()
        print(self.value) 

def download_files():
    try:
        url = 'https://raw.githubusercontent.com/BuzzFeedNews/2016-04-federal-surveillance-planes/master/data/feds/'
        filenames = ['feds1.csv', 'feds2.csv', 'feds3.csv']
        for file in filenames:
            if os.path.exists(file):
                os.remove(file)
            wget.download(url+file, out=file)
    except:
        print('Error occured while downloading')

def read_file():
    filenames = ['feds1.csv', 'feds2.csv', 'feds3.csv']
    root = None
    for file in filenames:
        dt = datetime.now()
        start = dt.microsecond
        print('reading file '+ file)
        with open(file, 'r') as read_obj:
            csv_dict_reader = DictReader(read_obj)
            # Iterate over each row in the csv using reader object
            for row in csv_dict_reader:
                # row variable is a list that represents a row in csv
                if (root == None):
                    root = Node(row)
                else:
                    root.insert(row)
        dt = datetime.now()
        end = dt.microsecond
        print('end time -----' + str(end - start) + '-------')
    return root

def main():
    sys.setrecursionlimit(10000)
    file = 'storedDataSet'
    # # download_files()
    # tree = read_file()
    # # Dump
    # dt = datetime.now()
    # start = dt.microsecond
    # file = open(file, "wb")
    # pickle.dump(tree, file)
    # dt = datetime.now()
    # end = dt.microsecond
    # print('pickle dump end -----' + str(end-start) + '-------')
    # Dump end
#    Get Tree back
    tree = None
    with open(file, 'rb') as pickle_file:
        tree = pickle.load(pickle_file)
    # tree.pprint()
    records = tree.findByLongitude(-98.7752)
    print('found: ', records)
    
if __name__ == "__main__":
    main()