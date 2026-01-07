//Check if a number is a strong number (sum of factorials of digits = number).

// 123 = 1! + 2! + 3!

import java.util.Scanner;

public class Hector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); //112
        int num = sc.nextInt();
        
        int originalNum = num;
        int sumOfFactorials = 0;
        int tempNum = num; // Use a temp variable!

        while (tempNum > 0) {
            int digit = tempNum % 10;
            int factorial = 1;
            for (int i = 1; i <=digit; i++){
                factorial = factorial * i; 
            }
            sumOfFactorials += factorial;
            tempNum /= 10;
        }

        if (originalNum == sumOfFactorials && originalNum != 0){
            System.out.println("Strong");
        }else{
            System.out.println("Not Strong");

        }

        sc.close();
    }
}
