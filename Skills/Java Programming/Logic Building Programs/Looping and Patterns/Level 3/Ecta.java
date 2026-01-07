//Find LCM of two numbers using loops. 4,6 --> 12  50 300

import java.util.Scanner;

public class Ecta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first number: ");
        int a = sc.nextInt(); // 4
        System.out.println("Enter second number: ");
        int b = sc.nextInt(); // 6
        
        if ( a == 0 || b == 0){
            System.out.println(0);
        } else {
            int max = Math.max(a, b);
            int min = Math.min(a, b);

            int lcm = max;

            while(true){
                if (lcm % min == 0){
                    System.out.println(lcm);
                    break;
                }
                lcm +=max;
            }


        }



        sc.close();
    }
}
