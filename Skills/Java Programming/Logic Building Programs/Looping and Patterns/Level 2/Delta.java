//Find the sum of digits of a number.

//import java.util.Scanner;

import java.util.Scanner;

public class Delta {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); // 545 --> 5 + 4 + 5
        int num = sc.nextInt();
        int count = 0;

        if( num == 0){
            System.out.println("Sum is 0");
        }

        while( num > 0 ){
            count += (num % 10);
            num /= 10;
        }

        System.out.println(count);
        sc.close();
    }
}
