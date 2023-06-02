import java.io.*;

public class Baekjoon_2444 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        int max = 2 * n -1;
        int cStart;
        for(int i=0; i<=max/2; i++){
            cStart = (2*i)+1;
            for (int j=0; j<(max-cStart)/2; j++) {
                bw.write(' ');
            }
            for(int k=0; k<cStart; k++){
                bw.write('*');
            }
            bw.write('\n');
        }
        for(int i=max/2-1; i>=0; i--){
            cStart = (2*i)+1;
            for (int j=0; j<(max-cStart)/2; j++) {
                bw.write(' ');
            }
            for(int k=0; k<cStart; k++){
                bw.write('*');
            }
            if(i !=0) {
                bw.write('\n');
            }
        }
        bw.flush();
    }
}
