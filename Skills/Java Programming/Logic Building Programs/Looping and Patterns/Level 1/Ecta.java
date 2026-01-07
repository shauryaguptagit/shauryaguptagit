//Print the table of a given number (n × 1 to n × 10). 

import java.util.Scanner;

public class Ecta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number table: ");
        int tableNumber = sc.nextInt();
        for(int i = 1; i < 11; i++){
            System.out.println("" + tableNumber + " X " + i + " = " + (tableNumber*i));
        }
        sc.close();
    }
}
