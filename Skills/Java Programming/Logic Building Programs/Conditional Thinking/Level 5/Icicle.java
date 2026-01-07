//Take two dates (day and month) and determine which one comes first in the calendar. 

import java.util.Scanner;

public class Icicle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter days for date 1: ");
        int days1 = sc.nextInt();
        System.out.println("Enter month for date 1: ");
        int month1 = sc.nextInt();
        System.out.println("Enter days for date 2: ");
        int days2 = sc.nextInt();
        System.out.println("Enter month for date 2: ");
        int month2 = sc.nextInt();

        if (month1 < 1 || month2 < 1 || days1 < 1 || days2 < 1 || month1 > 12 || month2 > 12 || days1 > 31 || days2 > 31 ){
            System.out.println("Not a valid date!");
        } else if (month1 > month2){
            System.out.println("Date 2 is earlier in calendar!");
        } else if (month2 > month1){
            System.out.println("Date 1 is earlier in calendar!");
        } else if(month1 == month2){
            if(days1 > days2){
            System.out.println("Date 2 is earlier in calendar!");
            }else if(days2 > days1){
            System.out.println("Date 1 is earlier in calendar!");
            }else{
            System.out.println("Both are same date in calendar!");
            }
        }
        sc.close();
    }
}
