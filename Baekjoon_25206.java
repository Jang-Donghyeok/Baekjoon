import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon_25206 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        double total = 0;
        double count = 0;

        for (int i = 0; i < 20; i++) {
            String[] inputs = br.readLine().split(" ");
            double point = Double.parseDouble(inputs[1]);
            String grade = inputs[2];

            switch(grade) {
                case "A+":
                    total += point * 4.5;
                    count += point;
                    break;
                case "A0":
                    total += point * 4.0;
                    count += point;
                    break;
                case "B+":
                    total += point * 3.5;
                    count += point;
                    break;
                case "B0":
                    total += point * 3.0;
                    count += point;
                    break;
                case "C+":
                    total += point * 2.5;
                    count += point;
                    break;
                case "C0":
                    total += point * 2.0;
                    count += point;
                    break;
                case "D+":
                    total += point * 1.5;
                    count += point;
                    break;
                case "D0":
                    total += point * 1.0;
                    count += point;
                    break;
                case "F":
                    count += point;
                    break;
                default:
                    break;
            }
        }

        System.out.println(total / count);
    }
}