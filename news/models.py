from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
from blanc_basic_assets.fields import AssetForeignKey


@python_2_unicode_compatible
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'categories'
        ordering = ('title',)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('news:post-list-category', (), {
            'slug': self.slug,
        })


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    category = models.ForeignKey(Category)
    slug = models.SlugField(max_length=100, unique_for_date='date')
    date = models.DateTimeField(default=timezone.now, db_index=True)
    date_url = models.DateField(db_index=True, editable=False)
    image = AssetForeignKey('assets.Image', null=True, blank=True)
    teaser = models.TextField(blank=True)
    content = models.TextField()
    published = models.BooleanField(default=True,
                                    db_index=True,
                                    help_text='Post will be hidden unless this option is selected')

    class Meta:
        get_latest_by = 'date'
        ordering = ('-date',)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('news:post-detail', (), {
            'year': self.date_url.year,
            'month': str(self.date_url.month).zfill(2),
            'day': str(self.date_url.day).zfill(2),
            'slug': self.slug,
        })

    def save(self, *args, **kwargs):
        self.date_url = self.date.date()
        super(Post, self).save(*args, **kwargs)

