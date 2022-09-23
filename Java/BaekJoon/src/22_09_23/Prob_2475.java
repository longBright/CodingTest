import java.util.Scanner;

// 22.09.23 백준 2475번
// 검증수
public class Prob_2475 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int[] arr = new int[5];
        int result = 0;
        for (int i = 0; i < 5; i++) {
            arr[i] = sc.nextInt();
            result += arr[i] * arr[i];
        }
        result %= 10;
        System.out.println(result);
        sc.close();
    }
}
