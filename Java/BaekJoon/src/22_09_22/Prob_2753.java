import java.util.Scanner;

// 22.09.22 백준 2753번
// 윤년
public class Prob_2753 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int year = sc.nextInt();

        if (year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)) System.out.println(1);
        else System.out.println(0);
        sc.close();
    }
}
