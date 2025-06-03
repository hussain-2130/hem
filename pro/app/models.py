from django.db import models
from django.contrib.auth.models import User
cchoice=[("pending","pending"),("closed","closed"),("open","open")]
class Ticket(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 title=models.CharField(max_length=200)
 description=models.TextField(max_length=200)
 created_by=models.DateTimeField(auto_now_add=True)
 status=models.CharField(choices=cchoice,default="pending",max_length=20)
class TicketHistory(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE)
 staff=models.ForeignKey(User,on_delete=models.CASCADE,related_name="staff")
 curr_status=models.CharField(choices=cchoice,default="pending",max_length=20)
 prev_status=models.CharField(choices=cchoice,default="pending",max_length=20)
 ticket=models.ForeignKey(Ticket,on_delete=models.CASCADE)

