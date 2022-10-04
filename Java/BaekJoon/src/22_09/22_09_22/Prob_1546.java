import java.util.Arrays;
import java.util.Scanner;

// 22.09.22 백준 1546번
// 평균
public class Prob_1546 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        double[] arr = new double[n];

        for(int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        System.out.println(arr[n-1]);

        double m = arr[n-1];
        double sum = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = arr[i] / m * 100;
            sum += arr[i];
            System.out.println(arr[i]);
        }
        double avg = sum / n;
        System.out.println(avg);
        sc.close();
    }
}
