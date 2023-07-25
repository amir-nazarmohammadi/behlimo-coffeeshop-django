from django.db import models
from category.models import Category
from django.urls import reverse
from django.utils.html import format_html
from django.core.exceptions import ValidationError
from django.conf import settings


# limit size image and raise error
def validate_image_size(value):
    limit = settings.FILE_UPLOAD_MAX_MEMORY_SIZE
    if value.size > limit:
        raise ValidationError(f'حجم فایل بیشتر از {limit/1024/1024:.2f} MB است')
    
# Create your models here.
class Menu(models.Model):

    titel = models.CharField(max_length=300,null=True,blank=True,verbose_name='نام آیتم')
    slug = models.CharField(unique=True, max_length=455, verbose_name='نام کوتاه')
    image = models.ImageField(upload_to='menu/', verbose_name='تصویر آیتم',validators=[validate_image_size])
    materials = description = models.TextField(verbose_name='مواد تشکیل دهنده')
    price = models.IntegerField(verbose_name='قیمت')
    is_available = models.BooleanField(default=True ,verbose_name='وضعیت موجودی')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='دسته بندی')
    gallery1 = models.ImageField(blank=True, null=True,upload_to='menu/', verbose_name='گالری 1',validators=[validate_image_size])
    gallery2 = models.ImageField(blank=True, null=True, upload_to='menu/', verbose_name='گالری 2',validators=[validate_image_size])
    gallery3 = models.ImageField(blank=True, null=True, upload_to='menu/', verbose_name='گالری 3',validators=[validate_image_size])
    description = models.TextField(verbose_name='توضحیات آیتم')

    class Meta:
        verbose_name = "منو"
        verbose_name_plural = "آیتم های منو"

    def image_tag(self):
        return format_html('<img src="{}" width="50" height="50" />'.format(self.image.url))

    image_tag.short_description = 'تصویر'

    def get_url(self):
        return reverse('item_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.titel

    