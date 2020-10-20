from django.core.mail import EmailMessage

def sendotp(otp, email):
	msg = '''Hi there!
Thanks for creating your account with us,

Your account verification OTP is '''+otp+'''

Thanks!'''
	sub = 'Account Verification OTP'
	email = EmailMessage(sub, msg, to=[email]).send()

def sendconfirmation(email):
	msg = '''Hi there!
We have received your query! We will contact you soon.

Thanks!'''
	sub = 'Account Confirmation - Details Received'
	email = EmailMessage(sub, msg, to=[email]).send()

def sendpassword(email,password):
	msg = '''Hi there!
Your account is approved by Admin, Below is your account Password.

'''+password+'''

Thanks!'''
	sub = 'Account Approved - Account Password'
	email = EmailMessage(sub, msg, to=[email]).send()