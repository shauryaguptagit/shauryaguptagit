import java.util.*;

public class Fibo {
    
    static int fib(int n){
        if(n<=1) return n;
        
        int a=0, b=1, c=0;
        for(int i =2; i<=n; i++){
            c=a+b;
            a=b;
            b=c;
        }
        return b;
    }
    
    public static void main(String args[]) {
        // Your Code Here
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(fib(n));
        sc.close();
    }
}