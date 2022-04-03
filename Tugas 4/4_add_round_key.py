from rsa import newkeys


state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    newkey = []
    for i in range (0,4):
        temp = []
        for n in range (0,4):
            temp.append(s[i][n]^k[i][n])
            #temp += (s[i][n]^k[i][n])
        newkey+=temp
    charr = []
    for i in newkey:
        charr.append(chr(i))
    return print(*charr, sep="")
    #return newkey

print(add_round_key(state, round_key))

