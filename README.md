# Research Assistant

An assistant where you can extract relevant information just by dropping a URL into it. 
The user can drop URLs and ask questions to receive relevant insights from that doc. 

---
## Features
-  Drop and process the URL to fetch article content.
- The content is fetched using Web Base Loader powered by Langchain.
- The extracted content is divided into chunks using the Recursive text splitter.
- Construct a vector store to store embeddings of these chunks into ChromaDB to enable swift retrieval of relevant content.
- Queries are created using the Langchain Prompt template and provide flexibility to the user and their queries.
- Interacts with the LLM(llama 3 via Groq) by inputting queries to receive answers with the source URL.

---
## Architecture of Research Assistant
![Architecture](assets/architecture.png)

## 🧠 Tech Stack

### Backend & Core
- Python
- LangChain
- Chroma Vector Database
- Groq LLMs (Llama 3.3)
- HuggingFace Embeddings (Alibaba-NLP/gte-base-en-v1.5)

### Document Processing
- Web scraping (WebBaseLoader)
- Text chunking (RecursiveCharacterTextSplitter)
- Prompt templates (PromptTemplate)

### Utilities
- Environment configuration with `.env`
- UUID-based document/session IDs

---
## Set-Up
1. Clone the repository
``` bash
  git clone https://github.com/itsmoksh/research-assistant.git
```
2. Run the following command to install all dependencies.
``` bash
  pip install -r requirements.txt
```
3. Create a new .env file with your Groq credentials as follows:
```text
   GROQ_API_KEY = GROQ API KEY HERE
```
4. Run the streamlit app using:
``` bash
  streamlit run main.py
```
---
## Streamlit UI
Here's the screenshot of how the Research Assistant Chatbot works. The article used in this demo 
It's from "The Hindu", and it's about Google's new Gen-AI model.

![Question1](assets/sc1.png)
The URL is processed first, converts the article into a document and chunks it. These chunks are stored in the Chroma. 
Database in the form of embeddings. Then, it's ready to give the answers.

![Question2](assets/sc2.png)
Here's the next question, asked by the bot, about the model capabilities and the purpose of launching the model.

---
**Try it out**:
**[Open Streamlit App](https://moksh-research-assistant.streamlit.app/)**

**Moksh Jain**

[LinkedIn](https://www.linkedin.com/in/itsmoksh/) • [GitHub](https://github.com/itsmoksh) • [Portfolio](https://codebasics.io/portfolio/Moksh-Jain)