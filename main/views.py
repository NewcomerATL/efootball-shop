from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406355893',
        'name': 'Anderson Tirza Liman',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)