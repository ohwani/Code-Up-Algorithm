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



def final_solution(board, moves):
    temp = []
    answer = 0
    for move in moves:
        for n in range(len(board)):
            if board[n][move - 1] != 0:
                temp.append(board[n][move - 1])
                board[n][move - 1] = 0
                if len(temp) > 1 and temp[-1] == temp[-2]:
                    temp.pop()
                    temp.pop()
                    answer += 2
                break   # break가 첫번째 if문의 블록 속에 존재해야된다. 아니면 move에 대한 반복문이 초기화가 되지 않아서 이상하게 돈다..

    return answer

