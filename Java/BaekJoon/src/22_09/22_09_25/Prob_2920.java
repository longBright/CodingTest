import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Prob_2920 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[8];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        br.close();

        boolean asc = true;
        boolean dsc = true;
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] < arr[i+1]) {
                dsc = false;
            }
            else if (arr[i] > arr[i+1]) {
                asc = false;
            }
        }

        if (asc) {
            System.out.println("ascending");
        }
        else if (dsc) {
            System.out.println("descending");
        }
        else {
            System.out.println("mixed");
        }
    }
}
