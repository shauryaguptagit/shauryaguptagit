//Take a month number (1–12) and print the number of days in that month (ignore leap years). 

import java.util.Scanner;

public class Jazz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a month number: ");
        int monthNum = sc.nextInt();

        if(monthNum > 12 || monthNum < 1){
            System.out.println("Invalid Input");
        }else if(monthNum == 2){
            System.out.println("28 Days");
        }else if(monthNum == 4 || monthNum == 6 || monthNum == 9 || monthNum == 11){
            System.out.println("30 Days");
        }else{
            System.out.println("31 Days");
        } 
        sc.close();
    }
}
