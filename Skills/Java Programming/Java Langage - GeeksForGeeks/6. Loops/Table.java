// import java.io.*;
import java.util.*;

class Table {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i =1; i<=10; i++){
            System.out.println(n + " X " + i + " = " + i*n);
        }
        sc.close();
    }
}