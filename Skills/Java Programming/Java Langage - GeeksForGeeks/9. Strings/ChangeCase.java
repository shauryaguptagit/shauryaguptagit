public class ChangeCase {
    public static void changeCase(String s) {
        // code here
        System.out.println(capitalize(s));
        System.out.println(s.toUpperCase());
    }
    public static String capitalize(String s) {
        if(s.isEmpty() || s==null){
            return s;
        }
        return s.substring(0,1).toUpperCase()+s.substring(1);
    }
    public static void main(String[] args) {
        String str = "geeksforGeeks";
        System.out.println("Changing case for the string: " + str);
        changeCase(str);
    }
}