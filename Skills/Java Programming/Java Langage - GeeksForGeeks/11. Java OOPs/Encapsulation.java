class Person{
    private String name;
    private int age;
    
    public Person(){
        this.name = "Geeks";
        this.age = 10;
    }
    
    public void setName(String name){
        this.name = name;
    }
    
    public void setAge(int age){
        this.age = age;
    }
    
    public String getName(){
        return name;
    }
    
    public int getAge(){
        return age;
    }
}