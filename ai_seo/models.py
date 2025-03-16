from django.db import models
from django.utils.translation import gettext_lazy as _

class AIGeneratedContent(models.Model):
    keyword = models.CharField(_('کلمات کلیدی'), max_length=200)
    generated_title = models.CharField(_('عنوان تولید شده'), max_length=200, blank=True)
    generated_content = models.TextField(_('محتوای تولید شده'), blank=True)
    generated_meta_description = models.TextField(_('توضیحات متا تولید شده'), blank=True)
    created_at = models.DateTimeField(_('تاریخ ایجاد'), auto_now_add=True)
    
    class Meta:
        verbose_name = _('محتوای تولید شده با هوش مصنوعی')
        verbose_name_plural = _('محتواهای تولید شده با هوش مصنوعی')
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return str(self.keyword)
