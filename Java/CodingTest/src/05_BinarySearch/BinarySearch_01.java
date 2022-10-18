import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 부품 찾기
public class BinarySearch_01 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // N 과 N 개의 부품 입력
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int[] items = new int[n];
        for (int i = 0; i < n; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }
        // items 정렬
        Arrays.sort(items);

        // M 입력
        int m = Integer.parseInt(br.readLine());
        // M 개의 부품 입력과 동시에 이진 탐색 수행
        st = new StringTokenizer(br.readLine(), " ");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            int target = Integer.parseInt(st.nextToken());
            // 찾으면 "yes" 찾지 못하면 "no" 를 StringBuilder 에 추가
            if (binarySearch(items, target, 0, n-1) == -1) {
                sb.append("no").append(" ");
            }
            else {
                sb.append("yes").append(" ");
            }
        }
        System.out.println(sb);
    }
    
    // 이진 탐색 메소드
    public static int binarySearch(int[] arr, int target, int start, int end) {
        while (start <= end) {
            int mid = (int)((start + end) / 2);
            // 중간점의 값이 찾고자 하는 값과 같을 경우 중간점의 인덱스 반환
            if (arr[mid] == target) {
                return mid;
            }
            // 좌측 탐색
            else if (arr[mid] > target) {
                end = mid - 1;
            }
            // 우측 탐색
            else {
                start = mid + 1;
            }
        }
        // 못찾을 경우 -1 반환
        return -1;
    }
}
