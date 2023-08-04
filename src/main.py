import json

from jni_openai import OpenAi


AI_OUTPUT_REL_PATH = "ai_questions_export/questions_ai_output.json"
DB_IMPORT_REL_PATH = "neo4j_import/questions_import.cypher"
NO_QUESTIONS = 50


class Item:
	def __init__(self, id: int, question: str, yes_answer: bool):
		self.id = id
		self.question = question
		self.yes_answer = yes_answer


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
	with open(DB_IMPORT_REL_PATH, "w") as file:
		for item in items:
			file.write(f' \
			CREATE (q:Question {{\n \
				id: {item.id},\n \
				question: "{item.question}", \n \
				yes_answer: {item.yes_answer}\n \
			}});\n\n')
	print(f"Import written to {DB_IMPORT_REL_PATH}")


def main() -> None:
	write_questions_to_json_file()
	items = read_questions_from_json_file()
	create_db_import_file(items)


if __name__ == "__main__":
	main()
