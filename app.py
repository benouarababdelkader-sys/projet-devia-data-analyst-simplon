import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

# Graphique 1 : ventes (quantités) par produit
figure_ventes = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')
figure_ventes.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

# Graphique 2 : chiffre d'affaires par produit
# Le chiffre d'affaires = prix x quantité, on crée donc une nouvelle colonne
données['chiffre_affaires'] = données['prix'] * données['qte']
figure_ca = px.pie(données, values='chiffre_affaires', names='produit', title="chiffre d'affaires par produit")
figure_ca.write_html('chiffre-affaires-par-produit.html')
print('chiffre-affaires-par-produit.html généré avec succès !')
