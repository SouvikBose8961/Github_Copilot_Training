from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, type='Test Activity', duration=10)
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=50)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_workout_creation(self):
        self.assertEqual(self.workout.difficulty, 'Easy')

    def test_activity_creation(self):
        self.assertEqual(self.activity.duration, 10)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 50)
