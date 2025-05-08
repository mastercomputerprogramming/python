from collections import deque
import heapq
from abc import ABC, abstractmethod

class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.courses = {}  # Hash table for O(1) access
        self._gpa = 0.0
        self.grade_history = []  # Stack for undo/redo

    def add_grade(self, course, grade):
        GRADE_POINTS = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 
                       'B':3.0, 'B-':2.67, 'C+':2.33, 'C':2.0,
                       'D+':1.33, 'D':1.0, 'F':0.0}
        if grade not in GRADE_POINTS:
            raise ValueError("Invalid grade")
        self.grade_history.append((course, grade))  # For undo
        self.courses[course] = GRADE_POINTS[grade]
        self._update_gpa()

    def _update_gpa(self):
        total = sum(self.courses.values())
        self._gpa = total / len(self.courses) if self.courses else 0.0

    def get_gpa(self):
        return round(self._gpa, 2)

class CourseGraph:
    def __init__(self):
        self.prerequisites = {}  # Adjacency list graph

    def add_prerequisite(self, course, prerequisite):
        self.prerequisites.setdefault(course, set()).add(prerequisite)

    def has_met_prerequisites(self, course, completed_courses):
        visited = set()
        queue = deque(self.prerequisites.get(course, []))
        while queue:
            prereq = queue.popleft()
            if prereq not in completed_courses:
                return False
            for next_prereq in self.prerequisites.get(prereq, []):
                if next_prereq not in visited:
                    queue.append(next_prereq)
            visited.add(prereq)
        return True

class StudentManager:
    def __init__(self):
        self.students = {}  # Hash table for O(1) access
        self.course_graph = CourseGraph()
        self.enrollment_queue = deque()  # Queue for processing
        self.undo_stack = []  # Stack for undo operations

    def add_student(self, student):
        if student.id in self.students:
            raise ValueError("Duplicate student ID")
        self.students[student.id] = student
        heapq.heappush(self.student_heap, (-student.get_gpa(), student.id))

    def process_enrollments(self):
        while self.enrollment_queue:
            student_id, course = self.enrollment_queue.popleft()
            if student_id in self.students:
                # Implement actual enrollment logic
                pass

    def get_top_performers(self, n=5):
        return heapq.nlargest(n, self.students.values(), key=lambda x: x.get_gpa())

    def find_course_conflicts(self):
        conflict_graph = {}
        for student in self.students.values():
            courses = list(student.courses.keys())
            for i in range(len(courses)):
                for j in range(i+1, len(courses)):
                    conflict_graph.setdefault(courses[i], set()).add(courses[j])
                    conflict_graph.setdefault(courses[j], set()).add(courses[i])
        return conflict_graph

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class AddGradeCommand(Command):
    def __init__(self, student, course, grade):
        self.student = student
        self.course = course
        self.grade = grade

    def execute(self):
        self.student.add_grade(self.course, self.grade)

# Interactive Menu System
def main_menu():
    manager = StudentManager()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Course Enrollment")
        print("4. Generate Reports")
        print("5. Undo Last Action")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            student_id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            manager.add_student(Student(student_id, name))
            
        elif choice == '2':
            student_id = int(input("Enter student ID: "))
            course = input("Enter course name: ")
            grade = input("Enter grade: ")
            try:
                manager.students[student_id].add_grade(course, grade)
            except KeyError:
                print("Student not found!")
                
        elif choice == '6':
            break

from math import sqrt
import heapq
from collections import deque
import random

class EnhancedStudentManager(StudentManager):
    def __init__(self):
        super().__init__()
        self.performance_model = None
        self.at_risk_model = None
        self.course_recommender = None

    def train_performance_predictor(self):
        """Logistic regression to predict course success"""
        dataset = self._prepare_training_data()
        n_folds = 5
        l_rate = 0.1
        n_epoch = 100
        scores = self.evaluate_algorithm(dataset, self.logistic_regression, 
                                       n_folds, l_rate, n_epoch)
        print(f"Model trained. Average accuracy: {sum(scores)/len(scores):.2f}%")

    def predict_course_success(self, student_id, course):
        """Predict likelihood of success in a course"""
        student = self.students.get(student_id)
        if not student:
            raise ValueError("Student not found")
        
        input_features = self._extract_features(student)
        prediction = self._logistic_predict(input_features)
        return f"Success probability: {prediction*100:.1f}%"

    def _prepare_training_data(self):
        """Convert student records to ML-ready format"""
        dataset = []
        for student in self.students.values():
            features = [
                student.get_gpa(),
                len(student.courses),
                sum(student.courses.values())/len(student.courses)
            ]
            outcome = 1 if student.get_gpa() > 3.0 else 0
            dataset.append(features + [outcome])
        return dataset

    def _logistic_predict(self, row, coefficients=None):
        """Core prediction function from your file"""
        if not coefficients:
            coefficients = [-0.406605464, 0.852573316, -1.104746259]  # Pretrained
        yhat = coefficients[0]
        for i in range(len(row)):
            yhat += coefficients[i+1] * row[i]
        return 1.0 / (1.0 + exp(-yhat))

    def early_warning_system(self):
        """Identify at-risk students using perceptron"""
        at_risk = []
        for student in self.students.values():
            features = [student.get_gpa(), len(student.courses)]
            if self._perceptron_predict(features):
                at_risk.append(student)
        return at_risk

    def _perceptron_predict(self, row):
        """Perceptron implementation from your file"""
        weights = [-0.1, 0.206, -0.234]  # Example weights
        activation = weights[0]
        for i in range(len(row)):
            activation += weights[i+1] * row[i]
        return activation < 0.5

# Interactive ML Menu Extension
def ml_menu(manager):
    while True:
        print("\nMachine Learning Features")
        print("1. Train Performance Predictor")
        print("2. Predict Course Success")
        print("3. Generate Early Warnings")
        print("4. Return to Main")
        
        choice = input("Choose ML option: ")
        
        if choice == '1':
            manager.train_performance_predictor()
        elif choice == '2':
            student_id = int(input("Enter student ID: "))
            course = input("Course to predict: ")
            print(manager.predict_course_success(student_id, course))
        elif choice == '3':
            at_risk = manager.early_warning_system()
            print(f"At-risk students: {[s.name for s in at_risk]}")
        elif choice == '4':
            break


if __name__ == "__main__":
    mgr = EnhancedStudentManager()
    # ... (existing student setup)

    # Add ML capabilities
    main_menu()
    ml_menu(mgr)
    #main_menu()

