from django.db import models


class Newspaper(models.Model):
    title = models.CharField('Title', max_length=100)
    text = models.TextField('Content')
    author = models.CharField('Author Name', max_length=100)
    date = models.DateField('Publ. date')
    img = models.FileField('Pics', upload_to='files/', null=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__(self):
        return f'{self.title}, {self.author}'
