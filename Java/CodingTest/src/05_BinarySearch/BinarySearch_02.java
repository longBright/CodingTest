import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 떡볶이 떡 만들기
public class BinarySearch_02 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        // N, M 입력
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 떡의 개별 높이 입력
        st = new StringTokenizer(br.readLine(), " ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        // 이진 탐색을 위한 정렬
        Arrays.sort(arr);

        // 이진 탐색 수행 후 결과 출력
        System.out.println(binarySearch(arr, m, 0, arr[n - 1]));
    }

    public static int binarySearch(int[] arr, int target, int start, int end) {
        int max = 0;
        while (start <= end) {
            int mid = (int) ((start + end) / 2);
            int sum = 0;
            for (int i = 0; i < arr.length; i++) {
                // 떡의 길이가 현재 절단기의 길이보다 길면 남고, 짧으면 남지 않음
                if (arr[i] > mid) {
                    sum += arr[i] - mid;
                }
            }
            // 요청한 떡의 길이보다 적을 경우 왼쪽 탐색(절단기 길이가 너무 긴 경우)
            if (sum < target) {
                end = mid - 1;
            }
            // 요청한 떡의 길이보다 크거나 같을 경우(절단기 길이가 적당한 경우)
            // 최댓값 갱신 후 오른쪽 탐색
            else {
                max = mid;
                start = mid + 1;
            }
        }
        return max;
    }
}
