class Label:
    def __init__(self, label_element):
        self.element = label_element

    def get_text(self):
        return self.element.text
