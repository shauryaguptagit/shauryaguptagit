//Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither. 

import java.util.Scanner;

public class Bash {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter three-digit number: ");
        int threeDigitNum = sc.nextInt();

        int lastDigit = threeDigitNum % 10; // 4
        int middleDigit = (threeDigitNum/10) % 10; // 2
        int firstDigit = (threeDigitNum/100) % 10;// 1

        if (middleDigit >= firstDigit && middleDigit >= lastDigit){
            System.out.println("Largest");
        }else if(middleDigit <= firstDigit && middleDigit <= lastDigit){
            System.out.println("Smallest");
        }else{
            System.out.println("Neither");
        }
        sc.close();
    }    
}
