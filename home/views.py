from django.shortcuts import render


def home(request):
    context = {
        "title": "Home",
        "text2": "HOME"
    }

    return render(request,
                  'home/index.html',
                  context,
                  )
