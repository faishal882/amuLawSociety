from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel 


class HomePage(Page):
    """
    The Home Page. This looks slightly more complicated than it is. You can
    see if you visit your site and edit the homepage that it is split between
    a:
    - Hero area
    - Body area
    - Moveable featured site sections
    """

    # Hero section of HomePage
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Homepage image",
    )
    hero_text = models.CharField(
        max_length=255, help_text="Write motto"
    )
    

    # Body section of the HomePage
    body = RichTextField(
        verbose_name="Home content block",
        blank=True,
        help_text="Write your vision for AMU LAW SOCIETY"
    )

    # Featured sections on the HomePage
    # You will see on templates/base/home_page.html that these are treated
    # in different ways, and displayed in different areas of the page.
    # Each list their children items that we access via the children function
    # that we define on the individual Page models e.g. BlogIndexPage
    featured_section_1_title = models.CharField(
        blank=True, max_length=255, help_text="Title to display for featured_section_1"
    )
    featured_section_1 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="First featured section for the homepage.",
        verbose_name="Featured section 1",
    )

    featured_section_2_title = models.CharField(
        blank=True, max_length=255, help_text="Title to display for featured_section_2"
    )
    featured_section_2 = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Second featured section for the homepage.",
        verbose_name="Featured section 2",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
                FieldPanel("hero_text"),
            ],
            heading="Hero section",
        ),
        FieldPanel("body"),
        MultiFieldPanel(
            [
                MultiFieldPanel(
                    [
                        FieldPanel("featured_section_1_title"),
                        FieldPanel("featured_section_1"),
                    ]
                ),
                MultiFieldPanel(
                    [
                        FieldPanel("featured_section_2_title"),
                        FieldPanel("featured_section_2"),
                    ]
                ),
            ],
            heading="Featured homepage sections",
        ),
    ]

    def __str__(self):
        return self.title

