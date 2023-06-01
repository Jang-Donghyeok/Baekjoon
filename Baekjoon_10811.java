import java.util.ArrayList;
import java.util.Scanner;

public class Baekjoon_10811 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] basket = new int[n];
        int temp;
        for(int i=0; i<n; i++){
            basket[i] = i+1;
        }
        for(int i=0; i<m; i++){
            int start = sc.nextInt();
            int end = sc.nextInt();
            for(int j=start-1; j<=end-1; j++, end--){
                temp = basket[j];
                basket[j] = basket[end-1];
                basket[end-1] = temp;
            }
        }
        for(int i=0; i<basket.length; i++){
            System.out.printf(String.valueOf(basket[i]));
            if(i+1 != basket.length){
                System.out.printf(" ");
            }
        }
    }
}
