//Take a character and check if it is a letter, a digit, or neither.

import java.util.Scanner;

public class Asset{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a character: ");
        char ch = sc.next().charAt(0);

        if(Character.isAlphabetic(ch)){
            System.out.println("Alphabet!");
        }else if(Character.isDigit(ch)){
            System.out.println("Digit!");
        }else{
            System.out.println("Neither!");
        }
        sc.close();
    }
}