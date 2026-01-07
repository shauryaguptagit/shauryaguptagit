//Print the factorial of a given number. 


// 5! = 5 X 4 X 3 X 2 X 1


import java.util.Scanner;

public class Icicle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); // 6
        int num = sc.nextInt();

        int i = 1;
        int factorialValue = 1;
        while( i < (num+1)){ // 1 2 3 4 5 6
            factorialValue *= i;
            i++;
        }
        System.out.println(factorialValue);
        sc.close();
    }
}
