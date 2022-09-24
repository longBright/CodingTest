import java.util.Scanner;

public class Prob_2675 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int r = sc.nextInt();
            String s = sc.nextLine();
            String p = "";

            for (char c: s.toCharArray()) {
                for (int j = 0; j < r; j++) {
                    p += c;
                }
            }
            System.out.println(p.trim());
        }
        sc.close();
    }
}
