import java.util.Scanner;

// 팀 결성
public class Graph_01 {
    // 노드의 개수 n, 간선의 개수 m
    public static int n, m;
    public static int[] parent = new int[100001];

    // Find 연산
    public static int findParent(int x) {
        // 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
        if (x == parent[x]) {
            return x;
        }
        return parent[x] = findParent(parent[x]);
    }

    // Unino 연산
    public static void unionParent(int a, int b) {
        // 루트 노드를 찾음
        a = findParent(a);
        b = findParent(b);
        // 둘 중 작은 값을 부모 노드로 설정
        if (a < b) {
            parent[b] = a;
        } else {
            parent[a] = b;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        // 부모 테이블 초기화(자기 자신)
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < m; i++) {
            int oper = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();

            // Union 연산 수행
            if (oper == 0) {
                unionParent(a, b);
            }
            // Find 연산 수행 후 결과 출력
            else {
                if (findParent(a) == findParent(b)) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }
        sc.close();
    }
}