import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/* 시각 */
public class implementation_02 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int count = 0;
        for (int h = 0; h <= n; h++) {
            for (int m = 0; m <= 59; m++) {
                for (int s = 0; s <= 59; s++) {
                    String str = Integer.toString(h) + Integer.toString(m) + Integer.toString(s);
                    if (str.contains("3")) count++;
                }
            }
        }
        System.out.println(count);
    }
}
