#include <stdio.h>
#include <time.h>

/*
  int x[] : takes an input array of integer
  return : a float value of even sum
*/
int evenSummation(int x[]){
    int evenSum = 0;   //OP1: initializing sum temp variable 
    int n = sizeof(x); //OP2: find array length
    for(int i = 0; i < n; i++){
        if(x[i]%2 == 0){ //OP3 check if a number is even?
            evenSum = evenSum + x[i]; //OP4: adding eval values
      }
    }
    return evenSum; //OP5: returning the values     
}//end of function

int main(){

    int n = 500000;
    int x[n]; // assign values to an array
    // preparing data of size n
    for(int i =0;i < n; i++){
      x[i] = i;
    }

    // measuring time taken by a C function
    clock_t t; 
    t = clock(); 
    int evenSum = evenSummation(x);
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds 
    printf("time taken by C is (sec)::  %f \n", time_taken); 

    return 0;
}
