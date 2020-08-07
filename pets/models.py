from django.db import models
from core import models as core_models


class Photo(core_models.TimeStampedModel):
    # 펫에 해당하는 사진으로 사진파일을 가지고, target이 되는 펫의 foreignkey를 가진다.
    file = models.ImageField(upload_to="pets_photos")
    pet = models.ForeignKey("pets.Pet", related_name="photos", on_delete=models.CASCADE)


class Pet(core_models.TimeStampedModel):
    # 이름, 고 or 강, 생일, 성별, 종류, 소개, 공개여부를 필드로 가지고, 주인을 가지기 위해 user를 가리키는 foreign key를 하나 가진다.
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=10, unique=True)
    pet_avatar = models.ImageField(upload_to="pet_avatars", null=True, blank=True)
    PET_CAT = "고양이"
    PET_DOG = "강아지"
    PET_CHOICE = ((PET_CAT, "고양이"), (PET_DOG, "강아지"))
    pet_kinds = models.CharField(
        choices=PET_CHOICE, max_length=15, default=PET_DOG, null=True, blank=True
    )
    birthday = models.CharField(null=True, blank=True, max_length=10)
    GENDER_MALE = "MALE"
    GENDER_FEMALE = "FEMALE"
    GENDER_CHOICE = ((GENDER_MALE, "MALE"), (GENDER_FEMALE, "FEMALE"))
    DOG_KINDS = (
        ("말티즈", "말티즈"),
        ("푸들", "푸들"),
        ("포메라니안", "포메라니안"),
        ("시츄", "시츄"),
        ("비숑", "비숑"),
        ("요크셔테리어", "여크셔테리어"),
        ("치와와", "치와와"),
        ("스피츠", "스피츠"),
        ("믹스견", "믹스견"),
        ("닥스훈트", "닥스훈트"),
        ("진도견", "진도견"),
        ("웰시코기", "웰시코기"),
        ("시바견", "시바견"),
    )
    dog_kind = models.CharField(choices=DOG_KINDS, max_length=15, null=True, blank=True)

    CAT_KINDS = (
        ("코숏", "코숏"),
        ("스코티쉬폴드", "스코티쉬폴드"),
        ("러시안블루", "러시안블루"),
        ("아메숏", "아메숏"),
        ("먼치킨", "먼치킨"),
        ("페르시안", "페르시안"),
        ("샴", "샴"),
        ("뱅갈", "뱅갈"),
        ("브리티쉬숏헤어", "브리티쉬숏헤어"),
        ("터키쉬앙고라", "터키쉬앙고라"),
        ("아비시니안", "아비시니안"),
        ("믹스", "믹스"),
    )
    cat_kind = models.CharField(choices=CAT_KINDS, max_length=15, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=15)
    profile = models.TextField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.owner.nickname}'s Pet {self.name}"

    def serialize_custom(self):
        data = {
            "name": self.name,
            "pet_avatar": str(self.pet_avatar),
            "pet_kinds": self.pet_kinds,
            "birthday": self.birthday,
            "dog_kind": self.dog_kind,
            "cat_kind": self.cat_kind,
            "gender": self.gender,
            "profile": self.profile,
            "is_visible": self.is_visible,
        }
        return data
