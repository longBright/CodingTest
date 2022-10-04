import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Prob_1259 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        while(true) {
            String num = br.readLine();
            String flippedNum = new StringBuilder(num).reverse().toString();

            if (num.equals("0")) break;

            if (num.equals(flippedNum)) {
                sb.append("yes\n");
            }
            else {
                sb.append("no\n");
            }
        }
        System.out.println(sb);
    }
}
