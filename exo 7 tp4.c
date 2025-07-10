/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

void po(int *a,int n){
    int b,i;
    int c=a[0];
    for(i=1;i<n;i++){
        if(c>a[i]){
            c=a[i];
        }
        }
        printf("%d",c);
    }
    

int main()
{
    int tab[7]={10,6,8,4,95,2,0};
    int n=7;
    po(tab,n);
}