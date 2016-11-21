from django.http import HttpResponse


	
def index(request):
    #install one of those REST clients in your web-browser
	if request.method == 'GET':
		#http://hostname?arg_1=1234
		arg_1 = request.GET['arg_1'] if 'arg_1' in request.GET else None
		arg_2 = reguest.GET['arg_2'] if 'arg_2' in request.GET else None
        result = {}
        if arg_1:
            result['arg_1'] = arg_1
        if arg_2:
            result['arg_2'] = arg_2
	    return HttpRespone(json.dumps(result))
    if request.method == 'POST':
		#http://hostname?arg_1=1234
		#and request body '{'one': 1, 'two': 2}'
        #Yes, it's GET too
        arg_1 = request.GET['arg_1'] if 'arg_1' in request.GET else None        
        args = json.loads(request.body)
        result = ''
        for key, value in args.iteritems():
            result += '{}: {}\n'.format(key, value)
        return HttpResponse(json.loads({'expr': result}))
	
