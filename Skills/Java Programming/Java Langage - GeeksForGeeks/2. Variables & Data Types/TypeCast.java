import java.util.*;

class TypeCast {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String num = sc.nextLine();
        // TypeCast to int double it and print
        int num1 = Integer.parseInt(num);
        num1 = num1*2;
        System.out.println(num1);
        sc.close();
    }
}
