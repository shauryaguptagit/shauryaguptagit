//Find HCF (GCD) of two numbers using loops. 12 16 


import java.util.Scanner;

public class Delta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter first number: ");
        int numOne = sc.nextInt(); // 12
        System.out.println("Enter second number: ");
        int numTwo = sc.nextInt(); // 16
        
        int HCF = 1;
        int c = Math.max(numTwo, numOne);
        int d = Math.min(numTwo, numOne);

        for ( int i = 1; i <=d; i++){ // 1,2,3,4.....12
            if (c % i == 0 && d % i == 0 ){
                HCF = i;
            }
        }

        System.out.println(HCF);

        sc.close();
    }
}
