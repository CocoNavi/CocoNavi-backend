from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from . import models as event_models
from pets import models as pet_models
from users import models as user_models


@method_decorator(csrf_exempt)
def add_events(request):
    if request.method == "POST":
        params_json = request.body.decode("utf8")
        data_json = json.loads(params_json)  # 파라미터를 디코딩한 후 json 형태로 변환
        print(data_json)
        title = data_json["title"]
        date = data_json["date"]
        date_splited = date.split("-")
        uid = data_json["uid"]
        pet_name = data_json["pet_name"]
        text = data_json["text"]
        year = date_splited[0]
        month = date_splited[1]
        day = date_splited[2]
        owner = user_models.User.objects.get(uid=uid)
        pet = pet_models.Pet.objects.filter(owner=owner).get(name=pet_name)
        # 여기부터 위의 정보를 가지고 이벤트 추가하는 코드 짜기
        event = event_models.DayEvent.objects.create(
            pet=pet, title=title, text=text, year=year, month=month, date=day,
        )
