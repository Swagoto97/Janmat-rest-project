from django.db import models
from django.contrib.auth.models import User
from datetime import *


USER_TYPE = (
    (1, "Admin"),
    (2, "User")
)


class UserProfile(models.Model):
    # This line binds this extended profile with user
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    profile_image = models.ImageField(
        upload_to="janamat/ProfileImage", blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateTimeField(auto_now=True)
    usr_type = models.IntegerField(choices=USER_TYPE, default=2)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = "UserProfile"


class Chellenge(models.Model):
    chellengeName = models.CharField(max_length=50, blank=False, null=False)
    chellengeDesc = models.TextField(max_length=1000, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True )
    # created_on = models.DateTimeField(default=datetime.today)
    # topiclist = models.ForeignKey(TopicList, on_delete=models.CASCADE)

    def __str__(self):
        return self.chellengeName  # You will get the list with the Challenge name

    class Meta:
        db_table = "Chellenge"


class TopicList(models.Model):
    # one too many or many to one relaton
    Chellenge = models.ForeignKey(Chellenge, on_delete=models.CASCADE)
    Topic = models.CharField(max_length=50, blank=False, null=False)
    TopicDesc = models.TextField(max_length=1000, blank=True, null=True)
    voteCount = models.IntegerField(default=0, null=False, blank=True)
    created_on = models.DateTimeField(auto_now=True )

    def __str__(self):
        return str(self.Topic)+' :  '+self.TopicDesc

    class Meta:
        db_table = "TopicList"


class Comment(models.Model):
    # id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="Comment_updated_by", null=True)

    chellenge_id = models.ForeignKey(Chellenge, on_delete=models.CASCADE)
    # This one works exact time of current location
    date_comment = models.DateTimeField(default=datetime.today)
    message = models.TextField('Message Field')

    def __str__(self):
        return str(self.user_id) + '    :   ' + str(self.chellenge_id) + '    :   ' + self.message

    class Meta:
        db_table = "Comment"


class Vote(models.Model):
    # id
    Chellenge = models.ForeignKey(Chellenge, on_delete=models.CASCADE)
    Topic = models.ForeignKey(TopicList, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    is_votted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.User) + '    :   ' + str(self.Chellenge) + '    :   ' + str(self.Topic)
        # return str(self.is_votted)

    class Meta:
        db_table = "Vote"
        unique_together = ('Chellenge', 'User',)
        # verbose_name


class testMOdel(models.Model):
    # id
    message = models.TextField('Message Field')

    def __str__(self):
        return self.message

    class Meta:
        db_table = "Test_MOdel"


class Timeline(models.Model):
    #id
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now=True )  #This one works exact time of current 
    news_header = models.CharField(max_length=500)
    news = models.TextField('Message Field')
    def __str__(self):
        return str(self.user_id)
    class Meta:
        db_table="Timeline"





from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)