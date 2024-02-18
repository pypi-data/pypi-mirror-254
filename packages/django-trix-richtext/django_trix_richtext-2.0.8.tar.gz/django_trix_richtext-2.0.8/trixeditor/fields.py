from django.db import models
from .widgets import TrixRichText


class TrixRichTextField(models.TextField):
    def formfield(self, **kwargs):
        kwargs['widget'] = TrixRichText(attrs={'id': 'trix-rich-text'})
        return super(TrixRichTextField, self).formfield(**kwargs)
