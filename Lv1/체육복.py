'''
문제 설명
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.

제한사항
전체 학생의 수는 2명 이상 30명 이하입니다.
체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
입출력 예
n	lost	reserve	return
5	[2, 4]	[1, 3, 5]	5
5	[2, 4]	[3]	        4
3	[3]	    [1]	        2

'''

# 처음 접근 방법
# 이런식으로 처음해서는 예제3번같은 경우에서 오류가 발생된다. 다시 처음부터 시작
# def solution(n, lost, reserve):
#     student = []
#     for i in range(n):
#         student.append(i + 1)
#
#     for i in range(n):
#         if lost:
#             p = lost.pop()
#             del student[p - 1]
#         else:
#             pass
#
#         if reserve:
#             r = reserve.pop()
#             if not r - 1 == 0 and not r == n:
#                 student.append(r + 1)
#                 student.append(r - 1)
#             elif r - 1 == 1:
#                 student.append(r + 1)
#             elif r + 1 == n:
#                 student.append(r - 1)
#         else:
#             pass
#
#     students = list(set(student))
#     answer = len(students)
#
#     return answer

'''
solution2 
접근 방법
1. answer = 이미 체육복을 가지고 있는 학생 수를 구한다 
 n - len(lost)
2. greedy 알고리즘을 생각하여, 최적의 해를 구하는 데 사용되는 근사적인 방법으로
lost 의 원소가 reserve+1 , reserve-1 가 존재하면 answer +1 해주고, 없애주는형식으로 해서 
answer 을 도출하려고한다.
'''


def solution2(n, lost, reserve):
    answer = n - len(lost)

    for l in lost:
        print(f"1 {lost}, {l}")
        for r in reserve:
            print(lost,l)
            print(reserve,r)
            if l == r:
                reserve.remove(l)
                lost.remove(l)
                answer += 1

    for l in lost:
        print("gk")
        for r in reserve:
            if r == l - 1 or r == l + 1:
                reserve.remove(r)
                answer += 1
                break

    return answer

print(solution2(8, [1,2,5,6], [1,2,5,6] ))



