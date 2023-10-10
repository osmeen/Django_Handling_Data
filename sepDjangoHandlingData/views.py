from django.shortcuts import render


def home(request):
    return render(request, template_name='index.html')


def register(request):
    received_name = request.POST.get("name")
    received_email = request.POST.get("email")
    received_password = request.POST.get("password")
    context = {
        "jina": received_name,
        "arafa": received_email,
        "siri": received_password
    }
    return render(request, 'register.html', context)

