//Take two numbers and determine whether both are even, both are odd, or one is even and one is odd.
import java.util.Scanner;

public class Growl {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first number: ");
        int num1 = sc.nextInt();
        System.out.println("Enter second number: ");
        int num2 = sc.nextInt();

        if (num1 % 2 == 0 && num2 % 2 == 0){
            System.out.println("Both are Even!");
        }else if(num1 % 2 != 0 && num2 % 2 != 0){
            System.out.println("Both are Odd!");
        }else{
            System.out.println("One is odd and One is even!");
        }
        sc.close();
    }
}
