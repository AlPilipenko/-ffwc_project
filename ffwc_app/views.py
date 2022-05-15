from django.shortcuts import render, redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.urls import reverse_lazy
from .models import User_Data, Weight_Update


from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
"custom method for user creations"

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


# Create your views here.

class PersonalPage(ListView, LoginRequiredMixin):
    model = User_Data
    context_object_name = 'user_data'
    template_name = 'ffwc_app/personal_page.html'

    def get_context_data(self, **kwargs):
        """ To see user specific data in the personal page.
        """
        context = super().get_context_data(**kwargs)
        context['user_data'] = context['user_data'].filter(user=self.request.user)
        context['weight_update'] = Weight_Update.objects.all().filter(
                                                    user=self.request.user.id)
        return context


class TestDetail(DetailView):
    pass
    model = User_Data
    context_object_name = 'test'
    template_name = 'ffwc_app/test_detail.html'


class InputWeight(CreateView, LoginRequiredMixin):
    model = Weight_Update
    # fields = ('weight_update', )
    fields = ['weight_update']
    # context_object_name = 'weight'
    context_object_name = 'weight_record'
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        """Because one model is related to other, I encountered
        'must be an instance of other model' error.
        """
        form.instance.user_id = self.request.user.id
        return super(InputWeight, self).form_valid(form)


class EditWeightRecord(UpdateView, LoginRequiredMixin):
    model = Weight_Update
    # fields = ('weight_update', )
    fields = ['weight_update']
    # context_object_name = 'weight'
    # context_object_name = 'weight_record'
    template_name = 'ffwc_app/edit_weight_update_form.html'
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super(EditWeightRecord, self).form_valid(form)


class ChangeUserDetails(UpdateView, LoginRequiredMixin):
    model = User_Data
    # fields = ('weight_update', )
    fields = ['name', 'weight', 'goal_weight', 'height']
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ChangeUserDetails, self).form_valid(form)


class CreateUserDetails(CreateView, LoginRequiredMixin):
    model = User_Data
    # fields = ('weight_update', )
    fields = ['name', 'weight', 'goal_weight', 'height']
    success_url = reverse_lazy('account')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateUserDetails, self).form_valid(form)

class Group(ListView):
    model = User_Data
    context_object_name = 'user_data'

    template_name = 'ffwc_app/group.html'


'____________________________________________________'

class CustomLoginView(LoginView):
    template_name = 'ffwc_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('group')


class RegisterPage(FormView):
    template_name = 'ffwc_app/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('group')

    def form_valid(self, form):
        """When reg form is valid return logedin user to the group page"""
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('group')
        return super(RegisterPage, self).get(*args, **kwargs)
