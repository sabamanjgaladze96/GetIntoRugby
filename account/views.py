from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def teampage(request):
    return render(request, 'teampage.html', {'team_name':'',
                                             'established':'',
                                             'division': '',
                                             'subdivision':'',
                                             'age_group': '',
                                             'training_ground_address': '',
                                             'contact_phone':'',
                                             'contact_email': '',
                                             'youtube_embed_link': '',})