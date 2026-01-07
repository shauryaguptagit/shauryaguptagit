public class PrintAlpha {
    public static void alphabets(char c1, char c2) {
        // code here
        for(char i = c1; i<=c2; i++) {
            System.out.print(i + " ");
        }
    }
    public static void main(String[] args) {
        char c1 = 'a';
        char c2 = 'f';
        System.out.println("Alphabets between " + c1 + " and " + c2 + " are: ");
        alphabets(c1, c2);
    }
}