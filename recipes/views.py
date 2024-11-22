from django.shortcuts import render
from projeto.utils.recipes.factory import make_recipe

def home(request):
    return render(request, 'pages/home.html', context={'recipes':[make_recipe() for _ in range(10)],})


def recipe(request, id):
    return render(request, 'pages/recipe-view.html', context={'recipe': make_recipe(),
    'is_detail_page': True,
    })
    