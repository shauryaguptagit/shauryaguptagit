//Check if a number is prime or not. PRIME NUMBER --> 13 is only divisible by 13 and 1


import java.util.Scanner;

public class Hector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); //13
        int number = sc.nextInt();
        
        if(number == 0 || number == 1){
            System.out.println("Neither Prime Nor Composite");
        }else{
            
            int num = Math.abs(number);

            int i = 1;
            int count = 0;
            while((num + 1) > i){
                if(num % i ==0){
                    count++;
                }
                i++;
            }
            if(count == 2){
                System.out.println("Prime Number");
            }else{
                System.out.println("Not Prime");
            }

        }

        sc.close();
    }
}
