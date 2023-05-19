import java.util.Scanner;

public class Baekjoon_2525 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int time = sc.nextInt();
        int min = sc.nextInt();
        int plus = sc.nextInt();
        int endt =(time+(min+plus)/60)%24;
        int endm = (min+plus) % 60;

        System.out.printf(endt + " " + endm);
    }
}
