import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Prob_2231 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int result = 0;
        for (int i = 1; i <= N; i++) {
            int M = 0;
            int temp = i;
            while (temp != 0) {
                M += temp % 10;
                temp /= 10;
            }
            if (M + i == N) {
                result = i;
                break;
            }
        }
        System.out.print(result);
    }
}
