//Check voting eligibility for a given age (18+). 

import java.util.Scanner;

public class Fizz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter age: ");
        int age = sc.nextInt();
    
        if (age>=18){
            System.out.println("Can Vote");
        }else{
            System.out.println("Cannot Vote");
        }
        sc.close();
    }
}
