from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from catalog.models import Product, BlogPost
from pytils.translit import slugify


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product



class ProductListView2(ListView):
    model = Product
    template_name = 'catalog/products.html'


############################################################
class BlogPostListView(ListView):
    model = BlogPost

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'is_published']
    success_url = reverse_lazy('catalog:list_blogpost')

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['content']
    success_url = reverse_lazy('catalog:list_blogpost')
    template_name = 'catalog/blogpost_update.html'

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = slugify(new_post.title)
            new_post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:posts_details', args=[self.kwargs.get('pk')])


class BlogPostDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        object.views_count += 1
        object.save()
        return object


############################################################


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"""Пришли данные:
Имя: {name}
Телефон: {phone}
Сообщение: {message}""")
    return render(request, 'catalog/contacts.html')
