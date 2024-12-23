from django.shortcuts import render,redirect
from django.views.generic import TemplateView,DetailView,FormView
from AdminApp.models import Blog
from .forms import CommentForm
from .models import Comment
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

class ViewerHomeView(TemplateView):
    template_name="viewer.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["blog"]=Blog.objects.all()
        return context

    
class ViewerDetailView(TemplateView):
    template_name = "viewer_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog=Blog.objects.get(id=kwargs["id"])
        context['blog']=blog
        context['form']=CommentForm()
        context['comments']=Comment.objects.filter(blog=blog)
        return context
        


    def post(self, request, *args, **kwargs):
        
        blog=Blog.objects.get(id=kwargs["id"])
        form = CommentForm(request.POST)
        if form.is_valid():
            blog=Blog.objects.get(id=kwargs["id"])
            Comment.objects.create(
                blog=blog,
                user=self.request.user,
                description=form.cleaned_data["description"]
            ) 
            messages.success(request,"Comment posted!")
            return redirect('viewerdetail_view',id=blog.id)

class AddCommentView(FormView):
    form_class=CommentForm
    model=Comment
    success_url=reverse_lazy('viewerdetail_view')

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"Comment Added!")
        return super().form_valid(form)
