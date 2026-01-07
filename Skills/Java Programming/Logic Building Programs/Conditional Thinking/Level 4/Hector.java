//Take a weekday number (1–7) and determine if it is a weekday or weekend


import java.util.Scanner;

public class Hector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a weekday number: ");
        int num = sc.nextInt();
        
        if (num > 7 || num < 1 ){
            System.out.println("Invalid");
        }else if(num > 5){
            System.out.println("Weekend");
        }else{
            System.out.println("Weekday");
        }
        sc.close();
    }
}
