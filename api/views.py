from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Hello, Git World!"})
def test_function(request):
    pass
def another_test_function(request):
    pass
def final_test_function(request):
    pass