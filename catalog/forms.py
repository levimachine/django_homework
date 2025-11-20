from catalog.models import BlogPost, Product, Version
from django import forms


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BlogPostForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'is_published')


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'price_per_piece',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        if cleaned_data.lower() in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                                    'полиция', 'радар']:
            raise forms.ValidationError('Невозможно создать продукт с таким именем!')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        is_actual = cleaned_data.get('is_actual')
        versions = Version.objects.filter(product=product, is_actual='actual')

        if len(versions) > 0 and is_actual == 'actual':
            raise forms.ValidationError('Может быть только одна активная версия!')
        return cleaned_data

    def clean_number(self):
        cleaned_data = self.cleaned_data.get('number')
        product = self.cleaned_data.get('product')
        version_list = Version.objects.all()
        for version in version_list:
            if version.product.name == product.name and version.number == cleaned_data:
                raise forms.ValidationError(f'Версия номер {cleaned_data} уже есть у продукта {product.name}!')
        return cleaned_data
