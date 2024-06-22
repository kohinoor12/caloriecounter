from django.shortcuts import render
import json
import requests

# Create your views here.


def home(request):
    
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': '6XqEhcXqsCojcB4LIQTlVwBQkFf2Ui3dFs8xPLNp'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'counter/home.html', {'api': api})
    else:
        return render(request, 'counter/home.html', {'query': 'Enter a valid query'})