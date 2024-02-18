import os
import json
from IPython.display import display, Markdown, clear_output
import ipywidgets as widgets
from ipywidgets import Layout
import requests


class Discussion():
    def __init__(self, question_id, questions, submit_url, net_id):
        self.question_id = question_id
        self.net_id = net_id
        self.boxes = [widgets.VBox([widgets.Label(value=q), widgets.Textarea(
            rows=2, layout=Layout(width='99%'))]) for q in questions]
        self.save_button = widgets.Button(description="Save Answers")
        self.submit_url = submit_url
        for box in self.boxes:
            box.children[1].observe(
                lambda change: self.save_answers(), names='value')
        self.refresh()
        self.save_button.on_click(self.get_responses)

    def refresh(self):
        if os.path.exists(self.question_id):
            with open(self.question_id, 'r') as f:
                answers = json.load(f)
            for box, answer in zip(self.boxes, answers):
                box.children[1].value = answer
        display(*self.boxes, self.save_button)
        self.print_answers()

    def print_answers(self):
        for box in self.boxes:
            display(
                Markdown(f"**{box.children[0].value}**\n\n{box.children[1].value}"))

    def save_answers(self):
        answers = [box.children[1].value for box in self.boxes]
        with open(self.question_id, 'w') as f:
            json.dump(answers, f)

    def get_responses(self, x):
        clear_output(wait=True)
        self.save_answers()
        self.submit_answers()
        self.refresh()

    def submit_answers(self):
        answers = [box.children[1].value for box in self.boxes]
        data = {
            "net_id": self.net_id,
            "answers": answers,
            "question": self.question_id
        }
        try:
            response = requests.post(self.submit_url, json=data)
            if response.status_code == 200:
                print("Answers submitted successfully!")
            else:
                print(
                    f"Failed to submit answers: {response.status_code}, {response.text}")
        except Exception as e:
            print(f"An error occurred while submitting answers: {str(e)}")

# Example usage:
# discussion = Discussion("answers.json", ["Question 1", "Question 2"], False, "http://example.com/submit", "student_net_id")
# Make sure to replace "http://example.com/submit" with your actual submit URL and "student_net_id" with the actual net ID.
