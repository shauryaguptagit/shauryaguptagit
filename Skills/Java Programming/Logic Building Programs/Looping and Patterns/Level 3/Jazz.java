//Print first n terms of a geometric progression (a, r). 

import java.util.Scanner;

public class Jazz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the first term (a): ");
        long a = sc.nextLong(); // Use long for large numbers
        
        System.out.println("Enter the common ratio (r): ");
        long r = sc.nextLong();
        
        System.out.println("Enter the number of terms (n): ");
        int n = sc.nextInt();

        long currentTerm = a;

        System.out.println("The first " + n + " terms of the GP are:");

        for (int i = 1; i <= n; i++) {
          
            System.out.print(currentTerm + " ");
            

            currentTerm *= r; 
        }
        
        System.out.println();
        sc.close();
    }
}
