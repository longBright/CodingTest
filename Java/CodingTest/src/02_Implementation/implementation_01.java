import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/* 상하좌우 */
public class implementation_01 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int x = 1;
        int y = 1;
        int n = Integer.parseInt(br.readLine());
        String[] type = { "L", "R", "U", "D" };
        int[] dx = { 0, 0, -1, 1 };
        int[] dy = { -1, 1, 0, 0 };
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int nx = x;
        int ny = y;
        // 입력 받은 계획 실행
        while (st.hasMoreTokens()) {
            String plan = st.nextToken();
            // 이동 방향 탐색
            for (int i = 0; i < 4; i++) {
                if (plan.equals(type[i])) {
                    nx = x + dx[i];
                    ny = y + dy[i];
                }
            }
            // 범위를 벗어나면 이동 X
            if (nx < 1 || nx > n || ny < 1 || ny > n) {
                continue;
            }
            // 범위를 벗어나지 않으면 이동
            else {
                x = nx;
                y = ny;
            }
        }
        System.out.println(x + " " + y);
    }
}
