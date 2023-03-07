from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm,MyPasswordResetForm
urlpatterns = [
    path('', views.index, name=''),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path('product-detail/<int:id>',
         views.ProductDetail.as_view(), name='product-detail'),
    path('category-title/<val>',
         views.CategoryTitle.as_view(), name='category-title'),

    path('profile',views.ProfileView.as_view(),name='profile'),
    path('address', views.address, name='address'),
    path('updateAddress/<int:id>', views.updateAddress.as_view(), name='updateAddress'),



    # Login,Register
    path('registration', views.CustomerRegistrationView.as_view(),
         name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html',
                                                        authentication_form=LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html',
         form_class=MyPasswordResetForm), name='password_reset'),
]
