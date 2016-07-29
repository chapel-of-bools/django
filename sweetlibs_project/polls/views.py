from django.http import HttpResponse

def index(request, num="1"):
     return render(request, 'polls/post_list.html', {})

# def index (request):
#     if first % 3 == 0:
#         word += 'Fizz'
#     if first % 5 == 0:
#         word += 'Buzz'
#     return HttpResponse()
#
#     if first < last:
#         index(first + 1, last)
#
# index(0, 100)
