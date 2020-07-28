from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from users import models as user_models
from django.http import HttpResponse, JsonResponse
import json


@method_decorator(csrf_exempt)
def google_login(request):
    if request.method == "POST":
        params_json = request.body.decode("utf8")
        data_json = json.loads(params_json)
        print(data_json)
        username = data_json["username"]
        nickname = data_json["nickname"]
        uid = data_json["uid"]
        login_method = data_json["login_method"]
        try:
            user = user_models.User.objects.get(uid=uid)
            response = {"result": "Already Exists"}
            return JsonResponse(response, status=201)
        except user_models.User.DoesNotExist:
            user = user_models.User.objects.create(
                username=username,
                uid=uid,
                login_method=login_method,
                nickname=nickname,
            )
            user.set_unusable_password()
            user.save()
            response = {"result": "Create User"}
            return JsonResponse(response, status=201)
