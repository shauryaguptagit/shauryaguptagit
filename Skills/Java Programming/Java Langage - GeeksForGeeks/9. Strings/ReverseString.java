public class ReverseString {
    public static String reverseString(String s) {
        // code here
        StringBuilder sb = new StringBuilder(s);
        sb.reverse();
        return sb.toString();
    }
    public static void main(String[] args) {
        String str = "GeeksForGeeks";
        System.out.println("Reversed string is: " + reverseString(str));
    }
}