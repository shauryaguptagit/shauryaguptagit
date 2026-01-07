//Print all factors of a given number.
import java.util.Scanner;

public class Fizz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); //100
        int num = sc.nextInt();

        for (int i = 1; i<= num /2; i++){
            if(num % i == 0){
                System.out.print(i + " ");
            }
        }
        System.out.println(num);
        sc.close();
    }
}
