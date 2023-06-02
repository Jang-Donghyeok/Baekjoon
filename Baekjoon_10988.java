import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon_10988 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int end = s.length();
        for(int i=0; i<end; i++, end--){
            if(!s.substring(i,i+1).equals(s.substring(end-1,end))) {
                System.out.printf("0");
                return;
            }
        }
        System.out.printf("1");
    }
}
