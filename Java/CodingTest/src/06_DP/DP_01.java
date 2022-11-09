import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 1로 만들기
public class DP_01 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int X = Integer.parseInt(br.readLine());
        int[] dp = new int[30001]; // DP 테이블 선언(굳이 최댓값의 크기로 선언을 해주어야 하는가?)

        for (int i = 2; i <= X; i++) {
            // 현재 수에서 1을 빼는 경우
            dp[i] = dp[i - 1] + 1;
            // 현재 수가 2의 배수인 경우
            if (i % 2 == 0) {
                dp[i] = Math.min(dp[i / 2] + 1, dp[i]);
            }
            // 현재 수가 3의 배수인 경우
            if (i % 3 == 0) {
                dp[i] = Math.min(dp[i / 3] + 1, dp[i]);
            }
            // 현재 수가 5의 배수인 경우
            if (i % 5 == 0) {
                dp[i] = Math.min(dp[i / 5] + 1, dp[i]);
            }
        }
        System.out.println(dp[X]);
    }
}
