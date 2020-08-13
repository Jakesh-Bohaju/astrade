from django.db import models
from PIL import Image
# Create your models here.
from DecorFront.imageresize import image_resize, logo_resize
from DecorFront.validator import name_validation

Review_Choices = (
    ("Review", 'Review',),
    ("Feedback", 'Feedback')
)


class Category(models.Model):
    title = models.CharField(max_length=25, validators=[name_validation])
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    brand = models.CharField(max_length=25, blank=True, null=True)
    price = models.FloatField()
    pub_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def image(self):
        return self.producthasimage_set.first()


class ProductHasImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        super(ProductHasImage, self).save(*args, **kwargs)
        image_resize(self.image.path)
        super(ProductHasImage, self).save(*args, **kwargs)


class Gallery(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    slug = models.SlugField(unique=True)
    status = models.BooleanField(default=False)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Gallery, self).save(*args, **kwargs)
        image_resize(self.image.path)
        super(Gallery, self).save(*args, **kwargs)


DEFAULT = 'avatar.png'


class SiteReview(models.Model):
    user = models.CharField(max_length=80, validators=[name_validation])
    comment = models.TextField()
    image = models.ImageField(blank=True, null=True, default=DEFAULT)
    choice = models.CharField(max_length=15, choices=Review_Choices)
    pub_date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.user


class BrandLogo(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(BrandLogo, self).save(*args, **kwargs)
        logo_resize(self.image.path)
        super(BrandLogo, self).save(*args, **kwargs)
