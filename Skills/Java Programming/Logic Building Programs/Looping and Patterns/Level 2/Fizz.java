//Check if a number is a perfect number.

import java.util.Scanner;

public class Fizz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); //100
        int num = sc.nextInt();

        if (num<=1){
            System.out.println("It is NOT a Perfect Number");
        } else {
            int sumOfDivisors = 0;

            for( int i = 1; i <= num / 2; i++){
                if (num % i == 0){
                    sumOfDivisors += i;
                }
            }
            if (sumOfDivisors == num){
                System.out.println("It is a Perfect Number");
            }else{
                System.out.println("It is not a Perfect Number");

            }
        }
        
        
        sc.close();
    }
}
