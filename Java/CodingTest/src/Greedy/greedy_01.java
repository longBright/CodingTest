import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

// 동전 거스름돈 문제
public class greedy_01 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] coins = {500, 100, 50, 10};
        int N = Integer.parseInt(br.readLine());
        int answer = 0;
        for (int coin: coins) {
            answer += N / coin;
            N %= coin;
        }
        System.out.println(answer);
    }
}
