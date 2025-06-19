# Test R script
texte <- "test"
paste("R is", texte)
test1 <- "tomo" # nolint
test2 <- "toto"
test3 <- "titi"
# print(paste(test1, test2, test3, sep = "-")) # nolint
nim1 <- 1
nim2 <- 2
nim1 + nim2
# print(nim1 + nim2) # nolint
var1 <- var2 <- var3 <- 1:10 # nolint
# print(var1, var2, var3) # nolint # nolint
# print(paste(var1, var2, var3, sep = "-")) # nolint
x <- 45L # nolint
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
str <- c("lirili\nlarila\nbombardino\nririli\n", "ririli\n", "lirili\n", "larila\n", "bombardino\n") # nolint
# cat(str) # affiche la chaine de caracteres # nolint
nchar(str) # compte le nombre de caracteres
grepl("li", str) # verifie si "li" est present dans str
grep("ri", str) # retourne les indices des occurences de "li"
gsub("li", "xx", str) # remplace "li" par "xx"
sub("li", "xx", str) # remplace la premiere occurence de "li" par "xx"
strsplit(str, "\n") # divise la chaine de caracteres en fonction du separateur "\n" # nolint
ptr <- "i'm atomic \"variable\",big mama \\hh\\" # nolint
# a=15 # nolint
# b=20 # nolint
# if (a > b) {
#  print("a est plus grand que b") # nolint
# } else if (a < b) {
#  print("a est plus petit que b") # nolint
# } else {
#  print("a est egal a b") # nolint: commented_code_linter.
# }
a <- 15
b <- 20
a %% b # modulo de a par b # nolint
a %/% b # division entiere de a par b (quotient)
d <- 5 # affectation locale
a | b # ou logique (element par element)
a & b # et logique (element par element)
a && b # et logique court-circuit
a || b # ou logique court-circuit
a <- 1:10 # sequence de 1 a 10 # nolint
a <- matrix(1:4, nrow = 2) # matrice 2x2
b <- matrix(5:8, nrow = 2) # matrice 2x2
a %in% b # verifzie si a est dans b
a %*% b # produit matriciel de a et b
a %o% b # produit tensoriel de a et b
a %x% b # produit tensoriel de a et b
i <- 1
while (i < 6) {
  # print(i) # nolint
  i <- i + 1
  if (i == 3) {
    break # passe a l'iteration suivante
  }
}
i <- 0
while (i < 6) {
  i <- i + 1
  if (i == 3) {
    next # passe a l'iteration suivante en omettant l'affichage de 3
  }
  # print(i) # nolint
}
for (x in 1:10) {
  if (x == 5) {
    next
  } else {
    # print(x) # nolint
  }
}
fruits <- list("apple", "banana", "cherry") # liste de fruits
for (x in fruits) {
  # print(x) # affiche chaque fruit # nolint
}
fruits <- c("apple", "banana", "cherry") # vecteur de fruits
for (x in fruits) {
  # print(x) # affiche chaque fruit # nolint
}
dice <- c(1, 2, 3, 4, 5, 6) # vecteur de des
for (x in dice) {
  if (x == dice[3]) {
    next # passe a l'iteration suivante en omettant l'affichage de 3
  }
  # print(x) # nolint
}
fruits <- list("apple", "banana", "cherry")

for (x in fruits) {
  if (x == "cherry") {
    break
  }
  # print(x) # nolint
}
