def red_knight(N, P):
    knight = dis, color = (0, N)
    count = 0
    while dis < P:
        P+=1
        dis+=2
        count+=1
    
    if color == 1:
        knight = ('Black', dis)
    else:
        knight = ('White', dis)
    return knight

#N is the row the knight starts in, column for knight will be 0 in a 2*n sized chessboard
#Black pawn in row 1 and white in 0 with column being P
#Function to find out at hich square will the knight catch le pawn. and which one
print(red_knight(1, 9888))