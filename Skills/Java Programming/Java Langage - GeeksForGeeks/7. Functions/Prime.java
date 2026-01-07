import java.util.Scanner;

public class Prime {

    // The main method MUST be static to be the program's entry point.
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number to find its prime factors: ");
        int n = sc.nextInt();
        
        System.out.print("Prime factors of " + n + " are: ");
        printPrimeFactors(n);
        
        sc.close();
    }

    /**
     * Prints the prime factors of a given number n.
     * This is an efficient implementation using trial division.
     * @param n The number to be factorized.
     */
    public static void printPrimeFactors(int n) {
        // Handle the case of the number being 0, 1, or negative.
        if (n <= 1) {
            System.out.println("No prime factors.");
            return;
        }

        // First, handle all factors of 2.
        while (n % 2 == 0) {
            System.out.print(2 + " ");
            n /= 2; // Divide n by 2
        }

        // Next, check for odd factors starting from 3 up to sqrt(n).
        // We can increment by 2 because we've already handled all even factors.
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            while (n % i == 0) {
                System.out.print(i + " ");
                n /= i; // Divide n by the found factor
            }
        }

        // This condition handles the case where n is a prime number
        // greater than 2 (e.g., if the original input was 13, or if n is
        // the last remaining prime factor).
        if (n > 2) {
            System.out.print(n);
        }
        
        System.out.println(); // For clean output
    }
}