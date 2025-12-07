from abc import ABC, abstractmethod

class GlossaryItem(ABC):

    def __init__(self, key: str):
        self.key = key
        self.translations= {} # dictionary


    def add_translation(self, lang,text):
        if self.translations.get(lang) is not None:
            print(f"{lang}: {text}")
            return
        self.translations[lang] = text

    @abstractmethod
    def describe(self):
        pass


class TermItem(GlossaryItem):
    def __init__(self, key: str):
        super().__init__(key)

    def describe(self):
        return f"Term: {self.key} - {self.translations}"

class AcronymItem(GlossaryItem):

    def __init__(self, key: str, expansion: str):
        super().__init__(key)
        self.expansion = expansion

    def describe(self):
        return f"Acronym: {self.key} - {self.expansion}"


items:list[GlossaryItem]=[
    TermItem("algoritm"),
    AcronymItem("AI", 'Artificial Intelligence')
]

def find_items(key: str , items:list[GlossaryItem]):
    for item in items:
        if item.key == key:
            en= item.translations.get("en", item.key)
            print(en)
            return
    print("Not found")



items[0].add_translation("en", "algorithm")
items[0].add_translation("ro", "algoritm")
items[1].add_translation("ro", "IA")
items[1].add_translation("EN", "AI")

for item in items:
    print(item.describe())

find_items("AI", items)
find_items("IA", items)