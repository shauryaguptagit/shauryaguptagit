//Take 5 numbers as input. If the user enters 0, skip it using continue. At the end, print the sum of all non-zero numbers entered. 

import java.util.Scanner;

public class Jazz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = 0;
        int sumNonZero = 0;

        for (int i = 1; i <= 5; i++){
            System.out.println("Enter the number: ");
            a = sc.nextInt(); 
            if (a == 0){
                continue;
            } else{
                sumNonZero += a;
            }
        }
        System.out.println("The sum of all non Zero Numbers entered is " + sumNonZero);
        sc.close();
    }
}
