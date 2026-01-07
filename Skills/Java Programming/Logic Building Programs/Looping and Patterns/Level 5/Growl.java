//Print a pattern where each row i prints i*i.

import java.util.Scanner;

public class Growl {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); //100
        int numOfRows = sc.nextInt();

        for (int i = 1; i <= numOfRows; i++){
            System.out.println(i*i);
        }

        sc.close();
    }
}
