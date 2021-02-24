from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Society
from django.contrib.auth.models import Group

from django.conf import settings
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

def society_registration(sender,instance,created,**kwargs):
	if created:
		group = Group.objects.get(name = 'Society')
		instance.groups.add(group)

		#user.groups.add(group)

		Society.objects.create(
					society=instance,
					name=instance.username,
					#email=instance.email,
				)
		print('Society created')

post_save.connect(society_registration,sender=User)









def create_auth_token(sender, instance=None, created=False, **kwargs):

	for user in User.objects.all():
		Token.objects.get_or_create(user=user)
post_save.connect(create_auth_token,sender=settings.AUTH_USER_MODEL)