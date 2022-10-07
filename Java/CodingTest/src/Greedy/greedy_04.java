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
            while (n % k != 0) {
                n--;
                cnt++;
            }
            n /= k;
            cnt++;
        }
        while (n > 1) {
            n--;
            cnt++;
        }
        System.out.println(cnt);
    }
}
