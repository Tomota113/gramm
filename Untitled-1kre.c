/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int nbo(int a,int *b,int taille){
    int c=0;
    for(int i=0;i<=taille;i++){
        if(a=b[i]){
            c=c+1;
        }
    }
    printf("%d",c);
}
    

int main()
{
    int a=6;
    int n=5;
    int tab[5]={5,6,34,7,9};
    nbo(a,tab,n);
    
    
    
    
    
}