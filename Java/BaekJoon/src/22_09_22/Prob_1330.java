import java.util.Scanner;

// 22.09.22 백준 1330번
// 두 수 비교하기
public class Prob_1330 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        
        if (a > b) {
            System.out.println(">");
        }
        else if (a < b) {
            System.out.println("<");
        }
        else {
            System.out.println("==");
        }
        sc.close();
    }
}
