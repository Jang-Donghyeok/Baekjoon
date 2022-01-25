import java.math.BigInteger;
import java.util.Scanner;

import static java.math.BigInteger.valueOf;

class Julka{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BigInteger Apple = new BigInteger(sc.nextLine());
        BigInteger Gap = new BigInteger(sc.nextLine());

        System.out.println((Apple.subtract(Gap)).divide(valueOf(2)).add(Gap)); // ((Apple - Gap) / 2) + Gap
        System.out.println((Apple.subtract(Gap)).divide(valueOf(2))); // (Apple - Gap) / 2
    }
}