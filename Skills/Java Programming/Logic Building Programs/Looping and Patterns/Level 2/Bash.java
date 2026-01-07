//Print the reverse of a given number.

import java.util.Scanner;

public class Bash {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); // 655 --> 556
        int num = sc.nextInt();
        
        String revNum = "";

        while( num > 0){
            revNum += String.valueOf(num % 10);
            num /= 10;
        }
        
        System.out.println(revNum);


        sc.close();
    }    
}
