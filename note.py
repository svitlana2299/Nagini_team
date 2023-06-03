class Note:
    def __init__(self):
        self.notes = []

    def add_notes(self, note, tags):
        dict_note = {'note': note, 'tags': tags}
        self.notes.append(dict_note)
        print(f"{note} добавлено")

    def __str__(self) -> str:
        return f"{self.notes}"

    def search_notes(self, word):
        result_search = []
        for note in self.notes:
            if word.lower() in note['note'].lower() or word.lower() in note['tags'].lower():
                result_search.append(note)
        if result_search:
            for note in result_search:
                print(note['note'])
        else:
            print("Замітки не знайдено")

    def edit_note_by_index(self, index, new_note):
        if index >= 0 and index < len(self.notes):
            self.notes[index]['note'] = new_note
            print("Замітка відредагована")
        else:
            print("Невірний індекс замітки")

    def edit_note_by_keyword(self, keyword, new_note):
        found = False
        for note in self.notes:
            if note['tags'].lower() == keyword.lower():
                note['note'] = new_note
                found = True
                break

        if found:
            print("Замітка відредагована")
        else:
            print(f"Замітка за ключовим словом '{keyword}' не знайдена")

    def delete_note_by_index(self, index):
        if index >= 0 and index < len(self.notes):
            del self.notes[index]
            print("Замітка видалена")
        else:
            print("Невірний індекс замітки")

    def delete_note_by_keyword(self, keyword):
        found = False
        for note in self.notes:
            if note['tags'].lower() == keyword.lower():
                self.notes.remove(note)
                found = True

        if found:
            print("Замітка з вказаним ключовим словом видалена")
        else:
            print(
                f"Замітки з вказаним ключовим словом '{keyword}' не знайдено")

    def sort_notes_alphabetically(self):
        sorted_notes = sorted(self.notes, key=lambda x: x['note'].lower())
        if sorted_notes:
            print("Відсортовані замітки:")
            for note in sorted_notes:
                print(note['note'])
        else:
            print("Замітки для сортування не знайдено")


test = Note()
test.add_notes('В вечері буде мітинг о 22:10', 'Мітинг, Засідання')
print(test)
test.search_notes('мітинг')
test.delete_note_by_index(0)
