class Person :
    def __init__(self, name, address, location) :
        self.name = name
        self.address = address
        self.location = location

n = int(input())
names = []
people = []
for _ in range(n) :
    name, add, loc = map(str, input().split())
    people.append(Person(name, add, loc))
    names.append(name)
names.sort()

for i in range(n) :
    if people[i].name == names[n-1] :
        print("name %s" % people[i].name)
        print("addr %s" % people[i].address)
        print("city %s" % people[i].location)
        break