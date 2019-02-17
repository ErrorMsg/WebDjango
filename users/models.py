from django.db import models

SEX_CHOICES=(
    (1, "male"),
    (2, "female")
)

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=128, unique=True)
    pw = models.CharField(max_length=256)
    mail = models.EmailField(unique=True)
    sex = models.IntegerField(choices=SEX_CHOICES, default = 1)
    ct_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-ct_time"]
        verbose_name = "user"
        verbose_name_plural = "users"

