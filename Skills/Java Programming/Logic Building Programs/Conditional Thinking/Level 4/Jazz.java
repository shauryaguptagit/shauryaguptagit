// Take a password string and check basic rules (length ≥ 8 and contains at least one digit).
// need looping for full implementation

import java.util.Scanner;

public class Jazz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter password: ");
        String pass = sc.nextLine();

        if (pass.length() >= 8 ){
            System.out.println("Valid");
        } else {
            System.out.println("Not Valid");
        }



        sc.close();
    }
}
