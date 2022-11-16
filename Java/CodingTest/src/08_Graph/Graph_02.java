import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

// 간선 클래스
class Edge implements Comparable<Edge> {
    private int distance;
    private int nodeA;
    private int nodeB;

    public Edge(int distance, int nodeA, int nodeB) {
        this.distance = distance;
        this.nodeA = nodeA;
        this.nodeB = nodeB;
    }

    public int getDistance() {
        return this.distance;
    }

    public int getNodeA() {
        return this.nodeA;
    }

    public int getNodeB() {
        return this.nodeB;
    }

    // 거리(비용)가 짧은 것이 높은 우선순위를 가지도록 설정
    @Override
    public int compareTo(Edge other) {
        if (this.distance < other.getDistance()) {
            return -1;
        }
        return 1;
    }
}

// 도시 분할 계획
public class Graph_02 {
    // 마을(노드) 개수 N, 길(간선) 개수 M
    public static int n, m;
    public static int[] parent = new int[100001];
    // 간선 리스트, 최종 비용 변수
    public static ArrayList<Edge> edges = new ArrayList<>();
    public static int result = 0;

    // Find 연산
    public static int findParent(int x) {
        // 루트 노드를 찾을 때까지 재귀적으로 호출
        if (x == parent[x]) {
            return x;
        }
        return parent[x] = findParent(parent[x]);
    }

    // Union 연산
    public static void unionParent(int a, int b) {
        a = findParent(a);
        b = findParent(b);
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

        // 부모테이블 초기화
        for (int i = 1; i <= n; i++) {
            parent[i] = i;
        }

        // 간선 정보 입력
        for (int i = 0; i < m; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            edges.add(new Edge(c, a, b));
        }

        // 간선 비용순 정렬
        Collections.sort(edges);

        int max = 0;
        // 간선을 하나씩 확인
        for (int i = 0; i < edges.size(); i++) {
            int cost = edges.get(i).getDistance();
            int a = edges.get(i).getNodeA();
            int b = edges.get(i).getNodeB();

            // 사이클이 발생하지 않으면 MST 에 추가
            if (findParent(a) != findParent(b)) {
                unionParent(a, b);
                result += cost;
                max = cost;
            }
        }
        System.out.println(result - max);

        sc.close();
    }
}