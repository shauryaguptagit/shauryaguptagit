public class ConsAndVows {

    static void checkString(String s) {
        int v = 0;
        int c = 0;

        // Your code here
        

        if (v > c)
            System.out.print("Yes");
        else if (c > v)
            System.out.print("No");
        else
            System.out.print("Same");

        System.out.println();
    }

    public static void main(String[] args) {
        String s = "geeksforgeeks";
        checkString(s);
    }
}