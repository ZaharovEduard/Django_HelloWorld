from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Hello, world!</h1>")
	
def index_0(request):
	response = HttpResponse()
	response.write("<h1>Wellcome</h1>")
	response.write("This is the polls app")
	return response
