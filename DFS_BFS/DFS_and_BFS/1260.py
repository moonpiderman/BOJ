
def solution(node, branch, point) :
    answer = 1
    n = node
    b = branch
    p = point

    li = [n, b, p]
    return li


if __name__ == '__main__' :
    node, branch, point = map(int, (input().split(' ')))
    print(solution(node, branch, point))