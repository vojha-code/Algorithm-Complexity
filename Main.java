public class Main{ 

    /*
      int x[] : takes an input array of integer
      return : a float value of even sum
    */
    public static int evenSummation(int[] x){
        int evenSum = 0;   //OP1: initializing sum temp variable 
        int n = x.length;  //OP2: find array length
        for(int i = 0; i < n; i++){
            if(x[i]%2 == 0){ //OP3 check if a number is even?
                evenSum = evenSum + x[i]; //OP4: adding eval values
            }
        }
        return evenSum;  //OP5: returning the values   
    }

    public static void main(String[] args){ 
        int n = 500000;
        int[] x  = new int[n]; // assign values to an array
        // preparing data of size n
        for(int i = 0; i< n; i++){
          x[i] = i;
        }
        
        // measuring time taken by a Java function
        long start = System.currentTimeMillis();

        int evenSum = evenSummation(x); //function calling 

        long finish = System.currentTimeMillis();
        double timeElapsed = (finish - start)/1000F; 

        System.out.printf("time taken by java is (sec)::  %f \n",timeElapsed);
    } 
} 
