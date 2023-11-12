from django.db import models

from modelcluster.fields import ParentalManyToManyField
from wagtail.fields import RichTextField
from wagtail.models import Page  
from wagtail.admin.panels import FieldPanel 
from wagtail.search import index


class OppurtunityIndexPage(Page):
    intro = models.CharField(blank=True, max_length=250)
    
    def children(self):
        return self.get_children().specific().live()

    def get_context(self, request):
        context = super().get_context(request)
        oppupages = self.get_children().live().order_by('-first_published_at')
        context['oppupages'] = oppupages 
        context['header'] = self.intro
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class OppurtunityPage(Page):
    STATUS = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
        ('Coming Soon', 'Coming Soon')
    )
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    organisation = ParentalManyToManyField('event.Organisation', blank=True)
    status = models.CharField(max_length=20, choices=STATUS) 

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro', help_text="Subject of Oppurtunity"),
        FieldPanel('date'),
        FieldPanel('status'),
        FieldPanel('organisation'),
        FieldPanel('body'),
    ]

