def solution(board, moves):
    temp = []
    answer = 0
    for move in moves:
        for n in range(len(board)):
            if board[n][move-1] == 0:
                pass
            else:
                temp.append(board[n][move-1])
                board[n][move-1] = 0
                break
            if len(temp) >= 2 and temp[len(temp)-1] == temp[len(temp)-2]:
                temp.pop(-1)
                temp.pop(-1)
                answer += 1
    return answer*2