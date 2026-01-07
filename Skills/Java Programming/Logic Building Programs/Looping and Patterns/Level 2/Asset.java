//Count the number of digits in a given number. 

import java.util.Scanner;

public class Asset{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); // 6  65  655  6555 
        int num = sc.nextInt();
        
        int digitCount = 0;

        if( num == 0){
            System.out.println("1");
        }

        while( num > 0){
            digitCount++;
            num /= 10;
        }
        
        System.out.println(digitCount);


        sc.close();
    }
}