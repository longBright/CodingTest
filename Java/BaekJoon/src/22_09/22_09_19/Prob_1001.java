import java.util.Scanner;

// 22.09.19 백준 1001번
// A + B
public class Prob_1001 {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);

        int A = in.nextInt();
        int B = in.nextInt();

        System.out.println(A-B);
        in.close();
    }
}
