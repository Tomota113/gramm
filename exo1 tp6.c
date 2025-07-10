/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int my(int n){
    if(n<2){
        return n;
    }else{
        return my(n-1)+my(n-2);
    }
}
int main()
{
    int n=3;
    int p=my(n);
    printf("%d",p);
    
}