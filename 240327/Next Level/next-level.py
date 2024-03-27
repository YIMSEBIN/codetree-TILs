class User :
    def __init__(self, userid="codetree", level=10) :
        self.userid = userid
        self.level = level

userid, level = map(str, input().split(' '))
user1 = User()
user2 = User(userid, int(level))

print("user %s lv %d" % (user1.userid, user1.level))
print("user %s lv %d" % (user2.userid, user2.level))