/* 2021 DevMatching 상반기 웹 백엔드 개발자 */
/* 로또의 최고 순위와 최저 순위 */
public class Dev_01 {
    public static void main(String[] args) {
        int[] lottos = {44, 1, 0, 0, 31, 25};
        int[] win_nums = {31, 10, 45, 1, 6, 19};
        int[] answer = solution(lottos, win_nums);
        System.out.println(answer[0] + " " + answer[1]);
    }

    // public static int[] solution(int[] lottos, int[] win_nums) {
    //     int[] answer = new int[2];
    //     int[] score = {6, 6, 5, 4, 3, 2, 1};
    //     int max = 0;
    //     int min = 0;
    //     for (int i = 0; i < lottos.length; i++) {
    //         if (lottos[i] == 0) max++;
    //         for (int j = 0; j < win_nums.length; j++) {
    //             if (lottos[i] == win_nums[j]) {
    //                 max++;
    //                 min++;
    //             } 
    //         }
    //     }
    //     answer[0] = score[max];
    //     answer[1] = score[min];
    //     return answer;
    // }

    public static int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int max = 0;
        int min = 0;

        for (int i = 0; i < lottos.length; i++) {
            if (lottos[i] == 0) max++;
            for (int j = 0; j < win_nums.length; j++) {
                if (lottos[i] == win_nums[j]) {
                    max++;
                    min++;
                } 
            }
        }
        answer[0] = getScore(max);
        answer[1] = getScore(min);
        return answer;
    }

    public static int getScore(int num) {
        switch(num) {
            case 6:
                return 1;
            case 5:
                return 2;
            case 4:
                return 3;
            case 3:
                return 4;
            case 2:
                return 5;
            default:
                return 6;
        }
    }
}
