from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel 
from wagtail.search import index


class NoticeIndexPage(Page):
    intro = models.CharField(blank=True, max_length=250)
    
    def get_context(self, request):
        context = super().get_context(request)
        noticepages = self.get_children().live().order_by('-first_published_at')
        context['noticepages'] = noticepages
        context['header'] = self.intro
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class NoticePage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', help_text="HeadTitle for Notice"),
        FieldPanel('date'),
        FieldPanel('body'),
    ]

