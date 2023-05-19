import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Baekjoon_10807 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int count = sc.nextInt();
        List<Integer> a = new ArrayList<>();
        for(int i=0; i<count; i++){
            a.add(sc.nextInt());
        }
        int same = sc.nextInt();
        int sameCount=0;
        for(int i : a){
            if(i == same){
                sameCount++;
            }
        }
        System.out.println(sameCount);
    }
}
