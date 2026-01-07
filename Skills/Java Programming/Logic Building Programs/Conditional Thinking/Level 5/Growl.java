//Take a 3-digit number and check if the sum of the first and last digit equals the middle digit.
import java.util.Scanner;

public class Growl {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a three digit number: ");
        int threeDigitNum = sc.nextInt(); // 354

        int firstDigit = threeDigitNum / 100;
        int lastDigit = threeDigitNum % 10;
        int middleDigit = (threeDigitNum/10) % 10;
        
        if ( middleDigit == firstDigit + lastDigit ){
            System.out.println("Yes, the sum of the first and last digit equals the middle digit.");
        } else{
            System.out.println("No, the sum of the first and last digit does not equal the middle digit.");
        }
        sc.close();
    }
}
