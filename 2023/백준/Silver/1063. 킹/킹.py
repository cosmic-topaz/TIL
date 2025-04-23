def f(King, Dorr, N):
    move, cmd, board = dict(), ' RTBL', 'X12345678XABCDEFGHX'
    for i in range(8): # 0 ~ 7
        for j in range(-1, 2): # -1 ~ 1
            move[(board[i+10]+cmd[j]).strip()] = board[i+10+j] # A~H + LR
            move[(board[i+10]+cmd[2*j]).strip()] = board[i+10]  # A~H + BT
            move[(board[i+1]+cmd[j]).strip()] = board[i+1] # 0~8 + LR
            move[(board[i+1]+cmd[2*j]).strip()] = board[i+1+j] # 0~8 + BT
    
    for _ in range(int(N)):
        # 입력을 받는다.
        c = input().strip()
        k_next = ''.join(move[x+y] for x in King for y in c)
        k_next = k_next[0]+k_next[-1]
        if k_next == Dorr:
            d_next = ''.join(move[x+y] for x in Dorr for y in c)
            d_next = d_next[0]+d_next[-1]
        else:
            d_next = Dorr
        if 'X' not in d_next+k_next:
            King, Dorr = k_next, d_next
    rst = '\n'.join([King, Dorr])
    return rst

import sys
input = sys.stdin.readline
inputs = sys.stdin.readlines


T = 1
for _ in range(T):
    print(f(*(input().split())))