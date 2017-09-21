def is_palindrome(n):
    s = str(n)
    res = True
    for i in range(len(s)//2):
        res &= s[i]==s[len(s)-i-1]
    return res
output = filter(is_palindrome, range(10000, 99999))
print(list(output))
