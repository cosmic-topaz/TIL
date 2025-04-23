def rot13(chr):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789\n\t'
    b = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm 0123456789\n\t'
    return b[a.index(chr)]

S = input().rstrip()
rst = ''.join([rot13(chr) for chr in S])
print(rst)