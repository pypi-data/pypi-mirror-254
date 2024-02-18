import os
import requests

API_URL = 'https://api.func.live'

def fetch_functions():
    response = requests.get(f"{API_URL}/functions")
    functions = response.json().get('functions', [])

    def create_function(func_name):
        def func(input_data):
            try:
                response = requests.post(f"{API_URL}/functions/{func_name}",
                                         headers={
                                             'Authorization': f'Bearer {os.getenv("FUNC_TOKEN")}',
                                             'Accept': 'application/json',
                                             'Content-Type': 'application/json'
                                         },
                                         json={'input': input_data})
                return response.json().get('output')
            except requests.RequestException as e:
                raise Exception(f"There was an error: {str(e)}")

        return func

    return {func['name']: create_function(func['name']) for func in functions}

func_live = fetch_functions()
# result = func_live['qrcode']('https://www.wakeflow.io')
# print(result)
