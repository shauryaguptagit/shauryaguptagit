public class Out {
    public static void main(String[] args) {
        // int x = 10, y = 20;
        // char z = 'G';
        // String str = "GFG";
        // System.out.println(x);
        // System.out.println(x+y);
        // System.out.println(x +" " + y);
        // System.out.print(str + " ");
        // System.out.print("Courses!");

        int x = 100, y = 200;
        System.out.format("Value of x is %d\n",x);
        double u = Math.PI;
        System.out.println(u);
        System.out.format("Value of PI = %.2f\n", u);
        System.out.format("Value of PI = %5.2f\n", u);
        System.out.format("Value of PI = %05.2f\n", u);
        System.out.printf("x = %d, y=%d", x,y);
    }
}
