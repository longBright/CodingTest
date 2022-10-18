import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

// 위에서 아래로
public class Sort_01 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Integer[] arr = new Integer[n];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        // 내림차순 정렬
        Arrays.sort(arr, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]).append(" ");
        }
        System.out.println(sb);
    }
}
