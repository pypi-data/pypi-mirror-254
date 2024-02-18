import os
import json
from IPython.display import display, Markdown, clear_output
import ipywidgets as widgets
from ipywidgets import Layout
import requests


class Discussion():
    def __init__(self, question_id, questions, net_id):
        self.question_id = question_id
        self.net_id = net_id
        self.boxes = [widgets.VBox([widgets.Label(value=q), widgets.Textarea(
            rows=2, layout=Layout(width='99%'))]) for q in questions]
        self.save_button = widgets.Button(description="Save Answers")
        self.url = "https://gmdsta5199.execute-api.us-east-1.amazonaws.com/Prod"
        self.submit_url = self.url + "/submit"
        self.fetch_url = self.url + "/fetch"
        self.local_save_path = f"saved_answers_{self.net_id}_{self.question_id}.json"
        for box in self.boxes:
            box.children[1].observe(
                lambda change: self.save_answers(), names='value')
        self.refresh()
        self.save_button.on_click(self.get_responses)

    def fetch_answers(self):
        data = {
            "net_id": f"{self.net_id}_{self.question_id}",
            "question": self.question_id
        }
        try:
            response = requests.post(self.fetch_url, json=data)
            if response.status_code == 200:
                return response.json()['answers']
        except requests.exceptions.RequestException:
            pass  # Student boi got no internet
        return self.load_local_answers()

    def print_answers(self):
        for box in self.boxes:
            display(
                Markdown(f"**{box.children[0].value}**\n\n{box.children[1].value}"))

    def refresh(self):
        answers = self.fetch_answers()
        for box, answer in zip(self.boxes, answers):
            box.children[1].value = answer
        display(*self.boxes, self.save_button)
        self.print_answers()

    def save_answers(self):
        answers = [box.children[1].value for box in self.boxes]
        data = {
            "net_id": f"{self.net_id}_{self.question_id}",
            "answers": answers,
            "question": self.question_id
        }
        try:
            response = requests.post(self.submit_url, json=data)
            if response.status_code != 200:
                print(
                    f"Failed to save answers: {response.status_code}, {response.text}")
                # Save locally if submission fails
                self.save_local_answers(data)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while saving answers: {str(e)}")
            # Save locally if an error occurs
            self.save_local_answers(data)

    def get_responses(self, x):
        clear_output(wait=True)
        self.save_answers()
        self.refresh()

    def submit_answers(self):
        self.save_answers()

    def save_local_answers(self, data):
        with open(self.local_save_path, 'w') as file:
            json.dump(data, file)
        print("Answers saved locally due to connectivity issues.")

    def load_local_answers(self):
        if os.path.exists(self.local_save_path):
            with open(self.local_save_path, 'r') as file:
                data = json.load(file)
            return data.get('answers', [])
        return []
