from django.db import models


class StaffModel(models.Model):
    avatar = models.ImageField(upload_to='avatar', verbose_name='avatar')
    name = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    short_description = models.TextField(verbose_name='short_description')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staffs'
