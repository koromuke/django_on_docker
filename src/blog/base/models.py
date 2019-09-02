from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtail.admin.edit_handlers import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Collection, Page
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet

# from .blocks import BaseStreamBlock

"""
Createable pages used in CodeRed CMS.
"""
from modelcluster.fields import ParentalKey
from coderedcms.forms import CoderedFormField
from coderedcms.models import (
    CoderedEmail,
    CoderedFormPage,
    CoderedWebPage
)



"""
Createable pages used in CodeRed CMS.
"""

class FormPage(CoderedFormPage):
    """
    A page with an html <form>.
    """
    class Meta:
        verbose_name = 'Form'

    template = 'coderedcms/pages/form_page.html'


class FormPageField(CoderedFormField):
    """
    A field that links to a FormPage.
    """
    class Meta:
        ordering = ['sort_order']

    page = ParentalKey('FormPage', related_name='form_fields', on_delete=models.CASCADE)

class FormConfirmEmail(CoderedEmail):
    """
    Sends a confirmation email after submitting a FormPage.
    """
    page = ParentalKey('FormPage', related_name='confirmation_emails', on_delete=models.CASCADE)


class WebPage(CoderedWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    Template renders all Navbar and Footer snippets in existance.
    """
    class Meta:
        verbose_name = 'Web Page'

    template = 'coderedcms/pages/web_page.html'






# bakerydemo



# @register_snippet
# class People(index.Indexed, ClusterableModel):
#     """
#     A Django model to store People objects.
#     It uses the `@register_snippet` decorator to allow it to be accessible
#     via the Snippets UI (e.g. /admin/snippets/base/people/)
#
#     `People` uses the `ClusterableModel`, which allows the relationship with
#     another model to be stored locally to the 'parent' model (e.g. a PageModel)
#     until the parent is explicitly saved. This allows the editor to use the
#     'Preview' button, to preview the content, without saving the relationships
#     to the database.
#     https://github.com/wagtail/django-modelcluster
#     """
#     first_name = models.CharField("First name", max_length=254)
#     last_name = models.CharField("Last name", max_length=254)
#     job_title = models.CharField("Job title", max_length=254)
#
#     image = models.ForeignKey(
#         'wagtailimages.Image',
#         null=True,
#         blank=True,
#         on_delete=models.SET_NULL,
#         related_name='+'
#     )
#
#     panels = [
#         MultiFieldPanel([
#             FieldRowPanel([
#                 FieldPanel('first_name', classname="col6"),
#                 FieldPanel('last_name', classname="col6"),
#             ])
#         ], "Name"),
#         FieldPanel('job_title'),
#         ImageChooserPanel('image')
#     ]
#
#     search_fields = [
#         index.SearchField('first_name'),
#         index.SearchField('last_name'),
#     ]
#
#     @property
#     def thumb_image(self):
#         # Returns an empty string if there is no profile pic or the rendition
#         # file can't be found.
#         try:
#             return self.image.get_rendition('fill-50x50').img_tag()
#         except:
#             return ''
#
#     def __str__(self):
#         return '{} {}'.format(self.first_name, self.last_name)
#
#     class Meta:
#         verbose_name = 'Person'
#         verbose_name_plural = 'People'
#
#
@register_snippet
class FooterText(models.Model):
    """
    This provides editable text for the site footer. Again it uses the decorator
    `register_snippet` to allow it to be accessible via the admin. It is made
    accessible on the template via a template tag defined in base/templatetags/
    navigation_tags.py
    """
    body = RichTextField()

    panels = [
        FieldPanel('body'),
    ]

    def __str__(self):
        return "Footer text"

    class Meta:
        verbose_name_plural = 'Footer Text'
