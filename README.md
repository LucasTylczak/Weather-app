# Weather App

Ce script Python permet de récupérer les prévisions météorologiques pour les trois prochains jours d'une ville donnée.

## Description

Ce script utilise l'API OpenWeatherMap pour obtenir les prévisions météorologiques. Il utilise également la bibliothèque `googletrans` pour traduire les termes météorologiques en français. L'utilisateur doit fournir le nom de la ville pour obtenir des prévisions précises.

## Fonctionnalités

- Traduit les termes météorologiques en français pour une meilleure lisibilité.
- Affiche les conditions météorologiques, la température et l'humidité pour chaque jour (aujourd'hui, demain, après-demain).

## Utilisation

1. Clonez ce dépôt sur votre machine locale.

### Kali Linux
```bash
pip install googletrans==4.0.0-rc1
git clone https://github.com/LucasTylczak/Weather-app.git
cd Weather-app
python3 Weather-app.py
```

### Windows Powershell
```bash
pip install googletrans==4.0.0-rc1
git clone https://github.com/LucasTylczak/Weather-app.git
cd .\Weather-app\
python .\Weather-app.py
```

2. Entrez le nom de la ville.

3. Les prévisions météorologiques pour les trois prochains jours seront affichées.

## Exemple

```bash
Entrez le nom de la ville: Paris

Jour 1 - 2024-02-03 12:00:00
Conditions météorologiques: Nuageux - Nuages épars
Température: 8.5 °C
Humidité: 65%

Jour 2 - 2024-02-04 12:00:00
Conditions météorologiques: Ensoleillé - Ciel dégagé
Température: 10.2 °C
Humidité: 57%

Jour 3 - 2024-02-05 12:00:00
Conditions météorologiques: Pluie - Pluie légère
Température: 6.8 °C
Humidité: 72%
```
