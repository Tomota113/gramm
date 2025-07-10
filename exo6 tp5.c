/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

struct voiture{
  char marque[25];
  int kilo;
  int dispo;
  
};

void afficher(struct voiture *a){
    printf("%s",a->marque);
    printf("%d",a->kilo);
    printf("%d",a->dispo);
}

int main()
{
    struct voiture e1={"toyata",14,0};
    afficher(&e1);
    
}