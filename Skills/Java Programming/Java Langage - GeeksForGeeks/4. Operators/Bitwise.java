public class Bitwise{
    public static void main(String[] args) {
        int x = 5;
        System.out.println(~x);
        /*
        5 = 101
        int = 32 bits
        00000000000000000000000000000101
        11111111111111111111111111111010
        2^32 - 1 -> 32 one bits
        2^32 - 1 - 5 --> Number
        -x = 2^32 -x
        x = -6
         */

        
        System.out.println(x<<1); //00000000000000000000000000000101 -> 00000000000000000000000000001010 (10)
        
        System.out.println(x>>1);
    }
}