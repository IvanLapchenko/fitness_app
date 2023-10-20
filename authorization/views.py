from django.http import JsonResponse
from .forms import SignUpForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return JsonResponse({'message': 'User created successfully', 'user_id': user.id}, status=201)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'errors': errors}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=405)
