//Print Fibonacci series up to n terms.
// 0 1 1 2 3 5 8 .........


import java.util.Scanner;

public class Icicle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); // 5 --> 0 1 1 2 3
        int num = sc.nextInt();

        int termOne = 0; // 1 1 2 3
        int termTwo = 1; // 1 2 3 5

        int i = 1;
        while( i <= num){ // 1, 2, 3, 4, 5
            System.out.println(termOne + " ");
            int nextTerm = termOne + termTwo;
            termOne = termTwo;
            termTwo = nextTerm;
            i++;
        }
        System.out.println(); // 0 1 1 2 3
        sc.close();
    }
}
