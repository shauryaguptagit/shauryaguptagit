//Take an alphabet character and check if it lies between 'a' and 'm' or 'n' and 'z'. 


import java.util.Scanner;

public class Hector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a character: ");
        char ch = sc.next().charAt(0);
        
        if (ch >= 'a' && ch <= 'm'){
            System.out.println("Yes! It lies b/w 'a' and 'm'");
        }else if(ch >= 'n' && ch <= 'z'){
            System.out.println("Yes! It lies b/w 'n' and 'z'");
        }else{
            System.out.println("No it does not lie b/w 'a' and 'm' or 'n' and 'z'");
        }
        sc.close();
    }
}
