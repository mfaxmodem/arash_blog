from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class MenuItem(models.Model):
    title = models.CharField(_('عنوان'), max_length=100)
    slug = models.SlugField(_('اسلاگ'), max_length=100, unique=True, allow_unicode=True)
    url = models.CharField(_('آدرس URL'), max_length=200, blank=True)
    parent = models.ForeignKey('self', verbose_name=_('منوی والد'), on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    order = models.IntegerField(_('ترتیب'), default=0)  # type: ignore
    is_active = models.BooleanField(_('فعال'), default=True)  # type: ignore
    
    class Meta:
        verbose_name = _('آیتم منو')
        verbose_name_plural = _('آیتم‌های منو')
        ordering = ['order']
    
    def __str__(self) -> str:
        return str(self.title)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
