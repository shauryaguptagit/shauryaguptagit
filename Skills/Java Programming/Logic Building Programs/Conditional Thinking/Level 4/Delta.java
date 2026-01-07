//Take 24-hour time (hours and minutes) and print whether it is AM or PM. 00:00 AM 12:00 PM

import java.util.Scanner;

public class Delta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter an hour: ");
        int hour = sc.nextInt();
        System.out.println("Enter the minutes: ");
        // int min = sc.nextInt();

        if (hour >= 0 && hour <= 11){
            System.out.println("It is AM");
        }else{
            System.out.println("PM");
        }

        sc.close();
    }
}
