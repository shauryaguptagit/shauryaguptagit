//Take marks (0–100) and print the corresponding grade (A/B/C/D/F).

import java.util.Scanner;

public class Czech {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the marks: ");
        int marksObtained = sc.nextInt();
        
        if (marksObtained >= 90){
            System.out.println("A");
        }else if(marksObtained >=80){
            System.out.println("B");
        }else if(marksObtained >=70){
            System.out.println("C");
        }else if(marksObtained >=60){
            System.out.println("D");
        }else{
            System.out.println("F");
        }
        sc.close();
    }
}
