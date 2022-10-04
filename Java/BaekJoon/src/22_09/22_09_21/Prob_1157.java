import java.util.Scanner;

public class Prob_1157 {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        str = str.toUpperCase();

        int[] arr = new int [26];

        for (int i = 0; i < str.length(); i++) {
            // 대문자인 경우
            if ('A' <= str.charAt(i) && str.charAt(i) <= 'Z') {
                arr[str.charAt(i) - 'A']++;
            }
            // 소문자인 경우
            else {
                arr[str.charAt(i) - 'a']++;
            }
        }

        int max = -1;
        char result = '?';
        for (int i = 0; i < 26; i++) {
            if (arr[i] > max) {
                max = arr[i];
                result = (char) (i + 65);
            }
            else if (arr[i] == max) {
                result = '?';
            }
        }
        System.out.println(result);
        in.close();
    }
}
