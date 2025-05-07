import requests

parametros = {
    'amount': 5,
    'type': 'boolean',
    'category': 9,
    'difficulty': 'medium',
}

URL_QUIZ = 'https://opentdb.com/api.php'


resposta_api = requests.get(url=URL_QUIZ, params=parametros)
resposta_api.raise_for_status()
resultado = resposta_api.json()

question_data = resultado['results']
