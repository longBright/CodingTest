import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Prob_2775 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] arr = new int[15][15];

        // dp 테이블 초기화
        for (int i = 0; i < 15; i++) {
            for (int j = 1; j < 15; j++) {
                arr[i][1] = 1;  // i층 1호 = 1
                arr[0][j] = j;  // 0층 j 호 = j
            }
        }

        // dp 테이블 값 갱신
        for (int i = 1; i < 15; i++) {
            for (int j = 2; j < 15; j++) {
                arr[i][j] = arr[i-1][j] + arr[i][j-1];
            }
        }
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++) {
            int k = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());
            sb.append(arr[k][n]).append("\n");
        }
        System.out.println(sb);
    }
}
