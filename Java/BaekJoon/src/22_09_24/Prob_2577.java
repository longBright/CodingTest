import java.util.Scanner;

public class Prob_2577 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        String result = Integer.toString(a * b * c);
        int[] arr = new int[10];

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < result.length(); j++) {
                if (Character.forDigit(i, 10) == result.charAt(j)) {
                    arr[result.charAt(j) - '0']++;
                }
            }
        }

        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }
        sc.close();
    }
}
