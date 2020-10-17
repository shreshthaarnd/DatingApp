from django.core.mail import EmailMessage

def sendotp(otp, email):
	msg = '''Hi there!
Thanks for creating your account with us,

Your account verification OTP is '''+otp+'''

Thanks!'''
	sub = 'Account Verification OTP'
	email = EmailMessage(sub, msg, to=[email]).send()