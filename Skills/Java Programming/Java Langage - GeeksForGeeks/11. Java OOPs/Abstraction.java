abstract class Shape{
    String color;
    Shape(String c){
        this.color = c;
    }
    public String getColor(){
        return this.color;
    }
    abstract double getArea();
}

class Square extends Shape{
    double side;
    Square(String c, double side){
        super(c);
        this.side = side;
    }
    public double getArea(){
        return side * side;
    }
}