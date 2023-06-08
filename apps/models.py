from ckeditor.fields import RichTextField
from django.contrib.auth.models import Permission
from django.db.models import (CASCADE, CharField, DateTimeField, FileField,
                              ForeignKey, ImageField, IntegerField, Model,
                              OneToOneField, BooleanField)
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from parler.models import TranslatableModel


class UseFulInfo(Model):
    title = CharField(max_length=255)
    image = ImageField(upload_to='images/usefullinfo/')
    number_download = IntegerField(default=0)
    file = FileField(upload_to='images/usefullinfo/')


class New(Model):
    title = CharField(max_length=255)
    # image = ImageField(upload_to='images/new/')
    view_count = IntegerField(default=0)
    is_premium = BooleanField(default=False)
    description = RichTextField(blank=True)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (("view_is_premium", "Can view premium new"),)
        ordering = ('-created_at',)


class Region(Model):
    name = CharField(max_length=255)


class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('apps.Region', CASCADE, 'districts')


class ResponsiblePerson(Model):
    full_name = CharField(max_length=255)
    phone = CharField(max_length=500)
    district = OneToOneField('apps.District', CASCADE)


class Category(MPTTModel):
    name = CharField(max_length=200, null=True, blank=True)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    @property
    def product_count(self):
        return self.product_set.count()

    def __str__(self):
        return self.name


class Product(Model):
    price = IntegerField(default=0)
    name = CharField(max_length=200, null=True, blank=True)
    category = ForeignKey('apps.Category', CASCADE)
    owner = ForeignKey('auth.User', CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        # indexes = [
        #     HashIndex(fields=["last_name", "first_name"]),
        #     BTreeIndex(fields=["first_name"], name="first_name_idx"),
        # ]
        #
        # constraints = [
        #     CheckConstraint(
        #         check=Q(end_date__gt=F('start_date')),
        #         name='check_start_date',
        #     )
        # ]

    def __str__(self):
        return self.name


class TestProduct(Model):
    product_id = IntegerField(auto_created=True, primary_key=True)
    name = CharField(max_length=255)


# Product.objects.filter(id=2).update(quantity=F('quantity') + 5)
#
# product = Product.objects.get(id=2)
# product.quantity += 5
# product.product_id = None
# product.save()

class ProductImage(Model):
    image = ImageField(upload_to='product/images')
    product = ForeignKey('apps.Product', CASCADE)
