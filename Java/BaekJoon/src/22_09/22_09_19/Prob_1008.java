import java.util.Scanner;

// 22.09.19 백준 1008번
// A - B
public class Prob_1008 {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);

        // Double A = Double.valueOf(in.nextInt());
        // Double B = Double.valueOf(in.nextInt());

        int A = in.nextInt();
        int B = in.nextInt();

        System.out.println((double) A/B);
        in.close();
    }
}
