public class array2  
{
    public static void main(String[] args) 
    {
        //Java programme to perform 2dimendional array
        
        int[][] arr=new int[3][3];

        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {
                arr[i][j]=10;
            }
        }

        for(int i=0;i<3;i++)
        {
            System.out.print("["+" ");
            for(int j=0;j<3;j++)
            {  
                System.out.print(+arr[i][j]+" ");
                
            }
            System.out.print("]");
            System.out.println();
        }
        
        int sum=0;
        for(int i=0;i<3;i++)
        {
            for(int j=0;j<3;j++)
            {  
                sum=sum+arr[i][j];
                
            }
            
        }

        System.out.println("sum of matrix is "+sum);
        
        
        
    }
}