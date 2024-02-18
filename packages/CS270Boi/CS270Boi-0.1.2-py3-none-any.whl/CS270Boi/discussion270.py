import os
import json
from IPython.display import display, Markdown, clear_output
import ipywidgets as widgets
from ipywidgets import Layout
import requests  # Import the requests library


class Discussion():
    def __init__(self, answers_file, questions, has_drive, submit_url):
        self.answers_file = answers_file if not has_drive else f"/content/drive/MyDrive/CS270/{answers_file}"
        self.boxes = [widgets.VBox([widgets.Label(value=q), widgets.Textarea(
            rows=2, layout=Layout(width='99%'))]) for q in questions]
        self.save_button = widgets.Button(description="Save Answers")
        self.submit_url = submit_url  # URL to submit answers
        for box in self.boxes:
            box.children[1].observe(
                lambda change: self.save_answers(), names='value')
        self.refresh()
        self.save_button.on_click(self.get_responses)

    def refresh(self):
        if os.path.exists(self.answers_file):
            with open(self.answers_file, 'r') as f:
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
        with open(self.answers_file, 'w') as f:
            json.dump(answers, f)

    def get_responses(self, x):
        clear_output(wait=True)
        self.save_answers()  # Save answers locally
        self.submit_answers()  # Submit answers to the backend
        self.refresh()

    def submit_answers(self):
        # Prepare the data to be submitted
        answers = [box.children[1].value for box in self.boxes]
        data = {
            # This should be dynamically obtained or entered by the student
            "net_id": "student_net_id",
            "answers": answers
        }
        try:
            response = requests.post(self.submit_url, json=data)
            if response.status_code == 200:
                print("Answers submitted successfully!")
            else:
                print("Failed to submit answers:", response.text)
        except Exception as e:
            print("An error occurred while submitting answers:", str(e))
