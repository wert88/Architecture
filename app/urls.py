from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('signup/', views.UserFormView.as_view(), name='signup'),
	path('about_us/', views.AboutUs.as_view(), name='about'),
	path('contact_us/', views.ContactUs.as_view(), name='contact_us'),
	path('pic/', views.PicView.as_view(), name='pic'),
	path('pic2/', views.PicView2.as_view(), name='pic2'),
	path('pic3/', views.PicView3.as_view(), name='pic3'),
	path('pic4/', views.PicView4.as_view(), name='pic4'),
	#path('gallery/', views.Gallery.as_view(), name='gallery'),

]
