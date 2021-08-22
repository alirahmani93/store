from django.db import models

from django.utils.translation import ugettext_lazy as _
from author.models import Author
from category.models import Category
from lib.models import BaseModel


class Post(BaseModel):
    DRAFT = 0
    PUBLISHED = 1
    ARCHIVED = 2

    STATUS_CHOICES = (
        (DRAFT, _('Draft')),
        (PUBLISHED, _('Published')),
        (ARCHIVED, _('Archived'))
    )
    title = models.CharField(max_length=255, verbose_name=_('title'))
    body = models.TextField(verbose_name='body', blank=True, null=True)

    author = models.ForeignKey(
        Author, related_name='posts', on_delete=models.SET_DEFAULT, default=1
    )
    attachment = models.FileField(
        verbose_name='attachment', upload_to='posts/attachments/', null=True
    )
    categories = models.ManyToManyField(Category, related_name='posts')
    status = models.PositiveSmallIntegerField(
        verbose_name="status", choices=STATUS_CHOICES, default=0
    )

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title

    def jalali_time(self, time):
        # Convert first
        return time

    def jalali_created_time(self):
        pass

    def get_absolute_url(self):
        pass
