from django.db import models

class User(models.Model):


    user_id = models.IntegerField(primary_key=True,help_text="id of post")
    user_name = models.CharField(max_length=30)
    user_displayname = models.CharField(max_length=30)
    user_email = models.EmailField(unique=True, null=False)
    user_password = models.CharField(max_length=100,null=False)
    user_bio = models.TextField(max_length=400)
    def __str__(self):
        return f"username{self.user_name}displayname {self.user_displayname} email{self.user_email} password{self.user_password} bio{self.user_bio}"