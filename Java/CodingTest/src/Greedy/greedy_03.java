import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class greedy_03 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());

        int max = 1;
        for (int i = 0; i < n; i++) {
            StringTokenizer stz = new StringTokenizer(br.readLine(), " ");
            int min = 10001;
            while (stz.hasMoreTokens()) {
                int temp = Integer.parseInt(stz.nextToken());
                min = Math.min(min, temp);
            }
            max = Math.max(max, min);
        }
        System.out.println(max);
    }
}
