import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/* 1이 될 때까지 */
public class greedy_04 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int cnt = 0;
        while (n >= k) {
            // 나눌 수 있을 때 까지 뺄셈
            while (n % k != 0) {
                n--;
                cnt++;
            }
            // 최대한 많이 나눔
            n /= k;
            cnt++;
        }
        // 남은 수가 1이 될 때까지
        while (n > 1) {
            n--;
            cnt++;
        }
        System.out.println(cnt);
    }
}
