//Check if a number is a multiple of 7 or ends with 7. 

import java.util.Scanner;

public class Ecta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number: ");
        int num = sc.nextInt();
        int number = Math.abs(num);
        if (number % 7 == 0 || number % 10 == 7){
            System.out.println("number is a multiple of 7 or ends with 7");
        }else{
            System.out.println("number is not a multiple of 7 or ends with 7");
        }
        sc.close();
    }
}
