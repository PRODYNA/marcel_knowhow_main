import json
import os

from Item import Item
from jni_openai import OpenAi
from jni_stable_diffusion import StableDiffusion
from jni_cypher import create_cypher


AI_OUTPUT_REL_PATH = "ai_questions_export/questions_ai_output.json"
DB_IMPORT_REL_PATH = "../marcel_knowhow_db/neo4j_import/questions.cypher"
FE_IMPORT_REL_PATH = "../marcel_knowhow_frontend/public/img/ai_gen"
NO_QUESTIONS = 50


def write_questions_to_json_file() -> None:
	open_ai = OpenAi()
	ai_questions = open_ai.create_quizz_questions(NO_QUESTIONS)

	with open(AI_OUTPUT_REL_PATH, "w") as file:
		file.write(ai_questions)
	print(f"Questions written to {AI_OUTPUT_REL_PATH}")


def read_questions_from_json_file() -> list[Item]:
	items: list[Item] = []
	with open(AI_OUTPUT_REL_PATH, "r") as file:
		ai_questions = file.read()
		questions: list[dict] = json.loads(ai_questions)
		for question in questions:
			item = Item(question["id"], question["question"], question["yes_answer"])
			items.append(item)
	no_items = len(items)
	if no_items == 0:
		raise Exception("No items found in json file")
	print(f"Read {no_items} items from {AI_OUTPUT_REL_PATH}")
	return items


def create_db_import_file(items: list[Item]) -> None:
	cypher = create_cypher(items)
	with open(DB_IMPORT_REL_PATH, "w") as file:
		file.write(cypher)
	print(f"Import written to {DB_IMPORT_REL_PATH}")


def create_question_illustrations(items: list[Item]) -> None:
	stable_diffusion = StableDiffusion(FE_IMPORT_REL_PATH)
	for item in items:
		stable_diffusion.createIllustration(item.question, str(item.id))
	print(f"Illustrations written to {FE_IMPORT_REL_PATH}")


def main() -> None:
	if not os.path.exists((os.path.dirname(DB_IMPORT_REL_PATH))):
		raise Exception(f"Directory {DB_IMPORT_REL_PATH} does not exist for db import file") 
	if not os.path.exists(FE_IMPORT_REL_PATH):
		raise Exception(f"Directory {FE_IMPORT_REL_PATH} does not exist for frontend import")

	write_questions_to_json_file()
	items = read_questions_from_json_file()
	create_db_import_file(items)
	create_question_illustrations(items)


if __name__ == "__main__":
	main()
