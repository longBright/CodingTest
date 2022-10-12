import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/* 게임개발 */
public class implementation_04 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 맵의 크기 입력
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        
        // 시작위치, 시작방향 입력
        st = new StringTokenizer(br.readLine(), " ");
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int direction = Integer.parseInt(st.nextToken());

        // 이동 방향에 따른 배열 선언
        int[] dx = { -1, 0, 1, 0 };
        int[] dy = { 0, 1, 0, -1 };
        
        // 회전 횟수(종료 조건) 및 결과값 선언
        int turnTimes = 0;  // 회전 횟수(종료 조건)
        int cnt = 1;        // 방문 칸 개수(시작 위치도 방문한 것으로 판정해야함)

        // 맵, 방문 리스트 초기화
        int[][] visited = new int[n][m];
        int[][] map = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int nx, ny;
        while (true) {
            // 회전
            direction = turnLeft(direction);

            nx = x + dx[direction];
            ny = y + dy[direction];
            // 이동 가능
            if (map[nx][ny] != 1 && visited[nx][ny] != 1) {
                x = nx;
                y = ny;
                turnTimes = 0;
                visited[x][y] = 1;
                cnt++;
                continue;
            }
            // 이동 불가능
            else {
                turnTimes++; // 회전 횟수 증가
            }
            // 종료 조건
            if (turnTimes == 4) {
                nx = x - dx[direction];
                ny = y - dy[direction];
                // 뒤로 이동 가능
                if (map[nx][ny] != 1) {
                    x = nx;
                    y = ny;
                }
                // 뒤로 이동 불가능
                else {
                    break;
                }
            }
        }
        System.out.println(cnt);
    }

    // 방향 회전 메소드
    public static int turnLeft(int direction) {
        // 북쪽인 경우 서쪽으로
        if (direction == 0) {
            direction = 3;
        }
        direction -= 1;
        return direction;
    }
}
