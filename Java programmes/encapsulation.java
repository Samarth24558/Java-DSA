class Employee
{
    private double basic_salary;
    

    public void Employee(double basic_salary)
    {
        this.basic_salary=basic_salary;
        
    }
    public void display()
    {
     
        System.out.println("Basic salary: "+this.basic_salary);
        System.out.println("TA: "+((this.basic_salary/100)*100));
        System.out.println("HRA: "+((this.basic_salary/100)*15));
        System.out.println("DA: "+((this.basic_salary/100)*20));


    }
}

public class encapsulation 
{
    public static void main(String[] args) 
    {
        Employee employee=new Employee(2500);
        employee.display();
        
    }
    
}

