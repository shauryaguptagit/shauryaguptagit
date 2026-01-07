//Take day and month and check if it forms a valid calendar date (ignoring leap years).

import java.util.Scanner;

public class Czech {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter day: ");
        int days = sc.nextInt();
        System.out.println("Enter month: "); 
        int month = sc.nextInt();
        
        
        if (month < 1 || month >12 || days < 1 ){
            System.out.println("Not Valid!");
        }else if (month == 2){
            if (days < 29){
                System.out.println("Valid!");
            }else{
                System.out.println("Not Valid!");
            }
        } else if(month == 4 || month == 6 || month == 9 || month == 11){
            if (days < 31) {
                System.out.println("Valid!");
            }else{
                System.out.println("Not Valid!");
            }
        } else{
            if (days < 32) {
                System.out.println("Valid!");
            }else{
                System.out.println("Not Valid!");
            }

        }
        sc.close();
    }
}
