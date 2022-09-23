import java.util.Scanner;

// 구구단
public class Prob_2739 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 1; i <= 9; i++) {
            System.out.printf("%d * %d = %d\n", n, i, n*i);
        }
        sc.close();
    }
}
