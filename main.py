from utils.time_check import logging_time

@logging_time
def solution(participant, completion):
    completion.sort()
    participant.sort()
    while completion:
        p = completion.pop()
        if p in participant:
            idx = participant.index(p)
            participant.pop(idx)
    answer = participant[0]
    return answer

solution(['leo', 'kiki', 'eden'],['eden', 'kiki'])