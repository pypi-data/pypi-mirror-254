import os
import json
from IPython.display import display, Markdown, clear_output
import ipywidgets as widgets
from ipywidgets import Layout
import requests


class Discussion():
    def __init__(self, question_id, questions, url, net_id):
        self.question_id = question_id
        self.net_id = net_id
        self.boxes = [widgets.VBox([widgets.Label(value=q), widgets.Textarea(
            rows=2, layout=Layout(width='99%'))]) for q in questions]
        self.save_button = widgets.Button(description="Save Answers")
        self.url = url + "/submit"
        for box in self.boxes:
            box.children[1].observe(
                lambda change: self.save_answers(), names='value')
        self.refresh()
        self.save_button.on_click(self.get_responses)

    def fetch_answers(self):
        fetch_url = self.url + "/fetch"
        data = {
            "net_id": f"{self.net_id}_{self.question_id}",
            "question": self.question_id
        }
        response = requests.post(fetch_url, json=data)
        if response.status_code == 200:
            return response.json()['answers']
        else:
            print(
                f"Failed to fetch answers: {response.status_code}, {response.text}")
            return []

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
        except Exception as e:
            print(f"An error occurred while saving answers: {str(e)}")

    def get_responses(self, x):
        clear_output(wait=True)
        self.save_answers()  # This will now save to DynamoDB through your backend
        self.refresh()  # This will fetch updated answers from DynamoDB

    def submit_answers(self):
        self.save_answers()  # Directly use save_answers to submit to DynamoDB
