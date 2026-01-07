import java.util.*;

public class NextPrime {
    public static void main(String args[]) {
        // Your Code Here
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(nextPrime(n));
    }
    
    static int nextPrime(int n){
        int num = n+1;
        while(true){
            if(isPrime(num)){
                return num;
            }
            num++;
        }
    }
    
    static boolean isPrime(int n){
        if(n<1){return false;}
        if(n==2 || n==3){return true;}
        if(n%2==0 || n%3==0){return false;}
        
        for(int i =5; i*i<=n; i+=6){
            if(n%i==0 || n%(i+2)==0){
                return false;
            }
        }
        return true;
    }
}