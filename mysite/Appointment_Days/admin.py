#import webapp2 
from django.contrib import admin
#import django.template.loader as dj
from .models import Appointment

admin.site.register(Appointment)

'''class MainAdminSite(AdminSite):
	site_header='Crystal administration'
	#def get(self):

admin_site=MainAdminSite(name='apt_list')
admin_site.register(Appointment)'''



'''class AppointmentHandler(webapp2.RequestHandler):
	#def get(self):

	def post(self):
		user_value = self.request.get('user_type')
		template_val = 'templates/' + user_value + '.html'
		if user_value == 'AppointmentDays':
			url_value = 'Appointment_Days'
		else:
			pass
		template = dj.get_template(template_val)
		self.response.write(template.render({'user_value': user_value}))
		self.redirect(url_value)


app = webapp2.WSGIApplication([
	('/', MainAdminSite),
	('Appointment_Days', AppointmentHandler),
	], debug=True)'''
# Register your models here.
