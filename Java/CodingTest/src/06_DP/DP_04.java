import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 효율적인 화폐 구성
public class DP_04 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] coins = new int[n];
        int[] d = new int[m + 1];

        // 화폐 입력
        for (int i = 0; i < n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        // DP 테이블 초기화
        for (int i = 0; i < m + 1; i++) {
            d[i] = 10001;
        }

        // 점화식에 따라 반복문 실행
        d[0] = 0;
        for (int i = 0; i < n; i++) {
            for (int j = coins[i]; j < m + 1; j++) {
                d[j] = Math.min(d[j], d[j - coins[i]] + 1);
            }
        }

        // 만들 수 없는 경우 -1 출력
        if (d[m] == 10001) {
            System.out.println(-1);
        } else {
            System.out.println(d[m]);
        }
    }
}
