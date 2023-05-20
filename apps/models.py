from ckeditor.fields import RichTextField
from django.db.models import Model, CharField, DateTimeField, IntegerField, ImageField, FileField, ForeignKey, CASCADE


class UseFulInfo(Model):
    title = CharField(max_length=255)
    image = ImageField(upload_to='images/usefullinfo/')
    number_download = IntegerField(default=0)
    file = FileField(upload_to='images/usefullinfo/')


class New(Model):
    title = CharField(max_length=255)
    image = ImageField(upload_to='images/new/')
    view_count = IntegerField(default=0)
    description = RichTextField(blank=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)


class Region(Model):
    name = CharField(max_length=255)


class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('apps.Region', CASCADE)


class ResponsiblePerson(Model):
    full_name = CharField(max_length=255)
    phone = CharField(max_length=500)
    district = ForeignKey('apps.District', CASCADE)



'''

[
    {
        "name": "Toshkent",
        "districts":[
            {
                "district": "Yunusobod tumani",
                "full_name": "Бакиров Тимур Жолдасбаевич",
                "phone": "612227089"
            }
        ]
    }
]





'''
