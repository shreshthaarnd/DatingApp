def checksession(request):
	try:
		uid = request.session['user_id']
		return True
	except:
		return False