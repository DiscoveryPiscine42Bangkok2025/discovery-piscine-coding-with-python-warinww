def check_dir(ls, dir, size , K, board, p = False):
    for rawX, rawY in ls:
        for dx, dy in dir:
            x, y = rawX + dx, rawY + dy
            while 0 <= x < size and 0 <= y < size:
                if [x, y] == K:
                    return True
                if board[x][y] != "." or p:
                    break
                x += dx
                y += dy
    return False

def checkmate(board):
    board = board.split("\n")
    size = len(board)
    col = [len(board[i]) for i in range(size)]
    check_piece = False

    for i in col:
        if i != size:
            print("Error, board need to be NxN.")
            return
        
    K = None
    P_ls, B_ls, R_ls, Q_ls = [[] for _ in range(4)]
    # P, B, R, Q
    dir = [
        [(-1,-1), (-1,1)],
        [(-1,-1), (-1,1), (1,-1), (1,1)],
        [(-1,0), (1,0), (0,-1), (0,1)], 
        [(-1,0), (1,0), (0,-1), (0,1), (-1,-1), (-1,1), (1,-1), (1,1)]
    ]
    
    for i in range(size):
        for j in range(size):
            if board[i][j] == "K":
                K = [i, j]
            elif board[i][j] == "P":
                P_ls.append([i, j])
            elif board[i][j] == "B":
                B_ls.append([i, j])
            elif board[i][j] == "R":
                R_ls.append([i, j])
            elif board[i][j] == "Q":
                Q_ls.append([i, j])
            elif board[i][j] != ".":
                check_piece = True

    if K is None:
        print("Error, don't have K in game.")
        return
    
    if check_piece:
        print("Error, piece undefined.")
        return

    P_result = check_dir(P_ls, dir[0], size, K, board, p = True)
    B_result = check_dir(B_ls, dir[1], size, K, board)
    R_result = check_dir(R_ls, dir[2], size, K, board)
    Q_result = check_dir(Q_ls, dir[3], size, K, board)
    
    print("Success" if P_result or B_result or R_result or Q_result else "Fail")