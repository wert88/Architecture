from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserForm, CustomAuthenticationForm, ContactForm
from django.contrib.auth import authenticate, login
from .models import Picture, Picture2, Picture3, Picture4

class IndexView(View):
	def get(self, request):
		return render(request, 'app/index.html')

class AboutUs(View):
	def get(self, request):
		return render(request, 'app/about.html')

class ContactUs(View):
	form = ContactForm()
	def get(self, request):
		form = self.form
		return render(request, 'app/contact.html', {'form': form})

	def post(self, request):
		form = self.form
		if form.is_valid():
			form = self.form(request.POST)
			user = form.save(commit=False)
			user.save()
		return render(request, 'app/index.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'app/signup.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
        return render(request, self.template_name, {'form': form})
		
class PicView(View):
	def get(self, request):
		pics = Picture.objects.all()
		return render(request, 'app/pic.html', {'pics':pics})

class PicView2(View):
	def get(self, request):
		pics = Picture2.objects.all()
		return render(request, 'app/pic2.html', {'pics':pics})
		
class PicView3(View):
	def get(self, request):
		pics = Picture3.objects.all()
		return render(request, 'app/pic3.html', {'pics':pics})

class PicView4(View):
	def get(self, request):
		pics = Picture4.objects.all()
		return render(request, 'app/pic4.html', {'pics':pics})
