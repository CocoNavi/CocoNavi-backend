from django.db import models
from core import models as core_models

class Photo(core_models.TimeStampedModel):
    file = models.ImageField(upload_to="pets_photos")
    pet = models.ForeignKey('pets.Pet', related_name='photos', on_delete=models.CASCADE)

class Pet(core_models.TimeStampedModel):
    owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=10, unique=True)
    PET_CAT = "고양이"
    PET_DOG = "강아지"
    PET_CHOICE = ((PET_CAT, "고양이"), (PET_DOG, "강아지"))
    pet_kinds = models.CharField(choices=PET_CHOICE,
                                    max_length=15,
                                    default=PET_DOG, null=True, blank=True)
    birthday = models.CharField(max_length=10)
    GENDER_MALE = "MALE"
    GENDER_FEMALE = "FEMALE"
    GENDER_CHOICE = ((GENDER_MALE, "MALE"), (GENDER_FEMALE, "FEMALE"))
    DOG_KINDS = (("말티즈", "말티즈"),("푸들", "푸들"), ("포메라니안", "포메라니안"), ("시츄", "시츄"), ("비숑", "비숑"), 
    ("요크셔테리어", "여크셔테리어"), ("치와와", "치와와"), ("스피츠", "스피츠"), ("믹스견", "믹스견"), ("닥스훈트", "닥스훈트"),
    ("진도견", "진도견"), ("웰시코기", "웰시코기"), ("시바견", "시바견"))
    dog_kind = models.CharField(choices=DOG_KINDS, max_length=15, null=True, blank=True)
    
    CAT_KINDS = (("스코티쉬폴드", "스코티쉬폴드"), ("러시안블루", "러시안블루"), ("먼치킨", "먼치킨"), ("페르시안", "페르시안"), ("샴", "샴"), 
    ("뱅갈", "뱅갈"), ("브리티쉬숏헤어", "브리티쉬숏헤어"), ("터키쉬앙고라", "터키쉬앙고라"), ("아비시니안", "아비시니안"), ("믹스", "믹스"))
    cat_kind = models.CharField(choices=CAT_KINDS, max_length=15, null=True, blank=True)
    gender = models.CharField(choices=GENDER_CHOICE, max_length=15)
    profile = models.TextField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.owner.nickname}'s Pet {self.name}"