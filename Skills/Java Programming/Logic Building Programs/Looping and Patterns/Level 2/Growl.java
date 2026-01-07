//Print all prime numbers between 1 and 100.

//import java.util.Scanner;

public class Growl {
    public static void main(String[] args) {
        System.out.println("Prime numbers between 1 and 100:");

        for ( int i = 1; i <= 100; i++){ //67

            boolean isPrime = true;

            if (i <= 1){
                isPrime = false;
            } else if( i > 2 && i % 2 == 0) {
                isPrime = false;
            } else if( i > 2) {
                for ( int n = 3; n <= Math.sqrt(i); n+= 2){
                    if (i % n == 0){
                        isPrime = false;
                        break;
                    }
                }
            }
            if (isPrime){
                System.out.println(i + " ");
            }
        }
        System.out.println();
    }
}
