import java.util.Scanner;

public class Baekjoon_25314 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        for(int i =0; i<size/4; i++){
            System.out.printf("long ");
        }
        System.out.println("int");
    }
}
