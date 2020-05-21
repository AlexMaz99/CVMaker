from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from home.models import University, Address, UserData

from accounts.forms import InterestsForm, ContactInfoForm, ExperienceForm, SkillsForm, LanguagesForm, ProjectsForm, \
    OrganizationsForm, EducationForm, UniversityForm, NewCV
from home.models import UserData, Cv, ContactInfo, Experience, Skills, Languages, Interests, Projects, Organizations, \
    Education, University, Address


def start_page(request):
    return render(request, 'home/start.html')


def cv_list(request):
    user_data = UserData.objects.get(user_id=request.user.id)
    context = {
        'cvs':user_data.current_cvs
    }
    return render(request, 'home/cv_list.html', context)


def view_cv(request, cv_number=0):
    user_data = UserData.objects.get(user_id=request.user.id)
    cv = user_data.current_cvs[cv_number]

    context = {
        "name": cv.name,
        "description":cv.description,
        "cv_number": cv_number
    }
    return render(request, 'home/view_cv.html', context)

# def view_cv(PDFTemplateView, cv_number=0):
#     template_name = "hello.html"
# print(request.user.id)
# user_data = UserData.objects.get(user_id=request.user.id)
# cv = user_data.current_cvs[cv_number]
#
#
# context = {
#     "name": cv.name
# }
# return render(request, 'home/view_cv.html', context)
def add_new_cv(request):
    if request.method == 'POST':
        form = NewCV(request.POST)
        if form.is_valid():
            user_data = UserData.objects.get(user_id=request.user.id)
            cv = Cv(contact_info=ContactInfo(),
                    education=[],
                    experience=[],
                    skills=[],
                    languages=[],
                    interests=[],
                    projects=[],
                    organizations=[],
                    description=form.cleaned_data['description'],
                    name=form.cleaned_data['name']
                    )
            user_data.current_cvs.append(cv)
            user_data.save()
            return render(request, 'home/add_cv_inf.html',
                          {'cv_number': len(user_data.current_cvs) - 1, 'form': ContactInfoForm(), 'isValid': True})
        else:
            return render(request, 'home/add_new_cv.html',
                          {'form': NewCV(), 'isValid': False})
    else:
        return render(request, 'home/add_new_cv.html',
                      {'form': NewCV(), 'isValid': False})


def add_cv_inf(request, cv_number):
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            user_data = UserData.objects.get(user_id=request.user.id)
            user_data.current_cvs[cv_number].contact_info = ContactInfo(
                city=form.cleaned_data['city'],
                country=form.cleaned_data['country'],
                phone=form.cleaned_data['phone'],
                github=form.cleaned_data['github'],
                linkedin=form.cleaned_data['linkedin'],
                personal_website=form.cleaned_data['personal_website'],
                email=form.cleaned_data['email']
            )
            user_data.save()
            return render(request, 'home/add_cv_inf.html',
                          {'cv_number': cv_number, 'form': ContactInfoForm(), 'isValid': True})
        else:
            return render(request, 'home/add_cv_inf.html',
                          {'cv_number': cv_number, 'form': ContactInfoForm(), 'isValid': False})
    else:
        return render(request, 'home/add_cv_inf.html',
                      {'cv_number': cv_number, 'form': ContactInfoForm(), 'isValid': False})


