from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from users import models as user_models
from django.http import HttpResponse, JsonResponse
from . import models as pet_models
import json


@method_decorator(csrf_exempt)
def get_pets(request):
    if request.method == "POST":
        params_json = request.body.decode("utf8")
        data_json = json.loads(params_json)  # 파라미터를 디코딩한 후 json 형태로 변환
        # print(data_json)
        uid = data_json["uid"]
        try:
            # uid를 pk로 잡았기 때문에 이를 이용해 현재 데이터베이스에 request로 받은 uid에 해당하는 유저가 있는지 확인 !! -> 없으면 exception이 발생해서 exception부분으로 이동한다.
            user = user_models.User.objects.get(uid=uid)
            pets = pet_models.Pet.objects.filter(owner=user).order_by("-created")
            pet_serialized = []
            if len(pets) == 0:
                return
            print("pet : ", pet_serialized)
            for pet in pets:
                pet_serialized.append(pet.serialize_custom())
            pets_json = json.dumps(pet_serialized)
            return HttpResponse(pets_json, content_type="text/json-comment-filtered")
        except user_models.User.DoesNotExist:
            response = {"result": "Error user does not Exists!!"}
            return JsonResponse(response, status=201)


@method_decorator(csrf_exempt)
def add_pets(request):
    if request.method == "POST":
        params_json = request.body.decode("utf8")
        data_json = json.loads(params_json)  # 파라미터를 디코딩한 후 json 형태로 변환
        uid = data_json["uid"]
        try:
            user = user_models.User.objects.get(uid=uid)
            name = data_json["name"]
            kind = data_json["kind"]
            profile = data_json["profile"]
            gender = data_json["gender"]
            avatar = data_json["avatar"]
            birthday = data_json["birthday"]
            species = data_json["species"]
            is_visible = data_json["is_visible"]
            print(gender)
            if kind == "강아지":
                if avatar == "":
                    pet = pet_models.Pet.objects.create(
                        owner=user,
                        name=name,
                        pet_kinds=kind,
                        birthday=birthday,
                        dog_kind=species,
                        gender=gender,
                        profile=profile,
                        is_visible=is_visible,
                    )
                else:
                    pet = pet_models.Pet.objects.create(
                        owner=user,
                        name=name,
                        pet_kinds=kind,
                        birthday=birthday,
                        dog_kind=species,
                        gender=gender,
                        profile=profile,
                        is_visible=is_visible,
                        avatar=avatar,
                    )
            elif kind == "고양이":
                if avatar == "":
                    pet = pet_models.Pet.objects.create(
                        owner=user,
                        name=name,
                        pet_kinds=kind,
                        birthday=birthday,
                        cat_kind=species,
                        gender=gender,
                        profile=profile,
                        is_visible=is_visible,
                    )
                else:
                    pet = pet_models.Pet.objects.create(
                        owner=user,
                        name=name,
                        pet_kinds=kind,
                        birthday=birthday,
                        cat_kind=species,
                        gender=gender,
                        profile=profile,
                        is_visible=is_visible,
                        avatar=avatar,
                    )
            else:
                response = {"result": "Error pet kind does not Exists!!"}
                return JsonResponse(response, status=201)
            response = {"result": "create success"}
            return JsonResponse(response, status=201)
        except user_models.User.DoesNotExist:
            response = {"result": "Error user does not Exists!!"}
            return JsonResponse(response, status=201)
