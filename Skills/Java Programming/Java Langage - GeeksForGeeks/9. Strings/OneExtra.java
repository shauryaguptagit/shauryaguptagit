public class OneExtra {
    public static char extraChar(String s1, String s2) {

        // write your code here
        char result = 0;
        
        for(int i = 0; i < s1.length(); i++){
            result ^= s1.charAt(i); 
        }
        for(int i = 0; i < s2.length(); i++){
            result ^= s2.charAt(i); 
        }
        return result;
    }
    public static void main(String[] args) {
        String s1 = "abcd";
        String s2 = "abcde";
        System.out.println("The extra character is: " + extraChar(s1, s2));
    }
}