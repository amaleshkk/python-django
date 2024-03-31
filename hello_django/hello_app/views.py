from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hello(request):
    movie_data ={
        'movies': [
            {
                'title' : "John wick",
                'year': 2014,
                'summary' : 'John Wick, a legendary hitman who comes out of retirement to seek revenge against the men who killed his dog, a final gift from his recently deceased wife.',
                'success' : True
            },
            {
                'title' : "The Dark Knight",
                'year': 2008,
                'summary' : 'Based on the DC Comics superhero Batman, it is the sequel to Batman Begins (2005) and the second installment in The Dark Knight Trilogy.',
                'success' : True
            },
            {
                'title' : "Lucy",
                'year': 2014,
                # 'summary' : 'A woman, accidentally caught in a dark deal, turns the tables on her captors and transforms into a merciless warrior evolved beyond human logic.',
                'success' : True
            }
        ]
    }
    return render(request, 'hello.html', movie_data)
    # return HttpResponse("<b>hello from views.py<b>")



