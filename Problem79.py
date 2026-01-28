class PasswordCharacter:
    def __init__(self, char):
        self.char = char
        self.lessThan = set()
        self.greaterThan = set()

    def __repr__ (self):
        return repr(self.lessThan) + " " + self.char + " " + repr(self.greaterThan)

def buildCharMap (fileName, attemptLength):
    charMap = dict()
    with open(fileName, "r") as f:
        for line in f.readlines():
            for i in range(attemptLength):
                char = line[i]
                if (char not in charMap):
                    charMap[char] = PasswordCharacter(char)
                for i2 in range(0, i):
                    charMap[char].lessThan.add(line[i2])
                for i2 in range(i + 1, attemptLength):
                    charMap[char].greaterThan.add(line[i2])
    return charMap

b = buildCharMap("0079_keylog.txt", 3)
so = sorted(b.items(), key = lambda item : len(item[1].lessThan))
password = "".join([key for key, value in so])
