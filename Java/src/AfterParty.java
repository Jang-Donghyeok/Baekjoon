import java.util.Scanner;

public class AfterParty {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String[] A = sc.nextLine().split(" ");
        String[] B = sc.nextLine().split(" ");
        int[] result = new int[B.length];
        int sum = Integer.parseInt(A[0])*Integer.parseInt(A[1]);
        for(int i=0; i<B.length; i++){
            result[i] = Integer.parseInt(B[i])-sum;
        }
        for(int i=0; i<B.length; i++){
            System.out.print(result[i]);
            if(i != B.length){
                System.out.print(" ");
            }
        }
    }
}
