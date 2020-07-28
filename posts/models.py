from django.db import models
from core import models as core_models

class Photo(core_models.TimeStampedModel):
    """Photo Model Definition"""
    file = models.ImageField(upload_to="posts_photos")
    post = models.ForeignKey("posts.Post", on_delete=models.CASCADE, related_name="post_photos")

    def __str__(self):
        return f"{self.post}'s Photo"

class Post(core_models.TimeStampedModel):
    """Custom Post Model"""
    #제목, 내용, 고or강, 종류, 지역을 가지고. 글의 주인과 해당하는 게시판에 대한 foreignkey를 가진다.
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    host = models.ForeignKey("users.User",
                             on_delete=models.CASCADE,
                             related_name="posts")
    board = models.ForeignKey("boards.Board",
                              on_delete=models.CASCADE,
                              related_name="posts")
    PET_CAT = "고양이"
    PET_DOG = "강아지"
    PET_CHOICE = ((PET_CAT, "고양이"), (PET_DOG, "강아지"))
    pet_kind = models.CharField(choices=PET_CHOICE,
                                    max_length=15,
                                    default=PET_DOG, null=True, blank=True)
    pet_age = models.IntegerField(blank=True, null=True)
    #종, 지역
    DOG_KINDS = (("말티즈", "말티즈"),("푸들", "푸들"), ("포메라니안", "포메라니안"), ("시츄", "시츄"), ("비숑", "비숑"), 
    ("요크셔테리어", "여크셔테리어"), ("치와와", "치와와"), ("스피츠", "스피츠"), ("믹스견", "믹스견"), ("닥스훈트", "닥스훈트"),
    ("진도견", "진도견"), ("웰시코기", "웰시코기"), ("시바견", "시바견"))
    dog_kind = models.CharField(choices=DOG_KINDS, max_length=15, null=True, blank=True)
    
    CAT_KINDS = (("스코티쉬폴드", "스코티쉬폴드"), ("러시안블루", "러시안블루"), ("먼치킨", "먼치킨"), ("페르시안", "페르시안"), ("샴", "샴"), 
    ("뱅갈", "뱅갈"), ("브리티쉬숏헤어", "브리티쉬숏헤어"), ("터키쉬앙고라", "터키쉬앙고라"), ("아비시니안", "아비시니안"), ("믹스", "믹스"))
    cat_kind = models.CharField(choices=CAT_KINDS, max_length=15, null=True, blank=True)
    
    DISTRICT_KOREA = (("서울특별시", "서울특별시"), ("부산광역시", "부산광역시"), ("인천광역시", "인천광역시"), ("대구광역시", "대구광역시"), ("광주광역시", "광주광역시"), ("대전광역시", "대전광역시"), ("울산광역시", "울산광역시"), ("세종특별자치시", "세종특별자치시"), ("경기도", "경기도"), ("강원도", "강원도"), ("충청북도", "충청북도"), ("충청남도", "충청남도"), ("경상북도", "경상북도"), ("경상남도", "경상남도"), ("전라북도", "전라북도"), ("전라남도", "전라남도"), ("제주특별자치도", "제주특별자치도"))
    district_korea = models.CharField(choices=DISTRICT_KOREA, max_length=15)
    def __str__(self):
        return f"title:{self.title}"

    def count_likes(self):
        return self.likes.count()

    count_likes.short_description = "Likes"

    def count_comments(self):
        return self.comments.count()

    count_comments.short_description = "Comments"

    def serializeCustom(self):
        data = {
            "pk": self.pk,
            "title": self.title,
            "text": self.text,
            "host": self.host.pk,
            "host_name": self.host.nickname,
            "board": self.board.pk,
            "likes_number": self.count_likes(),
            "created":str(self.created),
            "updated":str(self.updated),
            "comments_number": self.count_comments(),
        }
        return data
