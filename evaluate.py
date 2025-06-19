from evaluate import load

bleu = load("bleu")
predictions = ["Bonjour"]
references = [["Salut"]]  # Liste de listes (car plusieurs références possibles)
print(bleu.compute(predictions=predictions, references=references))