import java.util.Scanner;
public class Baekjoon_25304 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int total_Price = sc.nextInt();
        int count = sc.nextInt();
        for(int i=0; i<count; i++){
            int pay = sc.nextInt() * sc.nextInt();
            total_Price -= pay;
        }
        if(total_Price ==0){
            System.out.println("Yes");
        }else {
            System.out.println("No");
        }
    }
}
