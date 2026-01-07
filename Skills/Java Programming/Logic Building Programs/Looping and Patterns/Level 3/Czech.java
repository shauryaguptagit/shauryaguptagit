//Print all numbers between a and b divisible by 7.

//import java.util.Scanner;

import java.util.Scanner;

public class Czech {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: "); 
        int a = sc.nextInt(); // 10
        System.out.println("Enter b number: "); 
        int b = sc.nextInt(); // 15
        
        int c = Math.max(a, b);
        int d = Math.min(a, b);
        for (int i = d; i <= c; i++){
            if ( i % 7 == 0){
                System.out.print(i);
            }
        }

        sc.close();
    }
}
