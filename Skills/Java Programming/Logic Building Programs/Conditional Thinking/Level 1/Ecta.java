//Check if a given year is a leap year.
/*
 * LEAP YEAR
 * %4 == 0 and %100 != 0
 * %400 == 0
 */

import java.util.Scanner;

public class Ecta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the year: ");
        int yearValue = sc.nextInt();
        if(yearValue % 4 == 0 && yearValue % 100 !=0){
            System.out.println("Leap Year!");
        }else if(yearValue % 400 == 0){
            System.out.println("Leap Year!");
        }else{
            System.out.println("Not a Leap Year!");
        }
        sc.close();
    }
}
