class Employee{
    protected int id;
    protected int salary;
    public Employee(int id, int salary){
        this.id = id;
        this.salary = salary;
    }
}

class SalesEmployee extends Employee{
    protected int sales;
    public SalesEmployee(int id, int salary, int sales){
        super(id,salary);
        this.sales = sales;
    }
}