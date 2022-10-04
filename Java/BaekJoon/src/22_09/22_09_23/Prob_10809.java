import java.util.Scanner;

public class Prob_10809 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int[] result = new int[26];

        for (int i = 0; i < result.length; i++) {
            result[i] = -1;
        }

        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            if (result[idx] == -1) {
                result[idx] = i;
            }
        }

        for (int i: result) {
            System.out.print(i + " ");
        }
        sc.close();
    }
}
