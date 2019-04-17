from django.db import models
from django.forms import ModelForm

class Member(models.Model):
    name = models.CharField(max_length=22)
    first_name = models.CharField(max_length=22)
    member_id = models.IntegerField()

class Sport(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=22)
    member_nb = models.IntegerField(default=0)

class Activities(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    sport_nb = models.IntegerField(default=0)

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ["name", "first_name", "member_id"]

class SportForm(ModelForm):
    class Meta:
        model = Sport
        fields = ["member", "name", "member_nb"]

class ActivitiesForm(ModelForm):
    class Meta:
        model = Activities
        fields = ["sport", "sport_nb"]
