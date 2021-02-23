from typing import List

from django.db import models
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS_VALUES: List = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES: List = sorted([(item[1][0], item[0]) for item in LEXERS_VALUES])
STYLE_CHOICES: List = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    title: models.CharField = models.CharField(
        max_length=100,
        blank=True,
        default=''
    )
    code: models.TextField = models.TextField()
    linenos: models.BooleanField = models.BooleanField(default=False)
    language: models.CharField = models.CharField(
        choices=LANGUAGE_CHOICES,
        default='python',
        max_length=100
    )
    style: models.CharField = models.CharField(
        choices=STYLE_CHOICES,
        default='friendly',
        max_length=100
    )
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()

    class Meta:
        ordering = [
            'created'
        ]

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)
