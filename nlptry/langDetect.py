from textblob import TextBlob
from langdetect import detect

textArr = [
    'Ein, zwei, drei, vier',
    '我不觉的这个很OK',
    'OK,你赢了',
    'bonjour',
    'J\'ai reçu ce velo dans les délais mais au montage la fourche est si tordue que les passage de roue font un angle de 30 degrés avec la perpendiculaire au vélo',
]

for text in textArr:
    b = TextBlob(text)
    lang1 = b.detect_language()
    lang2 = detect(text)

    print(text,"\t\t\t\t:",lang1, "\t", lang2)
