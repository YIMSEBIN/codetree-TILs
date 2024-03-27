class Bomb :
    def __init__(self, code, color, second) :
        self.code = code
        self.color = color
        self.second = second

code, color, second = map(str, input().split())
bomb = Bomb(code, color, int(second))
print("code : %s" % bomb.code)
print("color : %s" % bomb.color)
print("second : %d" % bomb.second)