import java.util.*;
public class Mess {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if(n%2==0){
            System.out.println("Opponent!");
        }else{
            System.out.println("You!");
        }
        sc.close();
    }
}
