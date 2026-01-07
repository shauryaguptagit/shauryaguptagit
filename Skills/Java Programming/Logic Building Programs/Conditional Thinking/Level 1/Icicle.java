//Take a character and check if it’s a vowel or consonant. 

import java.util.Scanner;

public class Icicle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a character: ");
        char alphabet = sc.next().charAt(0); //New Info on how to read characters!
        char ch = Character.toLowerCase(alphabet);
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ){
            System.out.println("Vowel!");
        }else{
            System.out.println("Consonant!");
        }

        sc.close();
    }
}
