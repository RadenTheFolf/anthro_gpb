from tinydb import TinyDB, Query


class WordDB:
    DB_PATH = "data/db/words.json"

    def add_word(self, word):
        new_word = {
            "word_value": word,
            "xp_value": 0,
            "times_used": 1
        }

        db = TinyDB(self.DB_PATH)
        db.insert(new_word)
        db.close()

    def find_word(self, word_to_find):
        word = Query()
        db = TinyDB(self.DB_PATH)
        found = db.search(word.word_value == word_to_find)
        db.close()
        return found

    def update_xp(self, word_obj):
        word = Query()
        db = TinyDB(self.DB_PATH)
        current_count = word_obj.get("times_used")
        if current_count > 25:
            word_len = len(word_obj.get("word_value"))
            xp_earned = 0
            if word_len <= 2:
                xp_earned += 0.25

            if 3 <= word_len <= 5:
                xp_earned += 1

            if word_len >= 6:
                xp_earned += 1.5

            db.update({"xp_value": xp_earned}, word.word_value == word_obj.get("word_value"))

        db.close()

    def update_count(self, word_obj):
        word = Query()
        db = TinyDB(self.DB_PATH)
        current_count = word_obj.get("times_used")
        current_count += 1
        db.update({"times_used": current_count}, word.word_value == word_obj.get("word_value"))
        db.close()

    def get_xp_value(self, word_to_find):
        found = self.find_word(word_to_find)
        if len(found) > 0:
            for item in found:
                self.update_count(item)
                self.update_xp(item)
                return item.get("xp_value")
        else:
            self.add_word(word_to_find)
            return 0
