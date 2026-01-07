//Check whether a number is a perfect square (without using the square root function). 


import java.util.Scanner;

public class Jazz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = sc.nextInt(); //23
        int i = 0;
        while (i*i < num) {
            i++;
        }
        if (i*i == num){
            System.out.println("Perfect Square");
        }else{
            System.out.println("Not a perfect square");
        }

        sc.close();
    }
}
