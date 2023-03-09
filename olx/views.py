from django.shortcuts import render,redirect
from olx.forms import RegistrationForm,LoginForm,UserCreationForm,UserProfile,UserForm
from django.views.generic import View,FormView,CreateView,TemplateView,ListView,DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from olx.forms import ProductForm
from olx.models import Products
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
# from django.http import HttpResponse
# from olx.models import chatMessages
# from django.db.models import Q
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User as UserModel
# import json,datetime




def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login")
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

decs=[signin_required,never_cache]


class IndexView(ListView):
    template_name="index.html"
    context_object_name="products"
    model=Products



class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,"login.html",{"form":form})


class SignUpView(CreateView):
    template_name="register.html"
    form_class=RegistrationForm
    success_url=reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(self.request,"account has been created")
        return super().form_valid(form)


class UserProfileView(CreateView):
    template_name="user-profile.html"
    form_class=UserCreationForm
    success_url=reverse_lazy("signin")
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"profile has been created")
        return super().form_valid(form)




def Edit_profile(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance=request.user)
        form=UserCreationForm(request.POST,request.FILES,instance=request.user)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='Edit_profile')
    else:
        user_form = UserCreationForm(instance=request.user)
        profile_form = UserCreationForm(instance=request.user)

        return render(request,'profile-edit.html')

class ProductCreateView(CreateView):
   template_name="product-add.html"
   form_class=ProductForm
   success_url=reverse_lazy("home")

   def form_valid(self, form):
    form.instance.user=self.request.user
    messages.success(self.request,"product has been added")
    return super().form_valid(form)

   def form_invalid(self,form):
        messages.error(self.request,"coudn,t add product")
        return super().form_invalid(form)


@method_decorator(decs,name="dispatch")
class ProductDetailView(DetailView):
    template_name="product-detail.html"
    context_object_name="product"
    pk_url_kwarg="id"
    model=Products

decs
def logout_view(request,*args,**kwargs):
    logout(request)
    messages.success(request,"logged out")
    return redirect("signin")

# def send_chat(request):
#     resp = {}
#     User = get_user_model()
#     if request.method == 'POST':
#         post =request.POST
        
#         u_from = UserModel.objects.get(id=post['user_from'])
#         u_to = UserModel.objects.get(id=post['user_to'])
#         insert = chatMessages(user_from=u_from,user_to=u_to,message=post['message'])
#         try:
#             insert.save()
#             resp['status'] = 'success'
#         except Exception as ex:
#             resp['status'] = 'failed'
#             resp['mesg'] = ex
#     else:
#         resp['status'] = 'failed'

#     return HttpResponse(json.dumps(resp), content_type="application/json")   