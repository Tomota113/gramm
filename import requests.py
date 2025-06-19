import re
import csv
from pandas import DataFrame

# 1. Charger le fichier CSV d'entrée
input_csv = "lexique_bambara.csv"  # Remplacez par votre nom de fichier
output_csv = "lexique_bambara_nettoye.csv"

# Expression régulière pour parser chaque ligne
pattern = re.compile(
    r"(?P<bambara1>[^,]+),(?P<bambara2>[^\(]+)\( (?P<francais>[^\)]+) \)(?P<transcription1>[^\.]+)\.(?P<transcription2>[^\.]+)\."
)

entries = []

# 2. Lire et parser le fichier CSV
with open(input_csv, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
            
        match = pattern.match(line)
        if match:
            entries.append({
                "bambara": match.group("bambara1").strip(),
                "bambara_variante": match.group("bambara2").strip(),
                "francais": match.group("francais").strip(),
                "transcription": match.group("transcription1").strip(),
                "transcription_variante": match.group("transcription2").strip()
            })
        else:
            print(f"Format non reconnu - ligne ignorée : {line}")

# 3. Nettoyage supplémentaire
df = DataFrame(entries)

# Supprimer les doublons (en gardant la première occurrence)
df = df.drop_duplicates(subset=["bambara"])

# 4. Sauvegarder en CSV propre
df.to_csv(output_csv, index=False, encoding='utf-8')

print(f"Nettoyage terminé. {len(df)} entrées sauvegardées dans {output_csv}")