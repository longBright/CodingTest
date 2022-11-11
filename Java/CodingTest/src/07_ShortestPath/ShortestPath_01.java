import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class ShortestPath_01 {

    public static final int INF = (int) 1e9;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[][] graph = new int[n + 1][n + 1];

        // 최단 거리 테이블 전부 INF 로 초기화
        for (int i = 0; i < n + 1; i++) {
            Arrays.fill(graph[i], INF);
        }

        // 자기 자신에서 자기 자신으로 가는 비용은 0
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (i == j)
                    graph[i][j] = 0;
            }
        }

        // 각 간선에 대한 정보 입력
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        // X 와 K 입력
        st = new StringTokenizer(br.readLine(), " ");
        int x = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // 점화식에 따른 플로이드 워셜 알고리즘 수행
        floydWarshall(graph, n);

        int result = graph[1][k] + graph[k][x];
        if (result >= INF) {
            System.out.println(-1);
        } else {
            System.out.println(result);
        }
    }

    // 플로이드-워셜 알고리즘
    public static void floydWarshall(int[][] graph, int n) {
        for (int k = 1; k <= n; k++) {
            for (int a = 1; a <= n; a++) {
                for (int b = 1; b <= n; b++) {
                    graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
                }
            }
        }
    }
}
