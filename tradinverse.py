from transformers import pipeline

traducteur = pipeline(
    "translation",
    model="facebook/nllb-200-distilled-600M",
    src_lang="bam_Latn",
    tgt_lang="fra_Latn"
)

print(traducteur("I ni ce"))  # Output: "Bonjour"