from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.views.generic import *
from .models import *
from .forms import *
from django.db.models import Q
from django.urls import reverse_lazy,reverse
from django.contrib.auth import login,logout,authenticate
class PostDetailView(DetailView):
    model=Post
    template_name='post_view.html'

class HomeView(ListView):
    model=Post
    template_name='index.html'
    
class AddPostView(CreateView):
    model=Post
    template_name='add_post.html'
    fields='__all__'
    # def form_valid(self, form):
    #     form.instance.author=self.request.user
    #     form.instance.save()
    #     return super().form_valid(form)
    


class EditPostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='edit_post.html'

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
    
class SignUpView(CreateView):
    template_name='sign_up.html'
    form_class=SignUpForm
    success_url=reverse_lazy('home')
    def form_valid(self,form):
        username=form.cleaned_data.get('name')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        
        user=User.objects.create_user(username,email,password)
        
        form.instance.user=user
        login(self.request,user)
        
        return super().form_valid(form)
    
class LogOutView(TemplateView):
    def get(self,request):
        logout(request)
        return redirect('home')

    
class LogInView(FormView):
    template_name='log_in.html'
    form_class=LogInForm
    success_url=reverse_lazy('home')

    def form_valid(self, form):
        uname=form.cleaned_data.get("username")
        pword=form.cleaned_data.get("password")
        usr = authenticate(username=uname,password=pword)
        if usr is not None and hasattr(usr,'account') and usr.account:
            login(self.request,usr)
        elif usr is not None and hasattr(usr,'user') and usr.user:
            login(self.request,usr)
        else:
            return render(self.request,self.template_name,{'form':self.form_class,'error':'Invalid username or password'})
        return super().form_valid(form)

class UserDetail(TemplateView):
    template_name='user.html'
    
class SearchView(TemplateView):
	template_name="search.html"
	def get_context_data(self, **kwargs):
		keyword=self.request.GET.get("keyword")
		context=super().get_context_data(**kwargs)
		if keyword!="":
			results=Post.objects.filter(Q(body__icontains=keyword)|Q(author__icontains=keyword)|Q(category__icontains=keyword))
		else:
			results=Post.objects.none()
		context["results"]=results
		return context

class AddCommentView(CreateView):
    model=Comment
    form_class=CommentForm
    template_name='add_comment.html'
    def form_valid(self,form):
        form.instance.author = self.request.user
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)
    def get_success_url(self):
        return reverse_lazy('post-view', kwargs={'pk': self.kwargs['pk']})
    


# def details(request, id):
# 	myproduct=Member.objects.get(id=id)
# 	#Create a context dictionary
# 	template = loader.get_template('details.html')
# 	#Load the template
# 	context = {
# 	'myproduct': myproduct,
# 	}
# 	return HttpResponse(template.render(context, request))
