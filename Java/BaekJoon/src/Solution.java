import java.util.Arrays;

public class Solution {
    public String solution(String[] registered_list, String new_id) {
        String answer = "";

        while (Arrays.asList(registered_list).contains(new_id)) {

            String N = new_id.replaceAll("[^0-9]", "");
            String S = new_id.replaceAll("[0-9]", "");
            if (N.length() == 0) {
                N = "1";
            }
            // 정상적인 경우
            else {
                N = String.valueOf(Integer.parseInt(N) + 1);
            }
            new_id = S + N;
        }
        answer = new_id;
        return answer;
    }
}
