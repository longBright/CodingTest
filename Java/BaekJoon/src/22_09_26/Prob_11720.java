import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Prob_11720 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());  // n
        String str = br.readLine();
        int result = 0;

        for (int i = 0; i < n; i++) {
            result += str.charAt(i) - '0';
        }

        System.out.println(result);
        br.close();
    }
}
