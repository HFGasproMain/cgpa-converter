from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	user_level = (
		('Masters', 'Masters'),
		('BSc', 'BSc')
	)
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
	course_of_study = models.CharField(max_length=60, null=True, default='Computer Science')
	academic_scale = models.CharField(max_length=10)
	num_courses = models.PositiveIntegerField()
	photo = models.ImageField(upload_to='users', default='default.jpeg', blank=True)
	country = models.CharField(max_length=60, default='Nigeria')
	level = models.CharField(max_length=30, choices=user_level)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.username