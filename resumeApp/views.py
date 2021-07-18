from django.shortcuts import redirect, render
from .models import *

default_data = {
    'app_name': 'My Resume'
}

# Create your views here.

# load Personal Info 
def load_personal_info():
    default_data['personal_info'] = User.objects.all()[::-1]

# load all Skills 
def load_skills():
    default_data['skills'] = Skill.objects.all()[::-1]

# load work Experience
def load_experiences():
    default_data['experiences'] = Experience.objects.all()[::-1]

# load all languages
def load_languages():
    default_data['languages'] = Language.objects.all()[::-1]

# load education
def load_educations():
    default_data['educations'] = Education.objects.all()[::-1]

def index(request):
    load_personal_info()
    load_skills()
    load_experiences()
    load_languages()
    load_educations()

    return render(request, 'index.html ', default_data)

# show resume page
def resume_page(request):
    return render(request, 'resume.html', default_data)

# login page
def login_page(request):
    return render(request, 'login_page.html', default_data)

# login functionality
def login(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.POST['email'])

        if request.POST['password'] == master.Password:
            request.session['email'] = request.POST['email']
            
        return redirect(profile_page)
    else:
        return redirect(profile_page)

# register page
def register_page(request):
    return render(request, 'register_page.html', default_data)

# register functionality
def register(request):
    if request.method == 'POST':
        master = Master.objects.create(
            Email=request.POST['email'],
            Password=request.POST['password'],
            IsActive = True
        )

        User.objects.create(Master=master)

        return redirect(register_page)
    else:
        return redirect(register_page)

# load profile data
def profile_data(request):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)

    education = Education.objects.filter(User = user)[::-1]
    experience = Experience.objects.filter(User = user)[::-1]
    skill = Skill.objects.filter(User = user)[::-1]
    language = Language.objects.filter(User = user)[::-1]

    default_data['user_data'] = {
        'user': user,
        'education': education,
        'skill': skill,
        'language': language,
        'experience': experience
    }


# profile page
def profile_page(request):
    profile_data(request)
    return render(request, 'profile_page.html', default_data)

# update profile
def update_profile(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])
        user = User.objects.get(Master=master)

        user.FullName = request.POST['FullName']
        user.JobProfile = request.POST['JobProfile']
        user.Mobile = request.POST['Mobile']
        user.Gender = request.POST['Gender']
        user.Address = request.POST['Address']

        if 'profile_pic' in request.FILES:
            user.ProfilePic = request.FILES['profile_pic']

        user.save()

        return redirect(profile_page)
    else:
        pass

# update education
def update_education(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])
        user = User.objects.get(Master=master)
        education = Education()

        education.User = user
        education.Board = request.POST['Board']
        education.Standard = request.POST['Standard']
        education.StartDate = request.POST['StartDate']
        education.EndDate = request.POST['EndDate']
        education.IsContinue = True if 'IsContinue' in request.POST else False

        education.save()

        return redirect(profile_page)
    else:
        pass

# remove education
def remove_education(request, pk):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)

    Education.objects.get(User=user, pk=pk).delete()

    return redirect(profile_page)

# update experience
def update_experience(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])
        user = User.objects.get(Master=master)
        experience = Experience()

        experience.User = user
        experience.JobProfile = request.POST['JobProfile']
        experience.StartDate = request.POST['StartDate']
        experience.EndDate = request.POST['EndDate']
        experience.IsContinue = True if 'IsContinue' in request.POST else False
        
        experience.save()

        return redirect(profile_page)
    else:
        pass

# remove experience
def remove_experience(request, pk):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)

    Experience.objects.get(User=user, pk=pk).delete()

    return redirect(profile_page)

# update language
def update_language(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])
        user = User.objects.get(Master=master)
        language = Language()

        language.User = user
        language.LangName = request.POST['LangName']
        language.Level = request.POST['Level']
        
        language.save()

        return redirect(profile_page)
    else:
        pass

# remove language
def remove_language(request, pk):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)

    Language.objects.get(User=user, pk=pk).delete()

    return redirect(profile_page)

# update skill
def update_skill(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])
        user = User.objects.get(Master=master)
        skill = Skill()

        skill.User = user
        skill.Skill = request.POST['skill']
        skill.Level = request.POST['Level']
        
        skill.save()

        return redirect(profile_page)
    else:
        pass

# remove skill
def remove_skill(request, pk):
    master = Master.objects.get(Email=request.session['email'])
    user = User.objects.get(Master=master)

    Skill.objects.get(User=user, pk=pk).delete()

    return redirect(profile_page)

# change password
def change_password(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])
                
        print(request.POST)
        
        if request.POST['cur_password'] == master.Password:
            master.Password=request.POST['new_password']
            master.save()

        return redirect(profile_page)
    else:
        return redirect(profile_page)

# deactivate account
def deactivate_acc(request):
    if request.method == 'POST':
        master = Master.objects.get(Email=request.session['email'])

    if request.POST['deactivate_password'] == master.Password:
        master.IsActive = False
        master.save()

        return redirect(profile_page)   

# logout
def logout(request):
    if 'email' in request.session:
        del request.session['email']
    return redirect(index)     
