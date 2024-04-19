from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date

# Create your models here.
class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_purchase = models.DateField(auto_now_add=False)
    how_many_days = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.first_name + ' ' + self.user.last_name
    
    def checkDate(self):
        today = date.today()
        
        #days without weekends
        def date_by_adding_business_days(from_date, add_days):
            business_days_to_add = add_days
            current_date = from_date
            while business_days_to_add > 0:
                current_date += timedelta(days=1)
                weekday = current_date.weekday()
                if weekday >= 5: # sunday = 6
                    continue
                business_days_to_add -= 1
            return current_date
        
        if date_by_adding_business_days(self.date_of_purchase, self.how_many_days) < today:
            Client.objects.get(pk=self.pk).delete()
            print('deleted')