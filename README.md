# 🌟 TP4 Python POO – Polymorphisme & Classes Abstraites

[![Python Version](https://img.shields.io/badge/Python-3.x-blue)](https://www.python.org/)
[![Made With Love](https://img.shields.io/badge/Made%20with-Love-red.svg)]()

Bienvenue dans le dépôt du **TP4 de Programmation Orientée Objet en Python**, un ensemble d'exercices orientés vers le **polymorphisme**, les **classes abstraites**, et la manipulation de **collections d’objets hétérogènes**.

Ce README suit une présentation professionnelle inspirée des projets open-source pour rendre le dépôt clair, propre et attractif.

---

## 📁 Aperçu du Projet

Le TP est composé de **trois exercices**, chacun illustrant un concept POO clé :

### 🔹 Exercice 1 — Polymorphisme : "Les Animaux"

Mise en place d'une interface commune permettant de tester la substitution dynamique.

* Classe de base : `Animal`
* Sous-classes : `Chien`, `Chat`, `Vache`
* Fonction polymorphe : `faire_parler()`
* Test du *duck typing* avec une classe `Robot`
* Liste d'objets variés

---

### 🔹 Exercice 2 — Classes Abstraites : "Les Formes Géométriques"

Utilisation du module `abc` pour forcer l’implémentation de méthodes.

* Classe abstraite : `Forme` (`@abstractmethod aire()`)
* Formes concrètes : `Cercle`, `Rectangle`, `Triangle`
* Extension : `Carre` dérivé de `Rectangle`
* Calcul d'aires via polymorphisme
* Redéfinition de `__str__`

---

### 🔹 Exercice 3 — Système de Paiements

Application réaliste démontrant héritage + abstraction + polymorphisme.

* Classe abstraite : `Paiement`
* Sous-classes spécialisées :

  * `CarteBancaire`
  * `PayPal`
  * `Crypto`
* Fonction générique : `traiter_paiements()`
* Vérification des montants & gestion d'erreurs

---

## 🚀 Installation & Utilisation

### 1. Cloner le dépôt

```bash
git clone https://github.com/M4ds1ck/TP4_Python_OOP.git
```

### 2. Accéder à un exercice (par ex. EXERCICE3)

```bash
cd TP4_Python_OOP/EXERCICE3
```

### 3. Lancer les scripts

```bash
cd EXERCICE1 // EXERCICE 2 & EXERCICE 3
python test.py
```

---

## 🖥️ Exemples d’exécution

### ▶️ Exercice 1 — Animaux

```bash
Ouaf !
Miaou !
Meuh !
Ouaf !
```

### ▶️ Exercice 2 — Formes Géométriques

```bash
Cercle – aire : 28.27
Rectangle – aire : 20.00
Triangle – aire : 6.00
```

### ▶️ Exercice 3 — Paiements

```bash
Test montant négatif
.Test Carte Bancaire
Paiement Carte Bancaire de 100.00€ validé (Finissant par ****5678)
.Test Crypto
Paiement Crypto de 2.50 sur réseau BTC (Wallet: WALLET_ID)
.Test PayPal
Paiement PayPal de 50.00€ envoyé à test@test.com
.
----------------------------------------------------------------------
Ran 4 tests in 0.010s

OK
```

---

## 📦 Structure du Dépôt

```
TP4_Python_OOP/
├── EXERCICE1/
│   ├── animaux.py
│   └── test.py
├── EXERCICE2/
│   ├── formes.py
│   └── test.py
├── EXERCICE3/
│   ├── paiements.py
│   └── test.py
└── README.md
```

---

## 🙌 Auteur
**Nom :** Mahmoud Moukouch - 2333447 - [m.moukouch2471@uca.ac.ma](mailto:m.moukouch2471@uca.ac.ma) 

**GitHub :** [M4ds1ck](https://github.com/M4ds1ck)

**Projet :** TP4 – Polymorphisme & Classes Abstraites

---
