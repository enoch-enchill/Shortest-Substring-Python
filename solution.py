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
    ls = getLeftSubstring(s, u)
    v = ''.join(reversed(ls))
    rs = getLeftSubstring(v, u)
    r = ''.join(reversed(rs))
    return r


arr = "accbeddbcaffcaedbadec"
print(shortestSubstring(arr))
