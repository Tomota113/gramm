texte <- "test"
paste("R is",texte)
test1<- "tomo"
test2 <- "toto"
test3 <- "titi"
#print(paste(test1, test2, test3, sep = "-"))
nim1 <- 1
nim2 <- 2
nim1 + nim2
#print(nim1 + nim2) # nolint
var1 <-var2<-var3 <- 1:10 # nolint
#print(var1, var2, var3) # nolint # nolint
#print(paste(var1, var2, var3, sep = "-"))
x<-45L # nolint
is.character(x) # verifie si x est un caractere
is.logical(x) # verifie si x est un logique
is.numeric(x) # verifie si x est un nombre
is.integer(x) # verifie si x est un entier
as.integer(x) # convertie en entier
as.character(x) # convertie en caractere
as.numeric(x) # convertie en nombre
as.logical(x) # convertie en logique
max(5, 10, 15) # retourne le maximum
min(5, 10, 15) # retourne le minimum
sum(5, 10, 15) # retourne la somme
mean(5, 10, 15) # retourne la moyenne
sqrt(16) # retourne la racine carree
abs(-5.3) # retourne la valeur absolue
ceiling(5.3) # retourne le plafond
floor(5.3) # retourne le plancher
round(5.3) # retourne l'arrondi
round(5.7) # retourne l'arrondi
str<-c("lirili\nlarila\nbombardino\nririli\n","ririli\n","lirili\n","larila\n","bombardino\n")
#cat(str) # affiche la chaine de caracteres
nchar(str) # compte le nombre de caracteres
grepl("li", str) # verifie si "li" est present dans str
grep("ri", str) # retourne les indices des occurences de "li"
gsub("li", "xx", str) # remplace "li" par "xx"
sub("li", "xx", str) # remplace la premiere occurence de "li" par "xx"
strsplit(str, "\n") # divise la chaine de caracteres en fonction du separateur "\n"
ptr<- "i'm atomic \"variable\",big mama \\hh\\"
#a=15
#b=20
#if (a > b) {
#  print("a est plus grand que b")
#} else if (a < b) {
#  print("a est plus petit que b")
#} else {
#  print("a est egal a b") # nolint: commented_code_linter.
#}
a <- 15
b <- 20
a%%b # modulo de a par b # nolint
a %/% b # division entiere de a par b (quotient)
d <- 5 # affectation locale
a | b # ou logique (element par element)
a & b # et logique (element par element)
a && b # et logique court-circuit
a || b # ou logique court-circuit
a 1: 10 # sequence de 1 a 10 # nolint
a %in% b # verifie si a est dans b
a %*% b # produit matriciel de a et b
