import java.util.Scanner;

public class Baekjoon_10813 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] basket = new int[n];
        for(int i=0; i<n; i++){
            basket[i] = i+1;
        }
        for(int i=0; i<m; i++){
            int j = sc.nextInt();
            int k = sc.nextInt();
            int num = basket[j-1];
            basket[j-1] = basket[k-1];
            basket[k-1] = num;
        }
        for(int i=0; i<basket.length; i++){
            System.out.printf(String.valueOf(basket[i]));
            if(i+1 != basket.length){
                System.out.printf(" ");
            }
        }
    }
}
