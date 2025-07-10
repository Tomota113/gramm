/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    float a;
    int i=1;
    printf("note %d est ",i);
    scanf("%f",&a);
    float somme=a;
    while(a>0){
        i++;
        printf("note %d est ",i);
        scanf("%f",&a);
         if(a<0){
        break;
    }
        somme=somme+a;
    }
    printf("%.2f\n",somme);
    double moyenne;
    moyenne=somme/(i-1);
    printf("%.2f",moyenne);
    
    
	return 0;
}
