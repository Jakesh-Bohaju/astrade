from django.db import models

# Create your models here.
from DecorFront.imageresize import image_resize, logo_resize
from DecorFront.validator import phone_no_validation, mobile_no_validation

day_choices = (
    ("Sunday", "Sunday"),
    ("Monday", "Monday"),
    ("Tuesday", "Tuesday"),
    ("Wednesday", "Wednesday"),
    ("Thursday", "Thursday"),
    ("Friday", "Friday"),
    ("Saturday", "Saturday"),
)

am_pm_choice = (
    ("AM", "AM"),
    ("PM", "PM"),
)


class FrontHeader(models.Model):
    company_name = models.CharField(max_length=50)
    logo = models.ImageField()

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        super(FrontHeader, self).save(*args, **kwargs)
        logo_resize(self.logo.path)
        super(FrontHeader, self).save(*args, **kwargs)


class Banner(models.Model):
    title = models.CharField(max_length=10)
    caption = models.CharField(max_length=200)
    image = models.ImageField()
    weight = models.IntegerField()
    published = models.BooleanField()

    def __str__(self):
        return self.title + '(' + str(self.weight) + ')'


class Page(models.Model):  # always singular name for model
    title = models.CharField(max_length=70)
    menu_title = models.CharField(max_length=70)
    content = models.TextField()
    published = models.BooleanField()
    navbar = models.BooleanField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    proprietary = models.CharField(max_length=50)
    country = models.CharField(max_length=15)
    province = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    ward_no = models.IntegerField()
    phone1_no = models.CharField(max_length=10, validators=[mobile_no_validation])
    phone2_no = models.CharField(max_length=10, validators=[mobile_no_validation], blank=True, null=True)
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    facebook_page_link = models.CharField(max_length=1000, blank=True, null=True)
    facebook_page_name = models.CharField(max_length=150, blank=True, null=True)
    instagram_page_link = models.CharField(max_length=1000, blank=True, null=True)
    instagram_page_name = models.CharField(max_length=150, blank=True, null=True)
    twitter_page_link = models.CharField(max_length=1000, blank=True, null=True)
    twitter_page_name = models.CharField(max_length=150, blank=True, null=True)
    linkedin_page_link = models.CharField(max_length=1000, blank=True, null=True)
    linkedin_page_name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.proprietary

    def save(self, *args, **kwargs):
        super(ContactUs, self).save(*args, **kwargs)
        image_resize(self.image.path)
        super(ContactUs, self).save(*args, **kwargs)


class Services(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(AboutUs, self).save(*args, **kwargs)
        image_resize(self.image.path)
        super(AboutUs, self).save(*args, **kwargs)


class FestivalGreeting(models.Model):
    title = models.CharField(max_length=100)
    greeting_message = models.TextField()
    image = models.ImageField()
    status = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title


class OpeningClosingDetail(models.Model):
    day_name = models.CharField(max_length=15, choices=day_choices, unique=True)
    opening_time = models.IntegerField()
    opening_am_pm = models.CharField(max_length=2, choices=am_pm_choice)
    closing_time = models.IntegerField()
    closing_am_pm = models.CharField(max_length=2, choices=am_pm_choice)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.day_name


class WelcomeMessage(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
