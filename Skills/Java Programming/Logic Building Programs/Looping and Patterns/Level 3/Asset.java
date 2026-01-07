//Print the squares of numbers from 1 to n.

import java.util.Scanner;

public class Asset{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); 
        int num = sc.nextInt();
        
        for (int i = 1; i <= num; i++){
            System.out.print(i*i + " ");
        }

        sc.close();
    }
}