//Take a number and print whether it’s positive, negative, or zero.

import java.util.Scanner;

public class Asset{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = sc.nextInt();
        if(num>0){
            System.out.println("Positive!");
        }else if(num<0){
            System.out.println("Negative!");
        }else{
            System.out.println("Zero!");
        }
        sc.close();
    }
}