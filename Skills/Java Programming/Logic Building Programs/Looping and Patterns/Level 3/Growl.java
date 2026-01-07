//Find the sum of all factors of a number.

//import java.util.Scanner;

import java.util.Scanner;

public class Growl {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); //100
        int num = sc.nextInt();

        int sum = 0;

        for (int i = 1; i<= num /2; i++){
            if(num % i == 0){
                sum += i;
            }
        }
        System.out.println(sum + num);
        sc.close();
    }
}
