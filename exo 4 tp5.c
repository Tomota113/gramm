/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

struct etudiant{
    char nom[50];
    int age;
    float moyenne;
};

void saisir(struct etudiant *a){
    printf("nom: ");
    scanf("%s",a->nom);
    printf("age: ");
    scanf("%d",&(a->age));
    printf("moyenne: ");
    scanf("%f",&(a->moyenne));
}
void afficher(struct etudiant a){
    printf("%s",a.nom);
    printf("%d",a.age);
    printf("%f",a.moyenne);
}    

int main()
{
   struct etudiant a;
    saisir(&a);
    afficher(a);
    
    
    
}