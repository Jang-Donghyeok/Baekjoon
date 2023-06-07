import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon_2563 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        boolean[][] color = new boolean[101][101];
        int total=0;
        for(int i=0; i<n; i++){
            String s = br.readLine();
            int x = Integer.parseInt(s.split(" ")[0]);
            int y = Integer.parseInt(s.split(" ")[1]);
            for(int j=x; j<x+10; j++){
                for (int k=y; k<y+10; k++){
                    if(!color[j][k]){
                        color[j][k]= true;
                        total++;
                    }
                }
            }
        }
        System.out.println(total);
    }
}
