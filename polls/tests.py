from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionModelTests(TestCase):
    def test_published_recently_from_future(self):
        time = timezone.now() + timedelta(30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.published_recently(), False)


    def test_published_recently_with_old_question(self):
        time = timezone.now() - timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.published_recently(), False)


    def test_published_recently_with_recent_question(self):
        time = timezone.now() - timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.published_recently(), True)