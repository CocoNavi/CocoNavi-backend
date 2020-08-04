from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from users import models as user_models
from django.http import HttpResponse, JsonResponse
import json


@method_decorator(csrf_exempt)
def google_login(request):
    if request.method == "POST":
        # print(request.body)
        params_json = request.body.decode(
            "utf8"
        )  # 닉네임의 경우 한글로 된 경우가 많아서 이게 헥사 ? 값으로 들어오는데 이걸 다시 utf-8로 디코딩 해줌
        data_json = json.loads(params_json)  # 파라미터를 디코딩한 후 json 형태로 변환
        # print(data_json)
        username = data_json["username"]
        nickname = data_json["nickname"]
        uid = data_json["uid"]
        login_method = data_json["login_method"]
        try:
            # uid를 pk로 잡았기 때문에 이를 이용해 현재 데이터베이스에 request로 받은 uid에 해당하는 유저가 있는지 확인 !! -> 없으면 exception이 발생해서 exception부분으로 이동한다.
            user = user_models.User.objects.get(uid=uid)
            response = {
                "result": "Already Exists"
            }  # post요청이기 때문에 따로 response가 중요하지 않아 아무값이나 response해줌
            return JsonResponse(response, status=201)
        except user_models.User.DoesNotExist:  # 요청받은 uid에 해당하는 유저가 없는 상태이기 때문에 데이터베이스에 입력받은 값을 가지고 유저를 생성
            print("here!!")
            user = user_models.User.objects.create(
                username=username,
                uid=uid,
                login_method=login_method,
                nickname=nickname,
            )
            user.set_unusable_password()  # 패스워드는 중요하지않아서 아무값이나 넣어줌(자동생성)
            user.save()
            response = {"result": "Create User"}
            return JsonResponse(response, status=201)
