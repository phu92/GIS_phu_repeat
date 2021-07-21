from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import NewModel


def hello_world(request):
    if request.user.is_authenticated:

        if request.method == "POST":

            temp = request.POST.get('input_text')

            new_model = NewModel()
            new_model.text = temp
            new_model.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))
        else:
            data_list = NewModel.objects.all()
            return render(request, 'accountapp/hello_world.html',
                          context={'data_list': data_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView): #crete view 참조
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    #success_url = reverse_lazy('accountapp:detail') #아직 사용 불가
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)# get 로직이 들어있다.
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)# post 로직이 들어있다.
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'#유저 정보에 접근하기 위해
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)# get 로직이 들어있다.
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args,**kwargs)# post 로직이 들어있다.
        else:
            return HttpResponseForbidden()