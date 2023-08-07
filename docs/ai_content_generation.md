AI Content Generation
=====================
This repository holds the code to generate the questions and illustrations for quiz game as part of
the Marcel Knowhow Session project.
The code of the Python-based content creation is located in the `src` folder. It is recommended to
use a virtual environment to run the code. The `requirements.txt` file contains all dependencies.
One can also use the Visual Studio Code to run it (as described further below).

# Created Content
The Python script in `./src/main.py` will perform the genaration process and distribute the content
as described in the following paragraphs.
However, it is necessary to ensure that the companion projects `marcel_knowhow_db` and 
`marcel_knowhow_frontend` are also checked out and available with this names on the same directory
level as this project.
```
.
├── ...
├── marcel_knowhow_backend
├── marcel_knowhow_db
├── marcel_knowhow_frontend
├── marcel_knowhow_main
└── ...
```

## Quiz Questions
The quiz questions will be generated in two steps.
1. The direct output from the GPT-4 model will be stored in 
`./ai_questions_export/questions_ai_output.json`.
2. The JSON file will be processed and a Cypher text file to be imported for Neo4j will be created 
and stored in `../marcel_knowhow_db/neo4j_import/questions.cypher`.

## Illustrations
The information fromt the processed JSON file will be used to generate an illustration image for 
each question. The illustration images will be stored in 
`../marcel_knowhow_frontend/public/img/ai_gen` with the pattern
 `illustration_<question_id>.png`.

# Local Development Environment

## Provide a .env file
For creating AI content you will need to have API keys for OpenAI and Stable AI.
Provide these keys in a `.env` file in the root of the project.

Example:
```bash
openai.api_key=<Your_Key>
stableai.api_key=<Your_Key>
```


## Using Visual Studio Code
Inside VSC hit Ctrl+Shift+P and search for `python: create environment`.
Select `.venv`, a Python executable with Python 3.10 or higher and choose to install the dependencies from the requirements.txt file.
You should be able to run and debug the Fast API server by hitting F5 on the main.py file.

## Without Visual Studio Code
It is recommened to create a virtual environment with Python 3.10 or higher.
Given you have Python installed run run the following command in the project's root:
```bash
python3 -m venv .venv
```
Activate the virtual environment with:
```bash
source .venv/bin/activate
```
Install the dependencies with:
```bash
pip install -r requirements.txt
```