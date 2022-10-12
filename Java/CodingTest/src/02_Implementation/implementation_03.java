import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/* 왕실의 나이트 */
public class implementation_03 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String inputString = br.readLine();
        int row = inputString.charAt(1) - '0';
        int col = inputString.charAt(0) - 'a' + 1;
        int[][] types = { { -2, -1 }, { -2, 1 }, { 2, -1 }, { 2, 1 }, { -1, -2 }, { -1, 2 }, { 1, -2 }, { 1, 2 } };
        int cnt = 0;

        int nrow, ncol;
        for (int[] type: types) {
            nrow = row + type[0];
            ncol = col + type[1];
            if (nrow < 1 || nrow > 8 || ncol < 1 || ncol > 8) {
                continue;
            }
            cnt++;
        }
        System.out.println(cnt);
    }
}
