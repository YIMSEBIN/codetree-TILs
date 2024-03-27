class Meeting :
    def __init__(self, code, loca, time) :
        self.code = code
        self.location = loca
        self.time = time

code, point, time = map(str, input().split(' '))
meeting = Meeting(code, point, int(time))
print("secret code : %s" % meeting.code)
print("meeting point : %s" % meeting.location)
print("time : %d" % meeting.time)