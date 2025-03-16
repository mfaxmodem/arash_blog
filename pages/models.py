from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class Page(models.Model):
    title = models.CharField(_('عنوان'), max_length=200)
    slug = models.SlugField(_('اسلاگ'), max_length=200, unique=True, allow_unicode=True)
    content = models.TextField(_('محتوا'))
    featured_image = models.ImageField(_('تصویر شاخص'), upload_to='pages/', blank=True)
    created_at = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True)
    updated_at = models.DateTimeField(_('تاریخ بروزرسانی'), auto_now=True)
    # SEO fields
    meta_title = models.CharField(_('عنوان متا'), max_length=200, blank=True)
    meta_description = models.TextField(_('توضیحات متا'), blank=True)
    meta_keywords = models.CharField(_('کلمات کلیدی متا'), max_length=300, blank=True)
    
    is_published = models.BooleanField(_('منتشر شده'), default=True)  # type: ignore
    
    class Meta:
        verbose_name = _('صفحه')
        verbose_name_plural = _('صفحات')
    
    def __str__(self) -> str:
        return str(self.title)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
