//Print the product of digits of a given number. 
import java.util.Scanner;

public class Jazz {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter which number: "); // 6  65  655  6555 
        int num = sc.nextInt();
        
        int tempNum = num;
        int product = 1;

        while( tempNum > 0){

            int lastDigit = tempNum % 10;

            product *= lastDigit;

            tempNum = tempNum / 10;
        }

        if (num == 0){
            System.out.println(0);
        }else{
            System.out.println(product);
        }


        sc.close();
    }
}
