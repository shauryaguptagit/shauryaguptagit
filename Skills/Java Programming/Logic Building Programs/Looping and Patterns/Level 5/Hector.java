//Print factorial of each number from 1 to n.


import java.util.Scanner;

public class Hector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); // 5
        int num = sc.nextInt();
        int factorial = 1;
        for (int i = 1; i <= num; i++){ // 1 2 3 4 5
            for (int j = 1; j <= i; j++){ //1,1 2,1 2,2 3,1 3,2 3,3
                if ( j == 1){
                    factorial *= i;
                    System.out.println(factorial);
                }
            }
        }
        sc.close();
    }
}
