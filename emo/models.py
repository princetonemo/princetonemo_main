from django.db import models

class Department(models.Model):
	name = models.CharField(max_length=60, blank=True)
	abbr = models.CharField(max_length=3)
	num_students = models.IntegerField(default=0)

	angry_avg = models.FloatField(default=0., blank=True)
	sad_avg = models.FloatField(default=0., blank=True)
	neutral_avg = models.FloatField(default=0., blank=True)
	surprise_avg = models.FloatField(default=0., blank=True)
	fear_avg = models.FloatField(default=0., blank=True)
	happy_avg = models.FloatField(default=0., blank=True)

	def __unicode__(self):
		return self.abbr

class UserProfile(models.Model):
	num_scanned = models.IntegerField(default=0)

	angry_new = models.FloatField(default=0.)
	sad_new = models.FloatField(default=0.)
	neutral_new = models.FloatField(default=0.)
	surprise_new = models.FloatField(default=0.)
	fear_new = models.FloatField(default=0.)
	happy_new = models.FloatField(default=0.)

	angry_avg = models.FloatField(default=0., blank=True)
	sad_avg = models.FloatField(default=0., blank=True)
	neutral_avg = models.FloatField(default=0., blank=True)
	surprise_avg = models.FloatField(default=0., blank=True)
	fear_avg = models.FloatField(default=0., blank=True)
	happy_avg = models.FloatField(default=0., blank=True)

	department = models.ForeignKey(Department) # user is the many, department is the one
	def __unicode__(self):
		return self.id