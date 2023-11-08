from django.db import models

class category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self) -> str:
        return str(self.name)
    

class photo(models.Model):
    category=models.ForeignKey(category, on_delete=models.SET_NULL,null=True,blank=True)
    ques_no=models.IntegerField()
    description=models.TextField(null=True,blank=True)
    ques_url=models.URLField()
    ans_url=models.URLField()
    ques_heading=models.TextField()
    ques_image=models.ImageField()
    ans_image=models.ImageField()
    ans_second_image=models.ImageField(null=True,blank=True)

    def __str__(self) -> str:
        return str(self.ques_heading)


class urlClass(models.Model):
    url_heading=models.TextField()
    url_link=models.URLField(default="https://leetcode.com/arinutkarsh55/")
    url_description=models.TextField()

    def __str(self) -> str:
        return self.url_heading
    

class snippet_class(models.Model):
    snippet_heading=models.TextField()
    snippet_text=models.TextField()

    def __str(self) -> str:
        return self.snippet_heading