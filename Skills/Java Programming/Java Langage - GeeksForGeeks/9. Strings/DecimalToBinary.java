// User function Template for Java
public class DecimalToBinary {
    public static String toBinary(int n) {
        // Code here
        if (n == 0){
            return "0";
        }
        StringBuilder binary = new StringBuilder();
        
        while(n>0){
            binary.append(n%2);
            n/=2;
        }
        return binary.reverse().toString();
    }
    public static void main(String[] args) {
        int number = 10;
        System.out.println("Binary representation of " + number + " is: " + toBinary(number));
    }
}