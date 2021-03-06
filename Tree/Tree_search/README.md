### 🧑‍💻 [트리 baekjoon_4256](https://www.acmicpc.net/problem/4256)

![initial](https://user-images.githubusercontent.com/70942197/118909507-18426180-b95e-11eb-83c2-d74b99bd1eef.png)
>
> - BT를 전위 순회, 중위 순회한 결과가 주어진다.
> - 즉, 위의 함수 중 preorder(root node of BT)와 inorder(root node of BT)를 호출해서 만든 리스트가 주어진다.
> - 두 순회한 결과를 가지고 다시 BT를 만들 수 있다.
> - BT의 전위, 중위 순회한 결과가 주어졌을 때, 후위 순회했을 때의 결과를 구하는 프로그램을 작성하시오.
> - 예를 들어, 위의 그림을 전위 순회하면 3,6,5,4,8,7,1,2, 중위 순회하면 5,6,8,4,3,1,2,7이 된다. 이를 이용해 후위 순회하면 5,8,4,6,2,1,7,3이 된다
> 

> **입력**
> - 첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스의 첫째 줄에는 노드의 개수 n이 주어진다.
> - (1 ≤ n ≤ 1,000) BT의 모든 노드에는 1부터 n까지 서로 다른 번호가 매겨져 있다.
> - 다음 줄에는 BT를 전위 순회한 결과, 그 다음 줄에는 중위 순회한 결과가 주어진다. 
> - 항상 두 순회 결과로 유일한 이진 트리가 만들어지는 경우만 입력으로 주어진다.

![initial](https://user-images.githubusercontent.com/70942197/118909905-a61e4c80-b95e-11eb-80f4-3cd55ea43d42.png)
