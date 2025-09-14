import plotly.express as px
import plotly.io as pio
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Show a datapie based on quantities per products.
figureQtePerProducts = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')
# Show a datapie based on quantities per products.
données["CA"] = données["qte"] * données["prix"]
figureCaPerProducts = px.pie(données, values='CA', names='produit', title="Chiffre d'affaire par produits")

with open("ventes-par-region.html", mode="w", encoding="utf-8") as file:
    file.write(figureQtePerProducts.to_html(full_html=False, include_plotlyjs='cdn'))
    file.write(figureCaPerProducts.to_html(full_html=False, include_plotlyjs=False))

print('ventes-par-région.html généré avec succès !')
