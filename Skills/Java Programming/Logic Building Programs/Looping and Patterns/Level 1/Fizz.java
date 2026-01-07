//Print the sum of first n natural numbers. 

import java.util.Scanner;

public class Fizz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: ");
        int num = sc.nextInt();
        //for(int i = 1; i < 11; i++){
            //System.out.println("" + tableNumber + " X " + i + " = " + (tableNumber*i));
        //}
        int i = 1;
        int sum = 0;
        while( i < (num+1)){
            sum += i;
            i++;
        }
        System.out.println(sum);
        sc.close();
    }
}
