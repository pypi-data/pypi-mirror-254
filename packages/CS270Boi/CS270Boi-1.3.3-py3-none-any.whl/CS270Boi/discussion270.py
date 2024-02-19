import os
import json
import socket
from IPython.display import display, Markdown, clear_output
import ipywidgets as widgets
from ipywidgets import Layout
import requests
from collections import Counter


def internet_connection_available(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        return False


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
        self.local_save_path = f"local/locally_saved_answers_{self.net_id}_{self.question_id}.json"
        for box in self.boxes:
            box.children[1].observe(
                lambda change: self.save_answers(), names='value')
        self.refresh()
        self.save_button.on_click(self.get_responses)

    def fetch_answers(self):
        if not internet_connection_available():
            return self.load_local_answers()

        if os.path.exists(self.local_save_path):
            data = self.load_local_answers()
            os.remove(self.local_save_path)
            print("Uploaded locally saved answers!")
            return data

        data = {
            "net_id": self.net_id,
        }
        try:
            response = requests.post(self.fetch_url, json=data)
            if response.status_code == 200:
                if self.question_id in response.json():
                    return response.json()[self.question_id]
                else:
                    return []
        except requests.exceptions.RequestException:
            print("Failed to fetch answers due to connectivity issues.")

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
        if not internet_connection_available():
            self.save_local_answers(
                {"answers": [box.children[1].value for box in self.boxes]})
            return

        answers = [box.children[1].value for box in self.boxes]
        data = {
            "net_id": f"{self.net_id}",
            "answers": answers,
            "question": self.question_id
        }
        try:
            response = requests.post(self.submit_url, json=data)
            if response.status_code != 200:
                # print(f"Failed to save answers: {response.status_code}, {response.text}")
                self.save_local_answers(data)
            if os.path.exists(self.local_save_path):
                os.remove(self.local_save_path)
                print("Uploaded locally saved answers")
        except requests.exceptions.RequestException as e:
            # print(f"An error occurred while saving answers: {str(e)}")
            self.save_local_answers(data)

    def get_responses(self, x):
        clear_output(wait=True)
        if not internet_connection_available():
            print("Answers saved locally.")
        self.save_answers()
        self.refresh()

    def submit_answers(self):
        self.save_answers()

    def save_local_answers(self, data):
        if not os.path.exists("local"):
            os.makedirs("local")

        with open(self.local_save_path, 'w') as file:
            json.dump(data, file)

    def load_local_answers(self):
        if os.path.exists(self.local_save_path):
            with open(self.local_save_path, 'r') as file:
                data = json.load(file)
            return data.get('answers', [])
        return []
