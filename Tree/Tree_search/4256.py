

if __name__ == '__main__' :
    how_many_test = int(input())

    for i in range(how_many_test) :
        nodes = int(input())
        preorder = list(map(int, input().split()))
        inorder = list(map(int, input().split()))