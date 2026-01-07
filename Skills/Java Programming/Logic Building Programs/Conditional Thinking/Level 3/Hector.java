//Check if a number lies within the range [100, 999].


import java.util.Scanner;

public class Hector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = sc.nextInt();
        
        if (num >= 100 && num <= 999 ){
            System.out.println("Yes! number lies within the range [100, 999]");
        }else{
            System.out.println("No it does not lie b/w athe range [100, 999]");
        }
        sc.close();
    }
}
