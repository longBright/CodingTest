import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Prob_10250 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int h = Integer.parseInt(st.nextToken());
            Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());

            int floor, room;
            if (n % h == 0) {
                floor = h;
                room = n / h;
            }
            else {
                floor = n % h;
                room = n / h + 1;
            }
            sb.append(floor + String.format("%02d", room)).append("\n");
        }
        System.out.println(sb);
    }
}
