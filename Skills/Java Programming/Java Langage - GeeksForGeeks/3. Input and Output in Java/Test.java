import java.io.*;

public class Test{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter a string: ");
        // String s = br.readLine();
        int s = Integer.parseInt(br.readLine());
        System.out.println("You entered " + s);
    }
}