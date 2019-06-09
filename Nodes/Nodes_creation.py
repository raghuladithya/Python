class daynamenodes:
    def __init__(self,data):
        self.data = data
        self.next = None

e1 = daynamenodes("Monday")
e2 = daynamenodes("Tuesday")
e3 = daynamenodes("Wednesday")
e4 = daynamenodes("Thursday")

e1.next = e2
e2.next = e3
e3.next = e4

dayvalue = e1

while dayvalue:
    print(dayvalue.data)
    dayvalue = dayvalue.next
