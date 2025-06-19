import torch
print(torch.__version__)  # Doit afficher 2.0+
print(torch.cuda.is_available())  # Vérifie si CUDA fonctionne

from transformers import pipeline  # Ne devrait plus donner d'erreur