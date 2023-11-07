from django.db import models
from django import forms

from modelcluster.fields import ParentalManyToManyField
from wagtail.fields import RichTextField
from wagtail.models import Page  
from wagtail.admin.panels import FieldPanel,  MultiFieldPanel  
from wagtail.search import index
from wagtail.snippets.models import register_snippet

@register_snippet
class Organisation(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    about = RichTextField(blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('logo'),
        FieldPanel('about')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Organisations"


class EventIndexPage(Page):
    intro = models.CharField(blank=True, max_length=250)
    
    def get_context(self, request):
        context = super().get_context(request)
        eventpages = self.get_children().live().order_by('-first_published_at')
        context['eventpages'] = eventpages
        context['header'] = self.intro
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]


class EventPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    organiser = ParentalManyToManyField('event.Organisation', blank=True)
    event_date = models.DateTimeField(blank=True)
    thumbnail = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('intro', help_text="Subject of Event"),
            FieldPanel('date'),
            FieldPanel('event_date'),
            FieldPanel('organiser', widget=forms.CheckboxSelectMultiple),
        ], heading="Event information"),
        FieldPanel('body'),
        FieldPanel('thumbnail'),
    ]

