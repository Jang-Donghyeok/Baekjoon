import java.util.Scanner;

public class Baekjoon_5597 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] work = new int[30];
        for(int i=0; i<28; i++){
            int n = sc.nextInt();
            work[n-1] = n;
        }
        for (int i=0; i<30; i++){
            if(work[i] ==0){
                System.out.println(i+1);
            }
        }
    }
}
