//Print first n terms of an arithmetic progression (a, d).


import java.util.Scanner;

public class Icicle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the first term (a): ");
        int a = sc.nextInt();
        
        System.out.println("Enter the common difference (d): ");
        int d = sc.nextInt();
        
        System.out.println("Enter the number of terms (n): ");
        int n = sc.nextInt();

        int currentTerm = a;

        for(int i = 1; i<= n; i++){
            System.out.println(currentTerm + " ");
            currentTerm += d;
        }
        System.out.println();
        sc.close();
    }
}
