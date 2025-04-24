# 🧠 RAG for Culinary Assistance

This project is a **Retrieval-Augmented Generation (RAG)** system designed to help users find and generate cooking recipes based on available ingredients and other constraints (diet, time, etc.).

## 📚 Data Source

We used a simple text file named `recettes.txt` as our primary data source, containing structured recipes with ingredients, instructions, and optional tags.

## 🏗️ Technology Stack

- **Vector Store**: [ChromaDB](https://www.trychroma.com/) – used to build and manage our recipe knowledge base.
- **Language Model**: `llama3.2:1b` from [Ollama](https://ollama.com/) – for generating helpful, natural-sounding recipe suggestions.
- **Framework**: [LangChain](https://www.langchain.com/) – to handle document loading, embedding, retrieval, and LLM interaction.
- **Prompt Engineering**: We designed and iteratively improved a custom prompt template tailored for culinary use cases to guide the language model in providing relevant and accurate suggestions.

## 👥 Team Members

- **Zeineb Boussaidi**  
- **Achref Essefi**  
- **Balkis Haj Harrouchi**  
- **Wided Askri**  
- **Nourchene Laroussi**

---

This RAG system demonstrates how AI can be applied to enhance daily life through accessible and personalized cooking assistance.
