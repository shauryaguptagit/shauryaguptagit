public class Divisor {
    void printDivisors(int n) {
        // code here
        for(int i = 1; i<=n; i++){
            if(n%i == 0){
                System.out.print(i + " ");
            }
        }
    }
    public static void main(String[] args) {
        Divisor div = new Divisor();
        div.printDivisors(54);
    }
}