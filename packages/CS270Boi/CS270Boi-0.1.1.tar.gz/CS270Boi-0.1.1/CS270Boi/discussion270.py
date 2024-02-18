import os
import json
from IPython.display import display, clear_output, Markdown
from ipywidgets import widgets, Layout


class Discussion():
    def __init__(self, answers_file, questions, has_drive):
        self.answers_file = answers_file if not has_drive else f"/content/drive/MyDrive/CS270/{answers_file}"
        self.boxes = [widgets.VBox([widgets.Label(value=q), widgets.Textarea(
            rows=2, layout=Layout(width='99%'))]) for q in questions]
        self.save_button = widgets.Button(description="Save Answers")
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
        self.save_answers()
        self.refresh()
