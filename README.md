# Neov-Agent

# Steps to Run the .py App
1. Create a Virtual Environment
```sh
    python -m venv .venv
```
2. Activate the Virtual Environment
**On Windows (Command Prompt)**
```sh 
    .venv/Scripts/activate
```
**On macOS/Linux**
```sh 
    source .venv/bin/activate
```
3. Install Requirements 
```sh 
    pip install -r requirements
```
4. Create a .env File
Create a .env file in the project directory and add your OpenAI API key:
use `OPENAI_API_KEY="your-openai-api-key"`
5. Load Data into ChromaDB
```sh
    python load_data.py
```
6. Run the Streamlit App
``` sh
    stramlit run main.py
```
# Using the Notebook
- Add your API key here:
```python
    import os
    os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
```
- Run all notebook cells
- Enter your question using:
```python
    query = "What does NEOV do?"
```
