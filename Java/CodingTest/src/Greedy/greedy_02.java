import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/* 큰 수의 법칙 */
public class greedy_02 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine(), " ");
        StringTokenizer st2 = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st1.nextToken());
        int M = Integer.parseInt(st1.nextToken());
        int K = Integer.parseInt(st1.nextToken());
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st2.nextToken());
        }
        Arrays.sort(arr);
        int first = arr[N-1];
        int second = arr[N-2];
        int answer = 0;
        while (M != 0) {
            for (int i = 0; i < K; i++) {
                answer += first;
                M--;
            }
            answer += second;
            M--;
        }
        System.out.println(answer);
    }
}
