from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(verbose_name='message')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
