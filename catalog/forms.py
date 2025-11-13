from catalog.models import BlogPost, Product, Version
from django import forms


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'content', 'is_published')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'price_per_piece',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        if cleaned_data.lower() in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                                    'полиция', 'радар']:
            raise forms.ValidationError('Невозможно создать продукт с таким именем!')
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_number(self):
        cleaned_data = self.cleaned_data.get('number')
        product = self.cleaned_data.get('product')
        version_list = Version.objects.all()
        for version in version_list:
            if version.product.name == product.name and version.number == cleaned_data:
                raise forms.ValidationError(f'Версия номер {cleaned_data} уже есть у продукта {product.name}!')
        return cleaned_data
