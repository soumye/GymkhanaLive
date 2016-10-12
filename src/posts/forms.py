from django import forms

from pagedown.widgets import PagedownWidget
from django.utils import timezone
from .models import Post


# tag_choices = ('SNT Council', 'Games and Sports', 'Cultural')
tag_choices = (
    ('SNT Council', 'SNT Council'),
    ('Games and Sports', 'Games and Sports'),
    ('Cultural Council', 'Cultural Council'),
    ('FMC', 'FMC'),
    ('Vox Populi', 'Vox Populi'),
    ('Senate', 'Senate')
)

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    intro = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget(),initial=timezone.now())
    tags = forms.ChoiceField(
        required=True,
        # widget=forms.RadioSelect,
        choices=tag_choices,)
    class Meta:
        model = Post
        fields = [
            "title",
            "intro",
            "content",
            "image",
            "draft",
            "publish",
            "tags",
        ]

    def content(self):
        content = self.cleaned_data.get('content')
        return content