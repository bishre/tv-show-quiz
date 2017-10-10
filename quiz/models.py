from django.db import models


# Create your models here.

class Quiz(models.Model):
    quiz_number = models.PositiveIntegerField(blank=True)
    name = models.CharField(blank=True, max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField(blank=True)
    answer1 = models.CharField(blank=True, max_length=100)
    answer2 = models.CharField(blank=True, max_length=100)
    answer3 = models.CharField(blank=True, max_length=100)
    correct = models.PositiveIntegerField(blank=True)
    quiz = models.ForeignKey(Quiz, blank=True, related_name="questions")

    def __str__(self):
        return self.quiz.name + self.question


class club(models.Model):
    rank_team = models.CharField(max_length=100, blank=True)
    team_name = models.CharField(max_length=100, blank=True)
    game_played = models.CharField(max_length=100, blank=True)
    won_game = models.CharField(max_length=100, blank=True)
    lost_game = models.CharField(max_length=100, blank=True)
    draw_game = models.CharField(max_length=100 , blank= True)
    goal_difference = models.CharField(max_length=100, blank=True)
    points_game = models.CharField(max_length=100, blank=True)

    def __str__(self):

        	return  self.rank_team + "|" + self.team_name + " | " + self.game_played + "|" + self.won_game  + "|" + self.lost_game + "|"+self.draw_game+"|" + self.goal_difference + "|" + self.points_game