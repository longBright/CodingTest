import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Prob_2742 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        br.close();

        StringBuilder sb = new StringBuilder();

        while (n > 0) {
            sb.append(n + "\n");
            n--;
        }
        System.out.print(sb);
    }
}
