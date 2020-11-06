from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms
from . import models

BODY_TEMPLATE = (
    '{title} at {uri} was recommended to you by {name}.\n\n'
    'Comment: {comment}'
)


#
#
class MaterialListView(ListView):   #(LoginRequiredMixin,ListView)
    queryset = models.Material.objects.all()
    context_object_name = 'materials'
    template_name = 'materials/all_materials.html'




# def all_materials(request):
#     material_list = models.Material.objects.all()
#     return render(request,
#                   'materials/all_materials.html',
#                   {'materials': material_list})

@login_required
def material_details(request, year, month, day, slug):
    material = get_object_or_404(models.Material,
                                 slug=slug,
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)

    new_comment = None
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.material = material
            new_comment.save()
            return redirect(material)

    else:
        comment_form = forms.CommentForm()

    return render(request,
                  'materials/detail.html',
                  {'material': material,
                   'form': comment_form,
                   'was_added': new_comment})


def _prepare_mail(cd, request, material):
    material_uri = request.build_absolute_uri(
        material.get_absolute_url()
    )

    body = BODY_TEMPLATE.format(title=material.title,
                                uri=material_uri,
                                name=cd['name'],
                                comment=cd['comment'])

    subject = "{name}({email}) recommends you {title}".format(
        name=cd['name'],
        email=cd['my_email'],
        title=material.title,
    )

    return subject, body


def share_material(request, material_id):
    material = get_object_or_404(models.Material,
                                 id=material_id)
    sent = False
    if request.method == 'POST':
        form = forms.EmailMaterialForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject, body = _prepare_mail(cd, request, material)
            send_mail(subject, body, 'arturm.m@bk.ru', [cd['to_email'], ])
            sent = True
    else:
        form = forms.EmailMaterialForm()

    return render(request,
                  'materials/share.html',
                  {'material': material,
                   'form': form,
                   'sent': sent})


def user_login(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                username=cd['username'],
                password=cd['password'],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('OK!!')

                else:
                    return HttpResponse('не активный!')
            else:
                return HttpResponse('Проверьте логин или пароль!')
    else:
        form = forms.LoginForm()
        return render(request, 'login.html', {'form': form})


@login_required
def view_profile(request):
    return render(request, 'profile.html', {'user': request.user})

def register(request):
    if request.method == "POST":
        user_form = forms.UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'],
            )
            new_user.save()
            models.Profile.objects.create(user=new_user,
                                          photo='unknown.jpg')
            return render(request, 'registration_complete.html',
                          {'new_user': new_user})
    else:
        user_form = forms.UserRegistrationForm()
    return render(request, 'registration.html', {'form': user_form})


def edit_user(request):
    if request.method == "POST":
        user_form = forms.UserEditForm(data=request.POST,
                                       instance=request.user)
        profile_form = forms.ProfileEditForm(data=request.POST,
                                             instance=request.user.profile,
                                             files=request.FILES)
        user_form.save()
        profile_form.save()
        return render(request,
                      'profile.html',
                      {'user': request.user})
    else:
        user_form = forms.UserEditForm(instance=request.user)
        profile_form = forms.ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'edit_profile.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})