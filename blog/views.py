from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin






# def home(request):
#     posts = [
#         {'name': 'Post1', 'title': 'Django Basics', 'author': 'Rittika'},
#         {'name': 'Post2', 'title': 'Python Tips', 'author': 'John'},
#         {'name': 'Post3', 'title': 'Web Dev', 'author': 'Alice'},
#     ]

#     return render(request, 'blog/home.html', {'posts': posts})

# posts= [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'August 27,2018'
#     },
#     {
#         'author': 'John Doe',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'September 30,2018'
#     }
# ]


# def home(request):
#     postList=Posts.objects.all()
#     return render(request,'blog/home.html',{'posts':postList})

class PostListView(ListView):
    model=Posts
    template_name='blog/home.html'
    context_object_name='posts'
    ordering=['-data_posted']
    paginate_by=5


class UserPostListView(ListView):
    model=Posts
    template_name='blog/user_posts.html'
    context_object_name='posts'
    paginate_by= 5

    def get_queryset(self):
        user = User.objects.get(username=self.kwargs.get('username'))
        return Posts.objects.filter(author=user).order_by('-data_posted')

def about(request):
    return render(request,'blog/about.html',{'title':'About'})

class PostDetailView(DetailView):
    model=Posts

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Posts
    fields=['title','content']
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['title', 'content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False