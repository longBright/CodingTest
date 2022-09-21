import java.util.Scanner;

// 22.09.21 백준 1152번
// 단어의 개수
public class Prob_1152 {
    public static void main(String[] args) throws Exception {
        Scanner in = new Scanner(System.in);
        {
            String str = in.nextLine().trim();
            if (str.isEmpty()) {
                System.out.println(0);
            } else {
                System.out.println(str.split(" ").length);
            }
        }
        in.close();
    }
}