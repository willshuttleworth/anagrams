import sys

def permute(prefix, s):
    n = len(s)
    if n == 0:
        if prefix in dict and prefix not in sols:
            sols.append(prefix)
        return
    else:
        for i in range(n):
            permute(prefix + s[i], s[0:i] + s[i+1:n])

def tobitstring(num):
    global bits
    if num >= 1:
        tobitstring(num // 2)
        bits = bits + str(num % 2)

f = open('dict.txt')
# dictionary list
dict = [line.rstrip() for line in open('dict.txt')]

# letters given in anagrams game
letters = sys.argv[1]
bits = ''

# list of solutions
sols = []

for i in range(1, 64):
    tobitstring(i)
    while(len(bits) < 6):
        bits = '0' + bits
    # create new string with only characters that are '1' in bitstring, call permute on that if len(str) >= 3
    string = ''
    for j in range(6):
        if bits[j] == '1':
            string = string + letters[j]
    if len(string) >= 3:
        permute('', string)
    bits = ''

print(sorted(sols, key=len, reverse=True))

