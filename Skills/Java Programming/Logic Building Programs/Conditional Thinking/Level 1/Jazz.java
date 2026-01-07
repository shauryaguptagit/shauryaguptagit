//Take a character and check whether it’s uppercase, lowercase, a digit, or a special character. 

import java.util.Scanner;

public class Jazz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a character: ");
        char ch = sc.next().charAt(0);
        if (Character.isUpperCase(ch)){
            System.out.println("Uppercase");
        }else if(Character.isLowerCase(ch)){
            System.out.println("Lowercase");
        }else if(Character.isDigit(ch)){
            System.out.println("Digit");
        }else{
            System.out.println("Special Character");
        }
        sc.close();
    }
}
