from django.shortcuts import render, redirect

# Create your views here.
from DecorFront.forms import ReviewForm
from DecorFront.views import BaseView
from cms.models import *
from DecorFront.models import *


class PageView(BaseView):
    def get(self, request, page_slug):
        self.template_context['page'] = Page.objects.get(slug=page_slug)
        self.template_context['aboutus'] = AboutUs.objects.order_by('-id')
        galleries = Gallery.objects.order_by('?')
        products = Product.objects.order_by('?')
        allgallery = []
        for product in products:
            allgallery.append(product)
        for gallery in galleries:
            allgallery.append(gallery)
        self.template_context['galleries'] = allgallery

        return render(request, 'page.html', self.template_context)

    def post(self, request, page_slug):
        form = ReviewForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            # review_choice = request.POST.get('cou')
            # r_choice = review_choice.objects.get(country_name=country)
            # form.country_id = con.id
            form.save()
            return redirect('/')

        else:
            print(form.errors)
            # return render(request, 'page.html', {'form': form})
            # return redirect('/menu/contact-us', {'form': form})

        # return redirect('index')


        return render(request, 'page.html', {'form': form, 'page': Page.objects.get(slug=page_slug)})
