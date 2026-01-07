//Check if a number is a palindrome.

//import java.util.Scanner;

import java.util.Scanner;

public class Czech {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); // 545 --> 545
        int num = sc.nextInt();
        
        int originalNum = num;

        String revNum = "";

        while( num > 0 ){
            revNum += String.valueOf(num % 10);
            num /= 10;
        }

        if( Integer.parseInt(revNum) == originalNum){
            System.out.println("Palindrome");
        }else{
            System.out.println("Not a Palindrome!");
        }

        sc.close();
    }
}
