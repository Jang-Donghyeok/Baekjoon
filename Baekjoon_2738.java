import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Baekjoon_2738 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] a = new int[n][m];
        int[][] b = new int[n][m];
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                a[i][j] = sc.nextInt();
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                b[i][j] = a[i][j] + sc.nextInt();
            }
        }
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
               sb.append(b[i][j]).append(" ");
            }
            if(i !=n-1){
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }
}
