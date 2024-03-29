import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Node2 implements Comparable<Node2> {

    private int index;
    private int distance;

    public Node2(int index, int distance) {
        this.index = index;
        this.distance = distance;
    }

    public int getIndex() {
        return this.index;
    }

    public int getDistance() {
        return this.distance;
    }

    @Override
    public int compareTo(Node2 other) {
        if (this.distance < other.distance) {
            return -1;
        }
        return 1;
    }
}

public class ShortestPath_02 {

    public static int INF = (int) 1e9;
    public static ArrayList<ArrayList<Node2>> graph = new ArrayList<ArrayList<Node2>>();
    public static int[] d = new int[30001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        // 그래프 초기화
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<Node2>());
        }

        // 간선 정보 입력
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());

            graph.get(x).add(new Node2(y, z));
        }

        // 최단 거리 테이블 초기화
        Arrays.fill(d, INF);

        // 다익스트라 알고리즘 수행
        dijkstra(c);

        // 메시지를 받는 도시의 총 개수와 총 소요 시간 출력
        int count = 0;
        int maxVal = 0;
        for (int i = 1; i <= n; i++) {
            if (d[i] != INF) {
                count++;
                maxVal = Math.max(maxVal, d[i]);
            }
        }
        System.out.println((count - 1) + " " + maxVal);
    }

    public static void dijkstra(int start) {
        PriorityQueue<Node2> pq = new PriorityQueue<>();
        // 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
        pq.offer(new Node2(start, 0));
        d[start] = 0;

        while (!pq.isEmpty()) { // 큐가 비어있지 않다면

            // 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
            Node2 node = pq.poll();
            int dist = node.getDistance(); // 현재 노드까지의 비용
            int now = node.getIndex(); // 현재 노드

            // 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            if (d[now] < dist)
                continue;

            // 현재 노드와 연결된 다른 인접한 노드들을 확인
            for (int i = 0; i < graph.get(now).size(); i++) {
                int cost = d[now] + graph.get(now).get(i).getDistance();
                // 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if (cost < d[graph.get(now).get(i).getIndex()]) {
                    d[graph.get(now).get(i).getIndex()] = cost;
                    pq.offer(new Node2(graph.get(now).get(i).getIndex(), cost));
                }
            }
        }
    }
}
