import java.util.Scanner;

public class Try {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a string:");
        String s = sc.nextLine();
        System.out.println("You entered string: "+ s);
        System.out.println("Enter an integer:");
        int x = sc.nextInt();
        System.out.println("You entered Integer " + x);
        System.out.println("Enter a float:");
        float f = sc.nextFloat();
        System.out.println("You entered Float " + f);
        sc.close();
    }
}
