import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baekjoon_10798 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[][] text = new String[5][15];
        int max = 0;
        for(int i=0; i<5; i++){
            String s = br.readLine();
            max = max> s.length() ? max : s.length();
            for(int j=0; j<s.length(); j++){
                text[i][j] = s.split("")[j];
            }
        }
        StringBuffer sb = new StringBuffer();
        for(int i=0; i<max; i++){
            for(int j=0; j<5; j++){
                if(text[j][i] !=null){
                    sb.append(text[j][i]);
                }
            }
        }
        System.out.println(sb);
    }
}
