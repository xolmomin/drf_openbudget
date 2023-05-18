from ckeditor.fields import RichTextField
from django.db.models import Model, CharField, DateTimeField, IntegerField, ImageField


class New(Model):
    title = CharField(max_length=255)
    image = ImageField(upload_to='images/new/')
    view_count = IntegerField(default=0)
    description = RichTextField(blank=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
