from django.db import models
from django.utils.html import format_html
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.conf import settings


# limit size image and raise error
def validate_image_size(value):
    limit = settings.FILE_UPLOAD_MAX_MEMORY_SIZE
    if value.size > limit:
        raise ValidationError(f'حجم فایل بیشتر از {limit/1024/1024:.2f} MB است')

class Category(models.Model):
    titel = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    slug = models.CharField(unique=True, max_length=255, verbose_name='نام کوتاه')
    image = models.ImageField(upload_to='media/', verbose_name='تصویر دسته بندی',validators=[validate_image_size])
    description = models.TextField(verbose_name='توضیحات دسته بندی')

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def get_url(self):
        return reverse('menu_by_category',args=[self.slug])

    def image_tag(self):
        return format_html('<img src="{}" width="50" height="50" />'.format(self.image.url))

    image_tag.short_description = 'تصویر'

    def __str__(self):
        return self.titel
