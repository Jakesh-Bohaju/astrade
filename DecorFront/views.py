from datetime import datetime

from django.shortcuts import render
from django.utils import timezone
import pytz
from django.db.models import Count

from .models import *
from cms.models import *
from CustomAuth.models import *

# Create your views here.
from django.views import View


class BaseView(View):
    suchan = 'CLOSED'
    try:
        opclosing = OpeningClosingDetail.objects.all()
        tz = pytz.timezone('Asia/Kathmandu')
        kat_now = datetime.now(tz)
        current_time = kat_now.strftime('%H')
        for oc in opclosing:
            if oc.status:
                if oc.day_name == kat_now.strftime('%A'):
                    if (int(current_time) - 12) < oc.closing_time and int(current_time) > oc.opening_time:
                        suchana = "OPENING TILL {}{}".format(oc.closing_time, oc.closing_am_pm)
                        suchan = suchana
                    else:
                        suchana = "CLOSED"
                        suchan = suchana
            else:
                suchana = "CLOSED"
                suchan = suchana
    except:
        pass

    template_context = {
        'header': FrontHeader.objects.order_by('-id'),
        'navbar_pages': Page.objects.filter(navbar=True),
        'categories': Category.objects.order_by('title').all(),
        'services': Services.objects.filter(status=True),
        'product': Product.objects.order_by('?').all(),
        'contact': ContactUs.objects.order_by('-id'),
        'profile': Profile.objects.order_by('-id'),
        'message': suchan
    }

    def post(self, request, page_slug):
        pass


class HomePage(BaseView):
    def get(self, request):
        self.template_context['banners'] = Banner.objects.filter(published=True).order_by('-weight')
        self.template_context['festival'] = FestivalGreeting.objects.filter(status=True).order_by('-id')
        self.template_context['opcolsing'] = OpeningClosingDetail.objects.filter(status=True)

        categories = Category.objects.annotate(Count('product'))
        aa = categories.values_list('title', 'product__count')
        self.template_context['product_count'] = aa
        count_review = SiteReview.objects.filter(choice='Review')
        self.template_context['happy_client'] = count_review.count()
        self.template_context['reviews'] = count_review
        self.template_context['welcome_message'] = WelcomeMessage.objects.filter(status=True).order_by('-id')
        self.template_context['brand_logo'] = BrandLogo.objects.filter(status=True)

        return render(request, 'index.html', self.template_context)


def error_404(request, exception):
    data = {}
    return render(request, '404error.html', data)


def error_500(request):
    data = {}
    return render(request, '500error.html', data)
