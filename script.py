# Fonction pour générer un synonyme différent pour "Belle Bite" avec genre accordé et première lettre en majuscule
from datetime import datetime, timedelta
import json
import random

result = []
adjectives_masculine = ["Superbe", "Magnifique", "Splendide", "Impressionnant", "Étonnant", "Exquis", "Remarquable", "Exceptionnel", "Incroyable", "Admirable"]
adjectives_feminine = ["Superbe", "Magnifique", "Splendide", "Impressionnante", "Étonnante", "Exquise", "Remarquable", "Exceptionnelle", "Incroyable", "Admirable"]
nouns_masculine = ['Membre', 'Organe', 'Élément reproducteur', 'Fragment de virilité', 'Morceau de viande', 'Composant à foutre', 'Phallus', 
                    'Manche', 'Bâton', 'Engin', 'Dard', 'Gland', 'Zizi', 'Sexe', 'Appendice', 'Attribut', 'Outil', 'Braquemart',
                    'Popol', 'Zob',  'Bijou', 'Biroute', 'Bitonio', 'Bout', 'Braquemard', 'Calibre', 'Cierge', 'Colt', 
                    'Dague', 'Dard', 'Fusil', 'Gourdin', 'Javelot', 'Jonc', 'Kiki', 'Lance', 'Mat', 'Matraque', 'Paf', 'Pal', 
                    'Péniche', 'Pilou', 'Piquet', 'Pistil', 'Pistolet', 'Poireau', 'Popaul', 'Segment fragile', 'Tronçon du bas']
nouns_feminine = ['Parties', 'Pièce du boucher', 'Portion de sexe', 'Pine' 'Zigounette', 'Queue', 'Verge'  ]

for adjective in adjectives_masculine:
    for noun in nouns_masculine:
        result.append(f"{adjective} {noun}, Shinji !")
for adjective in adjectives_feminine:
    for noun in nouns_feminine:
        result.append(f"{adjective} {noun}, Shinji !")
random.shuffle(result)
datas = result[:365] 

# Génération du tableau pour chaque jour de l'année avec les corrections
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
one_day = timedelta(days=1)
synonyms_dict_corrected = {}

while start_date <= end_date:
    date_key = start_date.strftime("%m%d")
    day_of_year = (start_date - datetime(start_date.year, 1, 1)).days
    synonyms_dict_corrected[date_key] = result[day_of_year]
    start_date += one_day

# Conversion en JSON
file_path = 'dump.json'
with open(file_path, 'w') as file:
    json.dump(synonyms_dict_corrected, file, indent=4, ensure_ascii=False)

