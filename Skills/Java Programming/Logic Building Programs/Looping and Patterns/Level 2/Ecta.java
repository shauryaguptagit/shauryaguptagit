//Check if a number is an Armstrong number.

import java.util.Scanner;

public class Ecta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: "); //1622
        int num = sc.nextInt();

        int originalNum = num;
        int newSum = 0;
        int order = 0;



        int tempNum = num;
        if( tempNum == 0){
            order = 1;
        }else{
            while( tempNum > 0 ){
                tempNum /=10;
                order++;
            }
        }
        
        tempNum = num;

        while( tempNum > 0){
            int digit = tempNum % 10;
            newSum += (long)Math.pow(digit,order);
            tempNum /= 10;
        }

        if ( newSum == originalNum){
            System.out.println("armstrong no.");
        }else{
            System.out.println("not an armstrong no.");

        }

        sc.close();
    }
}
