//Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions. 
/*
 *  Cold:  Below 15°C (59°F)
    Warm:  15°C to 25°C (59°F to 77°F)
    Hot:   Above 25°C (77°F)
 */


import java.util.Scanner;

public class Hector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the temp: ");
        double tempValue = sc.nextDouble();
        if (tempValue<15) {
            System.out.println("Cold");
        }else if(tempValue>=15 && tempValue <= 25){
            System.out.println("Warm");
        }else{
            System.out.println("Hot");
        }
        sc.close();
    }
}
