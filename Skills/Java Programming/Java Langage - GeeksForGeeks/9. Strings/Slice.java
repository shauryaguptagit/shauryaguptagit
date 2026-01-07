public class Slice {
    public static String sliceString(String s) {
        // code here
        String str1 = s.substring(1,s.length()-1);
        return str1;
    }
    public static void main(String[] args) {
        String str = "GeeksForGeeks";
        System.out.println("Sliced string is: " + sliceString(str));
    }
}