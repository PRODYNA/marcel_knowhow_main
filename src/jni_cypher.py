from Item import Item


def create_cypher(items: list[Item]) -> str:
	cypher = 'CREATE (c:Creation {\n \
		create_date: datetime(), \n \
		source: "AI" \n \
	})\n'	

	for i, item in enumerate(items):
		cypher = f'{cypher} \
			CREATE (q{i}:Question {{\n \
				id: {item.id},\n \
				question: "{item.question}", \n \
				yes_answer: {item.yes_answer}\n \
			}})\n \
			CREATE (c)-[:CREATED]->(q{i})\n\n'
	cypher = f'{cypher};'
	return cypher
