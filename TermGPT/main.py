import requests
import io

def main_function():
	question = input("GPT>>$ ")
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
	