def add_data(request, cv_number, forms_number):
    # Experience
    if forms_number == 0:
        if request.method == 'POST':
            form = ExperienceForm(request.POST)
            if form.is_valid():
                user_data = UserData.objects.get(user_id=request.user.id)
                user_data.current_cvs[cv_number].experience.append(Experience(
                    start=form.cleaned_data['start'],
                    end=form.cleaned_data['end'],
                    company=form.cleaned_data['company'],
                    position=form.cleaned_data['position'],
                    description=form.cleaned_data['description']
                ))
                user_data.save()
                return render(request, 'home/add_data.html',
                              {'form': ExperienceForm(), 'isValid': True, 'name': "experience",
                               'forms_number': forms_number, 'cv_number': cv_number})
            else:
                return render(request, 'home/add_data.html',
                              {'form': ExperienceForm(), 'isValid': False, 'name': "experience",
                               'forms_number': forms_number, 'cv_number': cv_number})
        else:
            return render(request, 'home/add_data.html',
                          {'form': ExperienceForm(), 'isValid': False, 'name': "experience",
                           'forms_number': forms_number, 'cv_number': cv_number})

    # Skills
    elif forms_number == 1:
        if request.method == 'POST':
            form = SkillsForm(request.POST)
            if form.is_valid():
                user_data = UserData.objects.get(user_id=request.user.id)
                user_data.current_cvs[cv_number].skills.append(Skills(
                    name=form.cleaned_data['name']
                ))
                user_data.save()
                return render(request, 'home/add_data.html',
                              {'form': SkillsForm(), 'isValid': True, 'name': "skills", 'forms_number': forms_number,
                               'cv_number': cv_number})
            else:
                return render(request, 'home/add_data.html',
                              {'form': SkillsForm(), 'isValid': False, 'name': "skills", 'forms_number': forms_number,
                               'cv_number': cv_number})
        else:
            return render(request, 'home/add_data.html',
                          {'form': SkillsForm(), 'isValid': False, 'name': "skills", 'forms_number': forms_number,
                           'cv_number': cv_number})

    # Languages
    elif forms_number == 2:
        if request.method == 'POST':
            form = LanguagesForm(request.POST)
            if form.is_valid():
                user_data = UserData.objects.get(user_id=request.user.id)
                user_data.current_cvs[cv_number].languages.append(Languages(
                    name=form.cleaned_data['name'],
                    description=form.cleaned_data['description']
                ))
                user_data.save()
                return render(request, 'home/add_data.html',
                              {'form': LanguagesForm(), 'isValid': True, 'name': "languages",
                               'forms_number': forms_number, 'cv_number': cv_number})
            else:
                return render(request, 'home/add_data.html',
                              {'form': LanguagesForm(), 'isValid': False, 'name': "languages",
                               'forms_number': forms_number, 'cv_number': cv_number})
        else:
            return render(request, 'home/add_data.html',
                          {'form': LanguagesForm(), 'isValid': False, 'name': "languages",
                           'forms_number': forms_number, 'cv_number': cv_number})

    # Interests
    elif forms_number == 3:
        if request.method == 'POST':
            form = InterestsForm(request.POST)
            if form.is_valid():
                user_data = UserData.objects.get(user_id=request.user.id)
                user_data.current_cvs[cv_number].interests.append(Interests(
                    name=form.cleaned_data['name']
                ))
                user_data.save()
                return render(request, 'home/add_data.html',
                              {'form': InterestsForm(), 'isValid': True, 'name': "interests",
                               'forms_number': forms_number, 'cv_number': cv_number})
            else:
                return render(request, 'home/add_data.html',
                              {'form': InterestsForm(), 'isValid': False, 'name': "interests",
                               'forms_number': forms_number, 'cv_number': cv_number})
        else:
            return render(request, 'home/add_data.html',
                          {'form': InterestsForm(), 'isValid': False, 'name': "interests",
                           'forms_number': forms_number, 'cv_number': cv_number})

    # Projects
    elif forms_number == 4:
        if request.method == 'POST':
            form = ProjectsForm(request.POST)
            if form.is_valid():
                user_data = UserData.objects.get(user_id=request.user.id)
                user_data.current_cvs[cv_number].projects.append(Projects(
                    name=form.cleaned_data['name'],
                    description=form.cleaned_data['description']
                ))
                user_data.save()
                return render(request, 'home/add_data.html',
                              {'form': ProjectsForm(), 'isValid': True, 'name': "projects",
                               'forms_number': forms_number, 'cv_number': cv_number})
            else:
                return render(request, 'home/add_data.html',
                              {'form': ProjectsForm(), 'isValid': False, 'name': "projects",
                               'forms_number': forms_number, 'cv_number': cv_number})
        else:
            return render(request, 'home/add_data.html', {'form': ProjectsForm(), 'isValid': False, 'name': "projects",
                                                          'forms_number': forms_number, 'cv_number': cv_number})

    # Organizations
    elif forms_number == 5:
        if request.method == 'POST':
            form = OrganizationsForm(request.POST)
            if form.is_valid():
                user_data = UserData.objects.get(user_id=request.user.id)
                user_data.current_cvs[cv_number].organizations.append(Organizations(
                    name=form.cleaned_data['name'],
                    description=form.cleaned_data['description']
                ))
                user_data.save()
                return render(request, 'home/add_data.html', {'form': OrganizationsForm(), 'isValid': True,
                                                              'name': "organizations", 'forms_number': forms_number,
                                                              'cv_number': cv_number})
            else:
                return render(request, 'home/add_data.html', {'form': OrganizationsForm(), 'isValid': False,
                                                              'name': "organizations", 'forms_number': forms_number,
                                                              'cv_number': cv_number})
        else:
            return render(request, 'home/add_data.html', {'form': OrganizationsForm(), 'isValid': False,
                                                          'name': "organizations", 'forms_number': forms_number,
                                                          'cv_number': cv_number})

    # Education
    elif forms_number == 6:
        if request.method == 'POST':
            form = EducationForm(request.POST)
            if form.is_valid():
                user_data = UserData.objects.get(user_id=request.user.id)
                university_name = form.cleaned_data['university']

                university = None
                universities = University.objects.all()
                for i in universities:
                    if i.name == university_name:
                        university = i
                        break
                user_data.current_cvs[cv_number].education.append(Education(
                    start=form.cleaned_data['start'],
                    end=form.cleaned_data['end'],
                    field_of_study=form.cleaned_data['field_of_study'],
                    degree=form.cleaned_data['degree'],
                    faculty=form.cleaned_data['faculty'],
                    university=university
                ))
                user_data.save()
                return render(request, 'home/add_data.html', {'form': EducationForm(), 'isValid': True,
                                                              'name': "education", 'forms_number': forms_number,
                                                              'cv_number': cv_number})
            else:
                return render(request, 'home/add_data.html', {'form': EducationForm(), 'isValid': False,
                                                              'name': "education", 'forms_number': forms_number,
                                                              'cv_number': cv_number})
        else:
            return render(request, 'home/add_data.html', {'form': EducationForm(), 'isValid': False,
                                                          'name': "education", 'forms_number': forms_number,
                                                          'cv_number': cv_number})
    elif forms_number == 7:
        if request.method == 'POST':
            form = UniversityForm(request.POST)
            if form.is_valid():
                university = University(
                    name=form.cleaned_data['name'],
                    address=Address(
                        street=form.cleaned_data['street'],
                        street_number=form.cleaned_data['street_number'],
                        zip=form.cleaned_data['zip'],
                        city=form.cleaned_data['city']
                    )
                )
                university.save()
                return render(request, 'home/add_data.html', {'form': UniversityForm(), 'isValid': True,
                                                              'name': "university", 'forms_number': forms_number,
                                                              'cv_number': cv_number})
            else:
                return render(request, 'home/add_data.html', {'form': UniversityForm(), 'isValid': False,
                                                              'name': "university", 'forms_number': forms_number,
                                                              'cv_number': cv_number})
        else:
            return render(request, 'home/add_data.html', {'form': UniversityForm(), 'isValid': False,
                                                          'name': "university", 'forms_number': forms_number,
                                                          'cv_number': cv_number})
