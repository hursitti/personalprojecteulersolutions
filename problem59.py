import time

def getEncryptedMessage(fileName):
    with open(fileName, "r") as f:
        return [int(x) for x in f.next().split(",")]

def oldCycleDecrypt(x, y, z, em):
    li = [x, y, z]
    i = 0
    ret = ""
    while i < len(em):
        ret += chr(em[i] ^ li[i%3])
        i += 1
    return ret

def cycleDecrypt(x, y, z, em):
    li = [x, y, z]
    #inspired from this post https://waymoot.org/home/python_string/
    return ''.join([chr(em[i] ^ li[i%3]) for i in range(len(em))])

def generatePossibleMessages(em, decryptionMethod):
    ret = []
    ret2 = []
    r = range(97, 123)
    for x in r:
        for y in r:
            for z in r:
                cd = decryptionMethod(x, y, z, em)
                ret.append((chr(x) + chr(y) + chr(z), cd))
    return ret

def writeQuery (messages, outputName):
    with open(outputName, "w") as f:
        for key, message in messages:
            f.write(key + "\n" + message + "\n\n")

def buildQuery (wordList, messages):
    ret = []
    for key, message in messages:
        matching = True
        for word in wordList:
            if (word not in message):
                matching = False
        if matching:
            ret.append((key, message))
    ret.sort(reverse = True, key = lambda p : sum([p[1].count(word) for word in wordList]))
    return ret

em = getEncryptedMessage("0059_cipher.txt")
messages = generatePossibleMessages(em, cycleDecrypt)
b = buildQuery (["the"], messages)
writeQuery(b, "output2.txt")


def compareConcatMethods(a, b, trials, em):
    aTime = 0
    bTime = 0
    for i in range(trials):
        tTime = time.time()
        generatePossibleMessages(em, a)
        aTime += time.time() - tTime
        tTime = time.time()
        generatePossibleMessages(em, b)
        bTime += time.time() - tTime
    return (aTime/trials, bTime/trials)












