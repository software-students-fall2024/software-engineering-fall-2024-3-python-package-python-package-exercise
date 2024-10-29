import pytest
import time
import schedule 
import random as r 

from physicalexercise import Exercise, activate_exercises, run_exercise

class ExerciseTests: 
    def initialize_exercise(): 
        exercise = Exercise("Jogging", "5 minutes", "12 minutes", "18 minutes", "Cardio")
        assert exercise.name == "Jogging"
        assert exercise.low_intensity_duration == "5 minutes"
        assert exercise.medium_intensity_duration == "12 minutes"
        assert exercise.high_intensity_duration == "18 minutes"
        assert exercise.type == "Cardio"

    def get_exercise_attributes(): 
        exercise = Exercise("Seated Spinal Twist", "30 seconds", "1 minute", "2 minutes", "Stretching")
        assert exercise.get_name() == "Seated Spinal Twist"
        assert exercise.get_low_intensity_duration() == "15"
        assert exercise.get_high_intensity_duration() == "35"
        assert exercise.get_med_intensity_duration() == "25"
        assert exercise.get_type() == "Stretching"
    
    def get_exercise_output_low(capsys):
        exercise = Exercise("Walking", "5 minutes", "10 minutes", "15 minutes", "Cardio")
        exercise.output("low")
        low_output = capsys.readouterr()
        assert "Your exercise is: Walking for 5 minutes" in low_output.out

    def get_exercise_output_med(capsys):
        exercise = Exercise("Walking", "5 minutes", "10 minutes", "15 minutes", "Cardio")
        exercise.output("med")
        low_output = capsys.readouterr()
        assert "Your exercise is: Walking for 10 minutes" in low_output.out 

    def get_exercise_output_high(capsys):  
        exercise = Exercise("Walking", "5 minutes", "10 minutes", "15 minutes", "Cardio")
        exercise.output("high")
        low_output = capsys.readouterr()
        assert "Your exercise is: Walking for 15 minutes" in low_output.out


