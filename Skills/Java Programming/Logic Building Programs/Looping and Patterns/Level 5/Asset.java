//Print all numbers whose sum of digits is even (1–100).


//import java.util.Scanner;

public class Asset{
    public static void main(String[] args){
       
        for (int i = 1; i <= 100; i++){
            int sumOfDigits = 0;
            int tempNum = i;

            while (tempNum > 0) {
                sumOfDigits += (tempNum % 10);
                tempNum /= 10;
            }

            if (sumOfDigits % 2 == 0) {
                System.out.println(i);
            }
        }
    }
}