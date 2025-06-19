import random

# Dictionnaire complet de traduction Bambara-Français
traductions = {
    # Salutations
    "i ni sogoma": "Bonjour, bon matin",
    "ambaa": "Réponse masculine à 'bonjour'",
    "ounse": "Réponse féminine à 'bonjour'",
    "i ni tile": "Bonjour, bon après-midi / midi",
    "i ni wula": "Bonjour, début d'après-midi",
    "i ni su": "Bonsoir",
    "i ka kɛnɛ?": "Comment vas-tu ?",
    "tɔɔrɔ si tɛ": "Je vais très bien / pas de problème",
    "tɔɔrɔ si te": "Ça va bien, aucun problème",
    "i bisimila!": "Bienvenue !",
    "ini tche!": "Merci",
    "a' ni cɛ": "Merci à lui/elle",
    "k'an bɛn": "Au revoir / à bientôt",
    "nba": "Réponse masculine à bonjour",
    "nse": "Réponse féminine à bonjour",
    "i ni ce": "Merci (formel)",
    "aw ni ce": "Merci à vous (pluriel ou formel)",
    "aw bisimila!": "Bienvenue à plusieurs",
    "saha!": "Merci en retour à 'bisimila'",
    "k'an bɛn sɔɔni": "À bientôt",
    "k'an bɛn sini": "À demain",

    # Conversations
    "somɔgɔw bɛ di?": "Comment va la famille ?",
    "tɔɔrɔ t'u la": "Ils vont bien",
    "i tɔgɔ?": "Comment tu t'appelles ?",
    "ne tɔgɔ …": "Je m'appelle …",
    "i bɛ bɔ min?": "Tu viens d'où ?",
    "n bɛ bɔ …": "Je viens de …",
    "gɛlɛya ye mun ye?": "Quel est le problème ?",
    "mun don?": "C'est quoi ? / Que se passe-t-il ?",
    "i y'a faamu?": "Tu comprends ?",
    "n m'a faamu": "Je ne comprends pas",
    "n y'a faamu": "Je comprends",

    # Actions
    "na yan": "Viens ici",
    "i sigi": "Assieds-toi",
    "waati dɔɔnin dɔrɔn": "Un instant",
    "aw ye don": "Entrez !",
    "a ka ɲi": "D'accord / c'est bon",
    "hakéto": "Pardon / excuse-moi",
    "hakéto m'a faamu": "Désolé(e) j'ai pas compris",
    "ka su hεεrε": "Bonne nuit",

    # Nourriture et boissons
    "daraka": "Petit-déjeuner",
    "tilelafana": "Déjeuner",
    "surɔfana": "Dîner",
    "dabileni": "Bissap",
    "bleman": "Rouge",
    "djaiman": "Blanc",
    "nɔ̀nɔ": "Lait",
    "dí": "Miel",
    "glɔ": "Bière",
    "dlɔ̀": "Bière",
    "dlɔ̀min": "Boire de la bière",
    "dlɔ̀tɔya": "Ivre",

    # Famille et personnes
    "den": "Enfant",
    "denw": "Enfants",
    "muso": "Femme / épouse",
    "cɛ": "Homme / mari",
    "dɔ̀kɔtɔrɔ": "Docteur",
    "dɔ̀kɔtɔrɔmuso": "Docteur féminin",
    "dunan": "Étranger",
    "dunánkɛ": "Étranger mâle",
    "dunánmuso": "Étranger femme",

    # Objets et nature
    "mobili": "Voiture",
    "wari": "Argent",
    "finin": "Vêtement",
    "ji": "Eau",
    "dolari": "Dollar",
    "juru": "Corde",
    "bin": "Herbe",
    "fiyɛn": "Vent",
    "sanji": "Pluie",

    # Verbes et actions
    "ka gilan": "Construire/faire/inventer",
    "ka bein": "S'entendre",
    "ka gnogonye": "Se rencontrer",
    "ka dabiri": "Couvrir",
    "ka kalaya": "Réchauffer",
    "ka suma": "Mesurer",
    "ka yìra": "Montrer",
    "ka sigi": "S'asseoir",
    "ka wuli": "Se lever",
    "ka filɛ": "Regarder",
    "ka tɛ̀mɛ": "Passer",

    # Nombres
    "kelen": "Un",
    "fila": "Deux",
    "saaba": "Trois",
    "naani": "Quatre",
    "duuru": "Cinq",
    "wɔɔrɔ": "Six",
    "wolonfila": "Sept",
    "segin": "Huit",
    "kɔnɔntɔn": "Neuf",
    "tan": "Dix",

    # Expressions diverses
    "funteni bé": "Il fait chaud",
    "nɛnɛ bɛ": "Il fait froid",
    "sanji bɛ ka na": "Il pleut",
    "jogo jugu": "Mauvais comportement",
    "barika ala ye": "Dieu merci",
    "ne dalen b allah la": "Je crois en Dieu",
    "den bɛ ka kasi": "Le bébé pleure",
    "den tun bɛ sunɔgɔ la": "Le bébé dormait",
    "mobili ka teliya kosɛbɛ": "La voiture est très rapide",
    "baji ka bon": "La rivière est large",
    "tasuma bɛ so la": "La maison est en feu",
    "maliba": "Le grand Mali"
}


def traduire_bambara_francais(phrase):
    phrase = phrase.lower().strip()

    # Vérifie d'abord les correspondances exactes
    if phrase in traductions:
        return traductions[phrase]

    # Ensuite vérifie les correspondances partielles
    mots_trouves = []
    for bambara, francais in traductions.items():
        if bambara in phrase:
            mots_trouves.append(f"{bambara} : {francais}")

    if mots_trouves:
        return "Je n'ai pas compris toute la phrase, mais voici ce que j'ai reconnu:\n" + "\n".join(mots_trouves)
    else:
        suggestions = []
        for mot in phrase.split():
            if mot in traductions:
                suggestions.append(f"{mot} : {traductions[mot]}")

        if suggestions:
            return "Je ne connais pas cette phrase, mais voici des mots que je reconnais:\n" + "\n".join(suggestions)
        else:
            return "Désolé, je n'ai pas compris cette phrase en bambara. Essayez une autre phrase."


def chatbot():
    salutations = [
        "I ni sɔgɔma! N ye chatbot ye min bɛ bamanankan kumasenw fɛɛrɛ faransikan na.",
        "Aw bisimila! N bɛ se ka i dɛmɛ ka bamanankan fɛɛrɛ faransikan na.",
        "I ni ce! N bɛ bamanankan kumasenw fɛɛrɛ faransikan na."
    ]

    print(random.choice(salutations))
    print("Vous pouvez écrire des phrases en bambara et je les traduirai en français.")
    print("Tapez 'k'an bɛn' pour quitter.\n")

    while True:
        entree = input("Vous (en bambara): ")

        if entree.lower().strip() in ["k'an bɛn", "a ja"]:
            print("Chatbot: K'an bɛn sɔɔni! À bientôt!")
            break

        traduction = traduire_bambara_francais(entree)
        print(f"Chatbot: {traduction}\n")


if __name__ == "__main__":
    chatbot()