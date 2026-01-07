//Print all factors of a given number.
//import java.util.Scanner;

import java.util.Scanner;

public class Fizz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number (n): ");
        int n = sc.nextInt();

        System.out.println("Numbers from 1 to " + n + " with an even number of 1s:");

        // --- Outer Loop: Iterates from 1 to n ---
        for (int i = 1; i <= n; i++) {
            
            int oneCount = 0;
            int tempNum = i; // Make a copy of 'i' to destroy

            // --- Inner Loop: Count the 1s in the binary representation ---
            while (tempNum > 0) {
                // Get the last binary digit (0 or 1)
                int binaryDigit = tempNum % 2; 
                
                if (binaryDigit == 1) {
                    oneCount++;
                }
                
                // Remove the last binary digit
                tempNum = tempNum / 2; 
            }
            
            // --- Check: Is the count even? ---
            // We check oneCount > 0 because 0 is even, but 
            // the number 0 itself (not in our 1-n loop) has 0 ones.
            if (oneCount > 0 && oneCount % 2 == 0) {
                System.out.print(i + " ");
            }
        }
        
        System.out.println(); // For a clean new line at the end
        sc.close();

    }
}
