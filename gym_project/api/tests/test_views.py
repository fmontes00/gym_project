from rest_framework import status
from rest_framework.test import APITestCase
from gym.models import Equipment, Exercise


class ExerciseTestCase(APITestCase):
    def setUp(self):

        self.equipment = Equipment.objects.create(
            name="equipment 1", description="description 1"
        )

        self.exercise_1 = Exercise.objects.create(
            name="exercise 1",
            description="description 1",
            equipment=self.equipment,
        )
        self.exercise_2 = Exercise.objects.create(
            name="exercise 2",
            description="description 2",
            equipment=self.equipment,
        )

    def test_exercises_list(self):
        """Should return a list of all exercises"""
        # Preconditions
        self.assertEqual(Exercise.objects.count(), 2)

        response = self.client.get("/api/exercises")

        expected = [
            {
                "name": self.exercise_1.name,
                "description": self.exercise_1.description,
                "equipment": self.exercise_1.equipment.id,
            },
            {
                "name": self.exercise_2.name,
                "description": self.exercise_2.description,
                "equipment": self.exercise_2.equipment.id,
            },
        ]

        # Postconditions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    def test_exercises_retrive(self):
        """Should return the exercise with the given id"""

        response = self.client.get(f"/api/exercises/{self.exercise_1.id}")

        expected = {
            "name": self.exercise_1.name,
            "description": self.exercise_1.description,
            "equipment": self.exercise_1.equipment.id,
        }

        # Postconditions
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    def test_exercises_retrive_not_found(self):
        """Should return 404 when given exercise is not found"""

        response = self.client.get("/api/exercises/999")
        expected = {
            "detail": "Exercise not found",
        }

        # Postconditions
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.json(), expected)

    def test_exercises_create(self):
        """Should create a new exercise when given data is valid"""
        # Preconditions
        self.assertEqual(Exercise.objects.count(), 2)
        payload = {
            "name": "new exercise",
            "description": "new description",
            "equipment": self.exercise_1.equipment.id,
        }
        response = self.client.post("/api/exercises", data=payload)

        # Postconditions
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Exercise.objects.count(), 3)

    def test_exercises_create_invalid_data(self):
        """Should return 400 when given data is invalid"""
        # Preconditions
        self.assertEqual(Exercise.objects.count(), 2)
        payload = {
            "name": "new exercise",
        }

        response = self.client.post("/api/exercises", data=payload)

        expected = {"detail": "Given payload is invalid"}

        # Postconditions
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Exercise.objects.count(), 2)
        self.assertEqual(response.json(), expected)

    
    def test_exercises_delete(self):
        """Should delete an exercise when given id is valid"""

        # Preconditions
        self.assertEqual(Exercise.objects.count(), 2)
        
        response = self.client.delete("/api/exercises/1")

        #Postconditions

        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        self.assertEqual(Exercise.objects.count(), 1)

    def test_exercises_delete_invalid_id(self):
        """Should return 404 when given exercise is not found"""

        # Preconditions
        self.assertEqual(Exercise.objects.count(), 2)

        response = self.client.delete("/api/exercises/999")

        #Postconditions
        self.assertEqual(response.status_code,status.HTTP_404_NOT_FOUND)
        self.assertEqual(Exercise.objects.count(), 2)