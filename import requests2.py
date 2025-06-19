import pandas as pd

# Charger votre fichier CSV
df = pd.read_csv("bambara_clean.csv", encoding='utf-8')

# Afficher les 3 premières lignes pour vérification
print("Exemple de données avant nettoyage:")
print(df.head(3))

# 1. Supprimer les doublons (en se basant sur bambara_1)
df = df.drop_duplicates(subset=["bambara_1"])

# 2. Nettoyer les colonnes (supprimer les espaces superflus)
df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# 3. Uniformiser les transcriptions (exemple: remplacer ɛ par è)
df["transcription_1"] = df["transcription_1"].str.replace("ɛ", "è")
df["transcription_2"] = df["transcription_2"].str.replace("ɛ", "è")

# 4. Créer une version simplifiée pour la traduction
df_trad = df[["bambara_1", "francais"]].copy()
df_trad.columns = ["bambara", "francais"]  # Renommage pour compatibilité

# Sauvegarder les résultats
df.to_csv("lexique_complet_nettoye.csv", index=False, encoding='utf-8')
df_trad.to_csv("paires_traduction.csv", index=False, encoding='utf-8')

print("\nRésultats:")
print(f"- Fichier complet sauvegardé: lexique_complet_nettoye.csv ({len(df)} entrées)")
print(f"- Paires de traduction sauvegardées: paires_traduction.csv")
print("\nAperçu des paires de traduction:")
print(df_trad.head())