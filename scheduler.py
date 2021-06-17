class Interval:
    def __init__(self, interval):
        self.interval = interval 
    
    def __lt__(self, other):
        num1 = self.interval.split(':')
        num2 = other.interval.split(':') 
        print(num1)
        print(num2)
        if num1[0] == num2[0]:
            return int(num1[1]) - int(num2[1])
        else:
            return int(num1[0]) - int(num2[0])


def scehduler(schedule, incoming):
    res = []
    for interval in incoming:
        i = 0 
        while interval[0] > schedule[i][1]:
            i += 1
        if i + 1 < len(schedule) and interval[1] <= schedule[i+1][0]:
            schedule.insert()
            res.append[True]
        else:
            res.append(False)

i1 = Interval('10:50')
i2 = Interval('11:55')

if i1 < i2: 
    print(i1)
    print('is less than')
    print(i2) 

