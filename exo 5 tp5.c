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
    printf("nom: %s",a.nom);
    printf("age: %d",a.age);
    printf("moyenne: %f",a.moyenne);
}    
void meilleur(struct etudiant *a,int taille){
    float b=0;
    for(int i=0;i<taille;i++){
        if(a[i].moyenne>b){
            b=a[i].moyenne;
        }
    }
    printf("le meilleur est %f",b);
}
int main()
{
    int taille=2;
   struct etudiant a[2];
   for(int i=0;i<2;i++){
    saisir(&a[i]);
       
   }
    for(int i=0;i<2;i++){
    afficher(a[i]);
    }
    
    meilleur(a,2);
    
}