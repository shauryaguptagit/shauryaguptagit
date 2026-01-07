//Take three numbers and print the median value (neither maximum nor minimum).

import java.util.Scanner;

public class Czech {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number one: ");
        int numOne = sc.nextInt(); // 5 6 7
        System.out.println("Enter number two: "); 
        int numTwo = sc.nextInt();
        System.out.println("Enter number three: ");
        int numThree = sc.nextInt();

        if (numOne >= numTwo && numOne >= numThree){
            if(numTwo >= numThree){
                System.out.println(numTwo);
            }else{
                System.out.println(numThree);
            }
        }else if(numTwo >= numOne && numTwo >= numThree){
            if (numOne >= numThree){
            System.out.println(numOne);
            }else{
                System.out.println(numThree);
            }
        }else if(numThree >= numOne && numThree >= numTwo){
            if (numOne >= numTwo){
            System.out.println(numOne);
            }else{
                System.out.println(numTwo);
            }
        }

        sc.close();
    }
}
