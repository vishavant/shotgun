from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# QUIZ_QUESTION_TYPE = (
#     ('SINGLE CORRECT', 'Single Correct'),
#     ('TRUE OR FALSE', 'True or False'),
#     ('SUBJECTIVE', 'Subjective'),
#     ('MULTIPLE CORRECT', 'Multiple Correct'),
# )


# class Quiz(models.Model):
#     quiz_name = models.CharField(max_length=250)
#     quiz_image = models.ImageField(blank=True, upload_to='quiz_profile')
#     quiz_description = models.CharField(max_length=300, blank=True)
#     quiz_timer = models.TimeField(blank=True, null=True, help_text="Define time on each question")
#     no_of_participant = models.IntegerField(help_text="How Many Users can Participate in this quiz")
#     # participants = models.ManyToManyRel(User, related_name= 'participants')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.quiz_name}"
    
#     def get_questions(self):
#         return self.question_set.all()


# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
#     question = models.CharField(max_length=250)
#     desciption = models.CharField(max_length=300, blank=True)
#     question_media = models.FileField(upload_to='quiz/question_media', blank=True)
#     question_type = models.CharField(max_length=50, choices=QUIZ_QUESTION_TYPE)
#     time_limit = models.PositiveSmallIntegerField(default=60, help_text='By Default Question timer is set for 60 seconds', blank=True) # in second
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.question)

#     def get_answers(self):
#         return self.question.all()


# class SingleChoice(models.Model):
#     question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='singlechoice')
#     text = models.TextField()
#     is_correct = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Question: {self.question}, answer: {self.text} correct:{self.is_correct}"



# class MultipleChoice(models.Model):
#     question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='mulitplechoice')
#     text = models.TextField()
#     is_correct = models.BooleanField(default=False)




# class TrueFalseQuestion(models.Model):
#     question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='true_false_question')
#     is_true = models.BooleanField(default=False)



# class SubjectiveAnswer(models.Model):
#     question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='subjective_answer')
#     answer = models.TextField()



# class PollOption(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.TextField()
#     votes = models.PositiveIntegerField(default=0)






    


"""
============================================================================================================================
"""
class QuizLevel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"




class Quiz(models.Model):
    level = models.ForeignKey(QuizLevel, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    quiz_thumbnail = models.ImageField(blank=True, null=True, upload_to='quiz_thumbnail')
    required_score_to_pass = models.IntegerField(help_text="Required Score to Pass the Exam")
    no_of_participants = models.IntegerField(blank=True, null=True)
    no_of_questions = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"
    

    def get_questions(self):
        return self.question_set.all()



class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    question_media = models.FileField(upload_to='quiz/question_media', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
    
    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"question: {self.question.text} answer: {self.text} correct: {self.correct}"
    



class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)