# 🧠 RAG pour l’assistance culinaire

Ce projet est un système de **RAG (Retrieval-Augmented Generation)** conçu pour aider les utilisateurs à trouver et générer des recettes de cuisine à partir des ingrédients disponibles et d'autres contraintes (régime alimentaire, temps, etc.).

## 📚 Source des données

Nous utilisons un fichier texte simple nommé `recettes.txt` comme source principale, contenant des recettes structurées avec ingrédients, instructions et éventuellement des tags.

## 🏗️ Technologies utilisées

- **Base vectorielle** : [ChromaDB](https://www.trychroma.com/) – utilisée pour construire et gérer notre base de connaissances culinaire.
- **Modèle de langage** : `llama3.2:1b` de [Ollama](https://ollama.com/) – pour générer des suggestions de recettes naturelles et utiles.
- **Framework** : [LangChain](https://www.langchain.com/) – pour gérer le chargement des documents, l'embedding, la recherche et l'interaction avec le LLM.
- **Ingénierie de prompt** : Un prompt personnalisé a été conçu et amélioré pour guider le modèle dans des cas d’usage culinaires précis et pertinents.

## 👥 Membres de l’équipe

- **Zeineb Boussaidi**  
- **Achref Essefi**  
- **Balkis Haj Harrouchi**  
- **Wided Askri**  
- **Nourchene Laroussi**

## 🚀 Étapes d’exécution

### 1. 🔧 Installation des dépendances

Crée un environnement virtuel (optionnel mais recommandé) :

```bash
python -m venv env
source env/bin/activate  # Sur Windows : env\Scripts\activate
````
Installe les dépendances du projet :

```bash
pip install -r requirements.txt
````

### 2. 🤖 Installation de Ollama

Installe Ollama depuis le site officiel :  
👉 [https://ollama.com](https://ollama.com)

Une fois installé, lance cette commande pour télécharger le modèle utilisé dans ce projet :

```bash
ollama pull llama3.2:1b
````

### 3. 🧠 Construction de la base vectorielle

Lance le script suivant pour créer la base de connaissances vectorielle à partir du fichier `recettes.txt`, en utilisant l'embedding `Lajavaness/bilingual-embedding-large` :

```bash
python dbTreatment.py
````
Ce script va :

- Charger et découper les recettes en morceaux exploitables

- Générer les vecteurs d’embedding

- Stocker le tout dans une base vectorielle Chroma

4. 🍽️ Exécution du système RAG
Lance le script principal pour interagir avec le système de génération de recettes assisté par IA :

```bash
python prompt.py
````
Tu pourras ensuite poser des questions comme :
```bash
>> Que puis-je cuisiner avec des œufs et du parmesan ?
````
Le système te proposera des recettes adaptées, basées sur les ingrédients et les contraintes mentionnées.

