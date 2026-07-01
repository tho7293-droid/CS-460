import unittest
from CS460 import gale_shapley


class TestGaleShapley(unittest.TestCase):

    def test_given_3x3(self):
        """Case 1: Example from the project."""

        group_preferences = {
            "GroupA": ["Room1", "Room2", "Room3"],
            "GroupB": ["Room2", "Room3", "Room1"],
            "GroupC": ["Room1", "Room3", "Room2"],
        }

        room_preferences = {
            "Room1": ["GroupB", "GroupA", "GroupC"],
            "Room2": ["GroupA", "GroupC", "GroupB"],
            "Room3": ["GroupC", "GroupB", "GroupA"],
        }

        expected = {
            "GroupA": "Room1",
            "GroupB": "Room2",
            "GroupC": "Room3",
        }

        self.assertEqual(gale_shapley(group_preferences, room_preferences), expected)

    def test_conflict_heavy(self):
        """Case 2: All groups initially want the same room."""

        group_preferences = {
            "A": ["R1", "R2", "R3"],
            "B": ["R1", "R2", "R3"],
            "C": ["R1", "R2", "R3"],
        }

        room_preferences = {
            "R1": ["C", "B", "A"],
            "R2": ["B", "A", "C"],
            "R3": ["A", "B", "C"],
        }

        expected = {
            "C": "R1",
            "B": "R2",
            "A": "R3",
        }

        self.assertEqual(gale_shapley(group_preferences, room_preferences), expected)

    def test_mixed_4x4(self):
        """Case 3: Four groups and four rooms."""

        group_preferences = {
            "G1": ["R2", "R1", "R3", "R4"],
            "G2": ["R3", "R2", "R1", "R4"],
            "G3": ["R1", "R3", "R2", "R4"],
            "G4": ["R4", "R1", "R2", "R3"],
        }

        room_preferences = {
            "R1": ["G3", "G1", "G2", "G4"],
            "R2": ["G1", "G2", "G3", "G4"],
            "R3": ["G2", "G3", "G1", "G4"],
            "R4": ["G4", "G1", "G2", "G3"],
        }

        expected = {
            "G1": "R2",
            "G2": "R3",
            "G3": "R1",
            "G4": "R4",
        }

        self.assertEqual(gale_shapley(group_preferences, room_preferences), expected)


if __name__ == "__main__":
    unittest.main()