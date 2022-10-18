import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

// 두 배열의 원소 교체
public class Sort_03 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        // N, K 입력
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // 배열 A 입력
        st = new StringTokenizer(br.readLine(), " ");
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(a); // A 는 오름차순 정렬

        // 배열 B 입력
        st = new StringTokenizer(br.readLine(), " ");
        Integer[] b = new Integer[n];
        for (int i = 0; i < n; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(b, Comparator.reverseOrder()); // B 는 내림차순 정렬

        // 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
        for (int i = 0; i < k; i++) {
            // A의 원소가 B의 원소보다 작은 경우
            if (a[i] < b[i]) {
                // 두 원소를 교체
                int temp = a[i];
                a[i] = b[i];
                b[i] = temp;
            }
            // A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
            else
                break;
        }

        // 배열 A 의 총합 계산 후 출력
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += a[i];
        }
        System.out.println(sum);
    }
}
