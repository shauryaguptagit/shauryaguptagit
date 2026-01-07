//Print all numbers that are palindromes between 1–500.

//import java.util.Scanner;

public class Czech {
    public static void main(String[] args) {
        //int count = 0;
        for (int i = 1; i < 501; i++){ // 151 --> 151
            int originalNum = i;
            int reversedNum = 0;
            int tempNum = i;

            while (tempNum > 0){
                int digit = tempNum % 10;
                reversedNum = (reversedNum  * 10) + digit;
                tempNum /= 10;
            }

            if (originalNum == reversedNum){
                System.out.print(originalNum + " ");
            }
        }
        System.out.println();
    }
}
