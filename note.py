class Note:
    def __init__(self, note, tags):
        self.note = note
        self.tags = tags


    def __repr__(self) -> str:
        return f"{self.note}"

    def __str__(self):
        return f"Note: {self.note}"

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.note == other.note and self.tags == other.tags
        return False

    def __getitem__(self, key):
        if key == 'tags':
            return self.tags
        elif key == 'note':
            return self.note
        else:
            raise KeyError(f"Invalid key: {key}")


class NoteManager:
    def __init__(self):
        self.notes = {}

    def __str__(self) -> str:
        return f"{self.notes}"

    def __repr__(self) -> str:
        return f"{self.notes}"

    def add_notes(self, note, tags):
        new_note = Note(note, tags)
        for tag in tags:
            if tag in self.notes:
                self.notes[tag].append(new_note)
            else:
                self.notes[tag] = [new_note]
        print(f"Note added: {new_note}")

    def search_notes(self, word):
        result_search = []
        for notes in self.notes.values():
            for note in notes:
                if word.lower() in note.note.lower() or any(word.lower() in tag.lower() for tag in note.tags):
                    result_search.append(note)
        if result_search:
            for note in result_search:
                print(note.note)
        else:
            print("No notes found")

    def edit_note_by_index(self, index, new_note):
        found = False
        for notes in self.notes.values():
            if index >= 0 and index < len(notes):
                notes[index].note = new_note
                found = True
                break

        if found:
            print("Note edited")
        else:
            print("Invalid note index")

    def edit_note_by_keyword(self, keyword, new_note):
        found = False
        for notes in self.notes.values():
            for note in notes:
                if keyword.lower() in note.tags:
                    note.note = new_note
                    found = True
                    break

        if found:
            print("Note edited")
        else:
            print(f"No note found with keyword '{keyword}'")

    def delete_note_by_index(self, index):
        found = False
        for notes in self.notes.values():
            if index >= 0 and index < len(notes):
                del notes[index]
                found = True
                break

        if found:
            print("Note deleted")
        else:
            print("Invalid note index")

    def delete_note_by_keyword(self, keyword):
        found = False
        for tag, notes in self.notes.items():
            for index, note in enumerate(notes):
                if keyword.lower() in note.tags:
                    del notes[index]
                    found = True
                    break

        if found:
            print("Note with the specified keyword deleted")
        else:
            print(f"No notes found with keyword '{keyword}'")

    def sort_notes_alphabetically(self):
        sorted_notes = sorted(self.notes.values(),
                              key=lambda x: x[0].note.lower())
        if sorted_notes:
            print("Sorted notes:")
            for notes in sorted_notes:
                for note in notes:
                    print(note.note)
        else:
            print("No notes found for sorting")


test = NoteManager()
test.add_notes('В вечері буде мітинг о 22:10', ['Мітинг', 'Засідання'])
print(test)
test.search_notes('мітинг')
test.add_notes('салат, стейк, коктель', ['Меню'])
print(test.notes)
