from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company
from django.core.urlresolvers import reverse_lazy
# Create your views here.
class CompanyList(ListView):
    model=Company

class CompanyDetail(DetailView):
    model=Company

class CompanyCreateView(CreateView):
    model=Company
    fields='__all__'

class CompanyUpdateView(CreateView):
    model=Company
    fields='__all__'
