# Neov-Agent

# Steps to run .py app
1. create venv 
```sh
    python -m venv .venv
```
2. activate the envirenoment 
```sh 
    .venv/Scripts/activate
```
3. install requirements 
```sh 
    pip install -r requirements
```
4. create .env file with variable OPENAI_API_KEY= "OpenAI key api"
5. load data to chroma db
```sh
    python load_data.py
```
6. run the app
``` sh
    stramlit run main.py
```
# using the notebook
add the api key here 'os.environ["OPENAI_API_KEY"] = ""' and run all from here and
here you can enter your question'query = "What does NEOV do?"'
