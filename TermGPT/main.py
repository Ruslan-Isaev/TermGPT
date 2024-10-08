import requests
import io
import sys

def main_function():
	arguments = sys.argv[1:]
	if len(arguments) < 1:
		print("Не указаны аргументы!\n\nПример использования:\ngpt {вопрос} - задает вопрос ChatGPT\ngpt --file {путь} - ищет текст, указанный в файле.\n\nСохранение контекста отсутствует!")
		return
	elif arguments[0] == "--file":
		if len(arguments) > 1:
			try:
			             with open(arguments[1], 'r') as file:
			             	question = file.read()  

			except Exception as e:
				print(f'Error: {e}'
)
				return
		else:
			print("Вы не указали путь!")
	else:
		question = ' '.join(arguments)
	prompt = [{"role": "user", "content": question}]
	response = requests.post('http://api.onlysq.ru/ai/v1', json=prompt)
	response_json = response.json()
	if 'answer' in response_json:
	               answer = response_json['answer']
	               answer = answer.replace("GPT >>", "").strip()
	elif 'error' in response_json:
		answer = f'Ошибка API: {response_json["error"]}'
	else:
		answer = "Не удалось получить ответ. Проверьте API."
	print(answer)
	
