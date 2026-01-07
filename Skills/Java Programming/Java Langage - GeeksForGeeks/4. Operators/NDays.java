import java.util.*;
public class NDays {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int d = sc.nextInt();
        int n = sc.nextInt();
        int x = n % 7;
        int ans = d - x;
        if(ans > 0){
            System.out.println(ans);
        }else{
            System.out.println(ans+7);
        }
        sc.close();
    }
}
