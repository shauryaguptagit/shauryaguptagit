//Check if an amount can be evenly divided into 2000, 500, and 100 currency notes. 
import java.util.Scanner;

public class Growl {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter amount: ");
        int amount = sc.nextInt(); // 25200
        
        int twoK = amount/2000;
        int fiveH = (amount % 2000)/500;
        int oneH = ((amount % 2000)%500)/100;

        if (twoK*2000 + fiveH*500 + oneH*100 == amount){
            System.out.println("Yes, evenly divided!");
        }else{
            System.out.println("Cannot be evenly divided");
        }

        sc.close();
    }
}
