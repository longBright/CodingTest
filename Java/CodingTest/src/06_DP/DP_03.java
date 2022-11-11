import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 바닥 공사
public class DP_03 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int d[] = new int[1001];

        // DP 테이블 초기화
        d[1] = 1;
        d[2] = 3;

        // 점화식에 맞는 반복문 실행
        for (int i = 3; i < n + 1; i++) {
            d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796;
        }
        System.out.println(d[n]);
    }
}
