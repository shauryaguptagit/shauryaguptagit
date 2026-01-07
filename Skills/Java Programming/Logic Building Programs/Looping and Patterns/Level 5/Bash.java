//Count how many numbers between 1–500 are divisible by 7 but not by 5.

//import java.util.Scanner;

public class Bash {
    public static void main(String[] args) {
        int count = 0;
        for (int i = 1; i < 501; i++){
            if ( i % 7 == 0 && i % 5 != 0){
                count += 1;
            }
        }
        System.out.println(count);
    }    
}
