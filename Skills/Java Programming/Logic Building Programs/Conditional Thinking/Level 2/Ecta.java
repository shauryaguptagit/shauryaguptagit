//Take the hour of the day (0–23) and print “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night”. 

import java.util.Scanner;

public class Ecta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the hour: ");
        int hour = sc.nextInt();
        if(hour>= 5 && hour <=11){
            System.out.println("Good Morning!");
        }else if(hour>=12 && hour<=16){
            System.out.println("Good Afternoon!");
        }else if(hour>=17 && hour<=20){
            System.out.println("Good Evening!");
        }else{
            System.out.println("Good Night!");
        }
        sc.close();
    }
}
