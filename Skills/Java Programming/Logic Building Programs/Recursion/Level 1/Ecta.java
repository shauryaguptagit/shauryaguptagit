//Print sum of first n natural numbers recursively.


import java.util.Scanner;

public class Ecta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the term: ");
        int n = sc.nextInt();
        System.out.println("sum of first " + n + " natural numbers");
        int sumNat = sumNatNums(n);
        System.out.println(sumNat);

        sc.close();
    }
    public static int sumNatNums(int n){
        if (n <= 0) {
            return 0;
        }
        return n +sumNatNums(n - 1);
    }
}
