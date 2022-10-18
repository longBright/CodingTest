import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BinarySearch {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int n = Integer.parseInt(st.nextToken());
        int target = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 재귀함수 이진 탐색 결과 출력
        printResult(recusiveBinarySearch(arr, target, 0, n-1));

        // 반복문 이진 탐색 결과 출력
        printResult(loopBinarySearch(arr, target, 0, n-1));
    }

    // 재귀함수 이용
    public static int recusiveBinarySearch(int[] arr, int target, int start, int end) {
        // 종료 조건(없는 경우)
        if (start > end) {
            return -1;
        }
        int mid = (int)((start + end) / 2);
        // 찾은 경우 중간점 인덱스 반환
        if (arr[mid] == target) {
            return mid;
        }
        // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 탐색
        else if (arr[mid] > target) {
            return recusiveBinarySearch(arr, target, start, mid-1);
        }
        // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 탐색
        else {
            return recusiveBinarySearch(arr, target, mid+1, end);
        }
    }
    
    // 반복문 이용
    public static int loopBinarySearch(int[] arr, int target, int start, int end) {
        while (start <= end) {
            int mid = (int)((start + end) / 2);
            // 찾은 경우 중간점 인덱스 반환
            if (arr[mid] == target) {
                return mid;
            }
            // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 탐색
            else if (arr[mid] > target) {
                end = mid - 1;
            }
            // 중감점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 탐색
            else {
                start = mid + 1;
            }
        }
        return -1;
    }

    // 출력 메소드
    public static void printResult(int result) {
        if (result == -1) {
            System.out.println("해당 원소가 존재하지 않음");
        }
        else {
            System.out.printf("위치 : %d\n", result+1);
        }
    }
}
