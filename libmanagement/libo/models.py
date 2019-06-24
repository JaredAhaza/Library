from django.db import models

# Create your models here.
class Book(models.Model):
    """
    An Book class - to describe book in the system.
    """
    title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200)
    publisher = models.ForeignKey('Publisher')
    author = models.ForeignKey('Author')
    lend_period = models.ForeignKey('LendPeriods')
    page_amount = models.IntegerField()
    lend_by = models.ForeignKey('UserProfile', null=True, blank=True)
    lend_date = models.DateField(null=True, blank=True)
	purchase_date =models.DateField('Purchase date')





class LendPeriods(models.Model):
    """
    Users can borrow books from library for different
    time period. This class defines frequently-used
    lending periods.
    """
    name = models.CharField(max_length=30)
    days_amount = models.IntegerField()



class Publisher(models.Model):
    """
    Class defines book's publisher
    """
    name = models.CharField(max_length=30)




class Author(models.Model):
    """
    Class defines book's author
    """
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    date_of_birth = models.DateField()




class review(models.Model):
    """
    Class descirbes a review of the book
    saved by specific user
    """
    user = models.ForeignKey(User, blank=False, null=False)
    book = models.ForeignKey(Book, blank=False, null=False)
    review = models.CharField(max_length=600, null=False, blank=False)
    pub_date = models.DateTimeField('date published')





class UserProfile(models.Model):
    """
    Class provides more information according the system's users
    """
    user = models.OneToOneField(User)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    website = models.CharField(max_length=50, null=True, blank=True)
    fb_name = models.CharField(max_length=60, null=True, blank=True)
    friends = models.ManyToManyField('self', symmetrical=True)
    join_date = models.DateField()