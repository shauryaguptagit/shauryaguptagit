//Take a 4-digit number and check if the first and last digits are equal.

import java.util.Scanner;

public class Czech {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a four digit number: ");
        int fourDigitNum = sc.nextInt(); // 3214
        
        int firstDigit = (fourDigitNum/1000);
        int lastDigit = fourDigitNum % 10;
        
        if (firstDigit == lastDigit){
            System.out.println("They are Equal");
        }else{
            System.out.println("They are Not Equal");
        }

        sc.close();
    }
}
