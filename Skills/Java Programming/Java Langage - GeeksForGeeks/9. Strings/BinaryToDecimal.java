// User function Template for Java

public class BinaryToDecimal {
    public int binaryToDecimal(String b) {
        // Code here
        int decimal = 0;
        for (int i =0; i < b.length(); i++){
            char bit = b.charAt(i);
            
            decimal = decimal * 2 + (bit - '0');
        }
        return decimal;
    }

    public static void main(String[] args) {
        BinaryToDecimal converter = new BinaryToDecimal();
        String binaryString = "1010";
        int decimalValue = converter.binaryToDecimal(binaryString);
        System.out.println("The decimal value of binary " + binaryString + " is: " + decimalValue);
    }
}