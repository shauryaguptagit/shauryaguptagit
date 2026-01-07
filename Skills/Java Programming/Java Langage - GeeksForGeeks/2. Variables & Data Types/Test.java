// public class Test {
 
//     public static void main(String[] args) {
//         boolean isValid = true;
//         byte marks = 90;
//         float PI = 3.14f;
//         float div = 15.0f/4.0f;
//         long views = 100000000;
//         char gender = 'M';
//     }
// }


// class Point{
//     int x;
//     int y;
// }
// public class Test{
//     public static void main(String[] args) {
//         Point p = new Point();
//         p.x = 10;
//         p.y = 10;
//         System.out.println(p.x + " " + p.y);
//     }
// }


class Point{
    int x;
    int y;
}

class Test{
    public static void main(String[] args) {
        Point p1 = new Point();
        p1.x = 10; p1.y = 20;
        Point p2 = p1;
        p2.x = 30;
        System.out.println(p1.x);
        System.out.println(p2.x);
    }
}