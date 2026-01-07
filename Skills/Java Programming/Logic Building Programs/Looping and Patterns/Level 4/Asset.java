//Print the squares of numbers from 1 to n.

import java.util.Scanner;

public class Asset{
    public static void main(String[] args){


        // Scanner sc = new Scanner(System.in);
        // System.out.println("Enter which number: "); 
        // int num = sc.nextInt();
        
        // for (int i = 1; i <= num; i++){
        //     System.out.print("*");
        // }

        // Scanner sc = new Scanner(System.in);
        // System.out.println("Enter which number: "); 
        // int num = sc.nextInt();
        
        // for (int i = 1; i <= num; i++){
        //     for(int j = 1; j <= i; j++){
        //          System.out.print("*");
        //      }
        //      System.out.println();
        // }

        // Scanner sc = new Scanner(System.in);
        // System.out.println("Enter which number: "); 
        // int num = sc.nextInt();
        
        // for (int i = 1; i <= num; i++){
        //     for(int j = 0; j < i; j++){
        //          System.out.print("*");
        //      }
        //      System.out.println();
        // }

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); 
        int num = sc.nextInt();
        
        for (int i = 0; i < num; i++){
            for ( int j=0; j < num - i - 1; j++){
                System.out.print(" ");
            }
            for (int k = 0; k<= i; k++){
                System.out.print("*");
            }
            System.out.println();
        }

        sc.close();
    }
}