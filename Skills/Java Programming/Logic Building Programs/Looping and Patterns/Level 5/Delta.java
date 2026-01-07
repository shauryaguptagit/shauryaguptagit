//Print numbers between 1–100 whose digits add up to a multiple of 3


//import java.util.Scanner;

public class Delta {
    public static void main(String[] args) {
        
        for (int i = 1; i <= 100; i++){
            int sumOfDigits = 0;
            int tempNum = i;

            while (tempNum > 0) {
                sumOfDigits += (tempNum % 10);
                tempNum /= 10;
            }

            if (sumOfDigits % 3 == 0){
                System.out.print(i + " ");
            }
        }
        
    }
}
