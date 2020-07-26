from django.contrib import admin
from .models import *
admin.site.site_header = "JANAMAT"


class UserProfileAdmin(admin.ModelAdmin):
    list_display= ('user', 'profile_image', 'phone', 'dob', 'usr_type',)
admin.site.register(UserProfile, UserProfileAdmin)

class ChellengeAdmin(admin.ModelAdmin):
    list_display= ('chellengeName', 'chellengeDesc', 'created_on')
admin.site.register(Chellenge, ChellengeAdmin)

class TopicListAdmin(admin.ModelAdmin):
    list_display= ('Chellenge', 'Topic', 'TopicDesc', 'voteCount', 'created_on')
admin.site.register(TopicList, TopicListAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display= ('user_id', 'chellenge_id', 'date_comment', 'message', 'updated_by')
admin.site.register(Comment, CommentAdmin)


class VoteAdmin(admin.ModelAdmin):
    list_display= ('Chellenge', 'Topic', 'User', 'is_votted')
admin.site.register(Vote, VoteAdmin)


class TimelineAdmin(admin.ModelAdmin):
    list_display= ('user', 'date_time', 'news_header', 'news', )
admin.site.register(Timeline, TimelineAdmin)
