from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from . import models as event_models
from pets import models as pet_models
from users import models as user_models


@method_decorator(csrf_exempt)
def add_events(request):  # 이벤트 추가하는 코드
    if request.method == "POST":
        params_json = request.body.decode("utf8")
        data_json = json.loads(params_json)  # 파라미터를 디코딩한 후 json 형태로 변환
        # print(data_json)
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
            pet=pet,
            title=title,
            text=text,
            year=year,
            month=month,
            date=day,
            user=owner,
        )
        response = {"result": "Create Event"}
        return JsonResponse(response, status=201)


@method_decorator(csrf_exempt)
def revise_events(request):  # 이벤트 추가하는 코드
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
        pk = data_json["pk"]
        owner = user_models.User.objects.get(uid=uid)
        pet = pet_models.Pet.objects.filter(owner=owner).get(name=pet_name)
        # 여기부터 위의 정보를 가지고 이벤트 추가하는 코드 짜기
        try:
            event = event_models.DayEvent.objects.get(pk=pk)
            event.pet = pet
            event.title = title
            event.text = text
            event.year = year
            event.month = month
            event.date = day
            event.save()
            response = {"result": "Revise Event"}
            return JsonResponse(response, status=201)
        except event_models.DayEvent.DoesNotExist:
            response = {"result": "Error"}
            return JsonResponse(response, status=201)


@method_decorator(csrf_exempt)
def get_events_date(request):  # 각 날마다 해당하는 이벤트를 가져오는 부분
    params_json = request.body.decode("utf8")
    data_json = json.loads(params_json)  # 파라미터를 디코딩한 후 json 형태로 변환
    date = data_json["date"]
    uid = data_json["uid"]
    user = user_models.User.objects.get(uid=uid)
    date_splited = date.split("-")
    year = date_splited[0]
    month = date_splited[1]
    day = date_splited[2]
    events = (
        event_models.DayEvent.objects.filter(user=user)
        .filter(year=year)
        .filter(month=month)
        .filter(date=day)
        .order_by("created")
    )
    events_serialized = []
    for event in events:
        events_serialized.append(event.serialize_custom())
    events_json = json.dumps(events_serialized)
    return HttpResponse(events_json, content_type="text/json-comment-filtered")


@method_decorator(csrf_exempt)
def get_events_month(request):  # 캘린더 표시할때 month별 이벤트를 가져오는 코드
    params_json = request.body.decode("utf8")
    data_json = json.loads(params_json)  # 파라미터를 디코딩한 후 json 형태로 변환
    year = data_json["year"]
    month = data_json["month"]
    uid = data_json["uid"]
    user = user_models.User.objects.get(uid=uid)
    events = (
        event_models.DayEvent.objects.filter(user=user)
        .filter(year=year)
        .filter(month=month)
    )
    events_serialized = []
    for event in events:
        events_serialized.append(event.serialize_custom1())
    events_json = json.dumps(events_serialized)
    return HttpResponse(events_json, content_type="text/json-comment-filtered")
