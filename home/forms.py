from django import forms
from django.forms import ModelForm
import home.models as models   


#blog
class ArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = '__all__'

class ArticleCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Article_Category
        fields = '__all__'

#case studies
class CaseStudyForm(forms.ModelForm):
    class Meta:
        model = models.CaseStudy
        fields = '__all__'