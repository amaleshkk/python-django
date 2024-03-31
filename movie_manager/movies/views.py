from django.shortcuts import render, redirect, get_list_or_404
from . models import MovieInfo
from . forms import MovieForm

# Create your views here.

def create(request):
    frm = MovieForm()
    if request.POST:
        frm = MovieForm(request.POST)
        # title = request.POST.get('title')
        # year = request.POST.get('year')
        # summary = request.POST.get('summary')
        # movie_obj = MovieInfo(title=title, year=year, summary=summary)
        # movie_obj.save()
        if frm.is_valid:
            frm.save()
        else:
            frm = MovieForm()

            
    return render(request, 'create.html', {'frm': frm})

def list(request):
    # movie_data ={
    #     'movies': [
    #         {
    #             'title' : "John wick",
    #             'year': 2014,
    #             'summary' : 'John Wick, a legendary hitman who comes out of retirement to seek revenge against the men who killed his dog, a final gift from his recently deceased wife.',
    #             'success' : True,
    #             'img' : 'johnwick.jpeg'
    #         },
    #         {
    #             'title' : "The Dark Knight",
    #             'year': 2008,
    #             'summary' : 'Based on the DC Comics superhero Batman, it is the sequel to Batman Begins (2005) and the second installment in The Dark Knight Trilogy.',
    #             'success' : True,
    #             'img': 'darkknight.jpeg'
    #         },
    #         {
    #             'title' : "lucy",
    #             'year': 2014,
    #             # 'summary' : 'A woman, accidentally caught in a dark deal, turns the tables on her captors and transforms into a merciless warrior evolved beyond human logic.',
    #             'success' : True,
    #             'img' : 'lucy.jpeg'
    #         }
    #     ]
    # }

    movie_set = MovieInfo.objects.all()
    
    # return render(request, 'list.html', movie_data)
    return render(request, 'list.html', {'movies': movie_set})

# def edit(request, pk):
#     instance_edit = MovieInfo.objects.get(pk = pk)
#     if request.POST:
#         title = request.POST.get('title')
#         year = request.POST.get('year')
#         summary = request.POST.get('summary')
#         instance_edit.title = title
#         instance_edit.year = year
#         instance_edit.summary = summary
#         instance_edit.save()

#     frm = MovieForm(instance=instance_edit)
#     return render(request, 'create.html', {'frm': frm})


def edit(request, pk):
    instance_edit = MovieInfo.objects.get(pk = pk)
    if request.POST:
        frm = MovieForm(request.POST, instance=instance_edit)
        if frm.is_valid():
            instance_edit.save()
    else:
        frm = MovieForm(instance=instance_edit)
    return render(request, 'create.html', {'frm': frm})

def delete(request, pk):
    instance = MovieInfo.objects.get(pk = pk)
    instance.delete()
    movie_set = MovieInfo.objects.all()
    return render(request,'list.html', {'movies': movie_set})

# def delete(request, movie_id):
#     movie_obj = get_list_or_404(MovieInfo, id=movie_id)
    
#     if request.method == 'POST':
#         # Delete the MovieInfo object
#         movie_obj.delete()
#         # Redirect to a success URL
#         return redirect('success_url')

#     return render(request, 'delete.html', {'movie_obj': movie_obj})