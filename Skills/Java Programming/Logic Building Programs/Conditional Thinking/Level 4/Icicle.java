//Take electricity units consumed and calculate the bill as per slabs (using if-else). 

import java.util.Scanner;

public class Icicle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter units consumed: ");
        int units = sc.nextInt();
        int bill = 0;
        
        if (units <= 100) {
            bill = units * 2;
        } else if (units <= 200) {
            bill = (100 * 2) + ((units - 100) * 3);
        } else if (units <= 300) {
            bill = (100 * 2) + (100 * 3) + ((units - 200) * 4);
        } else {
            bill = (100 * 2) + (100 * 3) + (100 * 4) + ((units - 300) * 5);
        }
        System.out.println("Total Bill: ₹" + bill);
        sc.close();
    }
}
