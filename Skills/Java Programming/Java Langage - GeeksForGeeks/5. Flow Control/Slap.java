import java.util.*;
public class Slap {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the values of operands a and b");
        int a = sc.nextInt();
        int b = sc.nextInt();
        
        System.out.println("Enter the operation you would like to perform: (+ | - | * | / )");
        sc.nextLine();
        String operation = sc.nextLine();

        if(operation.equals("+")){
            System.out.println((a+b) + " is the sum!");
        }else if(operation.equals("-")){
            System.out.println((a-b) + " is the difference!");
        }else if(operation.equals("*")){
            System.out.println((a*b) + " is the product!");
        }else if(operation.equals("/")){
            System.out.println((a/b) + " is the divisor!");
        }else{
            System.out.println("Invalid operation!");
        }

        sc.close();
    }
}
