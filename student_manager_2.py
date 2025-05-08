import heapq
from collections import deque
from math import sqrt, exp
import random

# --- Minimal ML functions from your dataScience.py (adapted for students) ---

def mean(values):
    return sum(values) / float(len(values))

def variance(values, mean):
    return sum([(x - mean) ** 2 for x in values])

def covariance(x, mean_x, y, mean_y):
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - mean_x) * (y[i] - mean_y)
    return covar

def coefficients(dataset):
    x = [row[0] for row in dataset]
    y = [row[1] for row in dataset]
    mean_x, mean_y = mean(x), mean(y)
    b1 = covariance(x, mean_x, y, mean_y) / variance(x, mean_x)
    b0 = mean_y - b1 * mean_x
    return [b0, b1]

def simple_linear_regression(train, test):
    predictions = list()
    b0, b1 = coefficients(train)
    for row in test:
        yhat = b0 + b1 * row[0]
        predictions.append(yhat)
    return predictions

def predict(row, weights):
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i+1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0

def train_weights(train, l_rate, n_epoch):
    weights = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        for row in train:
            prediction = predict(row, weights)
            error = row[-1] - prediction
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row)-1):
                weights[i+1] = weights[i+1] + l_rate * error * row[i]
    return weights

def perceptron(train, test, l_rate, n_epoch):
    predictions = list()
    weights = train_weights(train, l_rate, n_epoch)
    for row in test:
        prediction = predict(row, weights)
        predictions.append(prediction)
    return predictions

# --- Core Student Management System ---

class Student:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.courses = {}  # course: grade point
        self._gpa = 0.0

    def add_grade(self, course, grade):
        GRADE_POINTS = {'A+':4.0, 'A':4.0, 'A-':3.67, 'B+':3.33, 
                        'B':3.0, 'B-':2.67, 'C+':2.33, 'C':2.0,
                        'D+':1.33, 'D':1.0, 'F':0.0}
        if grade not in GRADE_POINTS:
            raise ValueError("Invalid grade")
        self.courses[course] = GRADE_POINTS[grade]
        self._update_gpa()

    def _update_gpa(self):
        total = sum(self.courses.values())
        self._gpa = total / len(self.courses) if self.courses else 0.0

    def get_gpa(self):
        return round(self._gpa, 2)

class StudentManager:
    def __init__(self):
        self.students = {}
        self.student_heap = []
        self.enrollment_queue = deque()

    def add_student(self, student):
        if student.id in self.students:
            raise ValueError("Duplicate student ID")
        self.students[student.id] = student
        heapq.heappush(self.student_heap, (-student.get_gpa(), student.id))

    def add_grade(self, student_id, course, grade):
        if student_id not in self.students:
            print("Student not found.")
            return
        self.students[student_id].add_grade(course, grade)
        # Update heap
        self.student_heap = [(-s.get_gpa(), s.id) for s in self.students.values()]
        heapq.heapify(self.student_heap)

    def get_top_performers(self, n=5):
        top = heapq.nsmallest(n, self.student_heap)
        return [(self.students[student_id].name, -gpa) for gpa, student_id in top]

    # --- ML: Predict if a student is at risk using perceptron ---
    def train_perceptron_on_students(self):
        # For demo: GPA < 2.5 is at risk (label 1), else 0
        dataset = []
        for s in self.students.values():
            dataset.append([s.get_gpa(), len(s.courses), 1 if s.get_gpa() < 2.5 else 0])
        if len(dataset) < 2:
            print("Not enough data to train.")
            return None
        l_rate = 0.1
        n_epoch = 10
        weights = train_weights(dataset, l_rate, n_epoch)
        return weights

    def predict_at_risk(self, student_id, weights):
        s = self.students.get(student_id)
        if not s:
            return "Student not found"
        row = [s.get_gpa(), len(s.courses), None]
        pred = predict(row, weights)
        return "At risk" if pred == 1.0 else "Not at risk"

    # --- ML: Predict next GPA using regression ---
    def predict_next_gpa(self, student_id):
        s = self.students.get(student_id)
        if not s:
            return "Student not found"
        # Fake previous GPAs for demo
        gpa_history = [random.uniform(2.0, 4.0) for _ in range(3)] + [s.get_gpa()]
        semesters = list(range(1, len(gpa_history)+1))
        reg_data = [[semesters[i], gpa_history[i]] for i in range(len(semesters))]
        b0, b1 = coefficients(reg_data)
        next_semester = semesters[-1] + 1
        predicted_gpa = b0 + b1 * next_semester
        return f"Predicted next GPA: {predicted_gpa:.2f}"

# --- Interactive CLI ---

def main():
    mgr = StudentManager()
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Top Performers")
        print("4. Predict At-Risk Students (ML)")
        print("5. Predict Next GPA (ML)")
        print("6. List All Students")
        print("7. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            sid = int(input("Student ID: "))
            name = input("Name: ")
            try:
                mgr.add_student(Student(sid, name))
                print("Student added.")
            except ValueError as e:
                print(e)
        elif choice == "2":
            sid = int(input("Student ID: "))
            course = input("Course: ")
            grade = input("Grade (A, B+, C, etc): ")
            try:
                mgr.add_grade(sid, course, grade)
                print("Grade added.")
            except ValueError as e:
                print(e)
        elif choice == "3":
            top = mgr.get_top_performers()
            print("Top Performers:")
            for name, gpa in top:
                print(f"{name}: GPA {gpa}")
        elif choice == "4":
            weights = mgr.train_perceptron_on_students()
            if weights:
                for sid, s in mgr.students.items():
                    result = mgr.predict_at_risk(sid, weights)
                    print(f"{s.name} ({sid}): {result}")
        elif choice == "5":
            sid = int(input("Student ID: "))
            print(mgr.predict_next_gpa(sid))
        elif choice == "6":
            for sid, s in mgr.students.items():
                print(f"{sid}: {s.name}, GPA: {s.get_gpa()}, Courses: {list(s.courses.keys())}")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

