//Take a year and print the corresponding century (e.g., “19th century”, “20th century”)

import java.util.Scanner;

public class Jazz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter year: ");
        int year = sc.nextInt();

        if ( year%100 == 0 ){
            System.out.println("Century is " + year/100);
        }else{
            System.out.println("Century is " + ((year/100) + 1) );

        }
        sc.close();
    }
}
