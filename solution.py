def getLeftSubstring(s, u):
    l = ""
    for x in s:
        l += x
        if all(e in l for e in u):
            return l
        else:
            continue

def shortestSubstring(s):
    u = ''.join(sorted(list(set(s))))
    return ''.join(reversed(getLeftSubstring(''.join(reversed(getLeftSubstring(s, u))), u)))


arr = "accbeddbcaffcaedbadec"
print(shortestSubstring(arr))
