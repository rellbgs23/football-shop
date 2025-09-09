from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2406406780',
        'name': 'Farrel Rifqi Bagaskoro',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)