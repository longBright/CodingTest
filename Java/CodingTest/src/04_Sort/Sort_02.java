import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

// Student 클래스 선언
// 정렬을 위해 Comparable 인터페이스를 구현
class Student implements Comparable<Student> {
    private String name;
    private int score;

    public Student(String name, int score) {
        this.name = name;
        this.score = score;
    }

    // Getter 메소드
    public String getName() {
        return this.name;
    }

    public int getScore() {
        return this.score;
    }

    // comparTo 메소드 재정의
    @Override
    public int compareTo(Student other) {
        if (this.score < other.score) {
            return -1;
        }
        return 1;
    }
}

// 성적이 낮은 순서로 학생 출력하기
public class Sort_02 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 학생 수 입력
        int n = Integer.parseInt(br.readLine());

        // 학생 리스트 입력 및 생성
        List<Student> students = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String name = st.nextToken();
            int score = Integer.parseInt(st.nextToken());
            students.add(new Student(name, score));
        }

        // 학생 리스트 정렬
        Collections.sort(students);

        // 성적 낮은 순으로 학생 이름 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < students.size(); i++) {
            sb.append(students.get(i).getName()).append(" ");
        }
        System.out.println(sb);
    }
}
