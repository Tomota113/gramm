/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    int i,n,som;
    som=0;
    i=0;
    while(i<4){
        printf("donner un entier ");
        scanf("%d",&n);
        som+=n;
        i++;
    }
    printf("somme: %d\n",som);
    
	return 0;
}
