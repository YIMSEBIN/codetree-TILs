class Spy :
    def __init__(self, codename, grade) :
        self.codename = codename
        self.grade = grade

min_spy = Spy('', 100)
for _ in range(5) :
    codename, grade = map(str, input().split(' '))
    spy = Spy(codename, int(grade))
    if min_spy.grade > spy.grade :
        min_spy = spy

print(min_spy.codename, min_spy.grade)