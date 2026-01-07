import java.io.*;
import java.util.*;

class TypeConv {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        double d = sc.nextDouble();
        // Typecast and print
        int nested = (int) d;
        System.out.println(nested);
        sc.close();
    }
}
