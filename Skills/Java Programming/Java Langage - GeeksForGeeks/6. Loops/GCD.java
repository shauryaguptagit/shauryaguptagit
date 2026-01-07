import java.util.*;

public class GCD {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i = sc.nextInt();
        int mi = Math.min(n,i);
        int ans =0;
        for(int j = 1; j<=mi; j++){
            if(n%j==0 && i%j==0){
                ans = j;
            }
        }
        System.out.println(ans);
        sc.close();
    }
}