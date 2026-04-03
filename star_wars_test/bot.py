import random
from frame import frames
# re: used for regex matching of user input against expected answers
import re
# unicodedata: used for normalizing text by removing accents 
import unicodedata

class FrameBot:

    def __init__(self, role, language):
        self.current_frame = frames[role]
        self.language = language
        self.memory = []
        self.common_ground = []
        self.asked_questions = []
        self.current_question = None
        self.current_question_frame = None

        self.questions = self.current_frame[f"questions_{language}"]
        self.good_responses = self.current_frame[f"good_responses_{language}"]
        self.bad_responses = self.current_frame[f"bad_responses_{language}"]

    # the bot introduces itself and prints the introduction text
    def introduction(self):
        char_name = self.current_frame[f"character_name_{self.language}"]
        intro = self.current_frame[f"intro_{self.language}"]
        print(f"> {char_name}: {intro}")

    # analyze the user input and return True if correct, False otherwise
    def analyze(self, user_input):
        return self.check_answer(user_input)

    # decision is based on the ratio of correct answers to asked questions
    def decision(self, correct, asked):
        return correct / asked if asked > 0 else 0

    # generate a response based on whether the user's answer was correct or not
    def generate(self, correct):
        if correct:
            return random.choice(self.good_responses)
        else:
            return random.choice(self.bad_responses)

    # ask a question that has not been asked before, 
    # return False if no more questions are available
    def ask_question(self):
        available = [question for question in self.questions if question not in self.asked_questions]

        if not available:
            print("\n> " + self.current_frame[f"test_end_{self.language}"])
            return False

        self.current_question = random.choice(available)
        self.current_question_frame = self._initialize_question_frame(self.current_question)
        self.asked_questions.append(self.current_question)

        char_name = self.current_frame[f"character_name_{self.language}"]
        question_text = self.current_question["question"]
        print(f"> {char_name}: {question_text}")
        
        return True

    # build the frame for the current question and initialize its slots
    def _initialize_question_frame(self, question):
        expected_answers = list(question["answers"])

        if question.get("type") == "multi":
            slots = {
                "expected": expected_answers,
                "given": [],
                "result": None,
                "trials": 0,
                "confidence": 0.0,
                "matched": {answer: False for answer in expected_answers},
            }
        else:
            slots = {
                "expected": expected_answers,
                "given": None,
                "result": None,
                "trials": 0,
                "confidence": 0.0,
            }

        return {
            "question": question["question"],
            "type": question.get("type", "single"),
            "slots": slots,
        }

    # normalize text by removing accents and converting to lowercase
    def _normalize_text(self, text):
        normalized = unicodedata.normalize("NFKD", text)
        return "".join(ch for ch in normalized if not unicodedata.combining(ch)).lower()

    # check if the normalized user input contains the normalized answer as a whole word
    def _contains_answer(self, normalized_input, answer):
        normalized_answer = self._normalize_text(answer)

        # checks that either before and after the normalized answer there is no alphanumeric character
        # re.escape is used to match the normalized answer even if it contains special regex characters
        pattern = rf"(?<!\w){re.escape(normalized_answer)}(?!\w)"

        # return True if the pattern is found in the normalized input, False otherwise
        return re.search(pattern, normalized_input) is not None

    # map user input and expected labels to canonical true/false values
    def _to_bool_label(self, text):
        normalized = self._normalize_text(text).strip()

        true_aliases = {"vero", "true", "v", "t"}
        false_aliases = {"falso", "false", "f"}

        for token in true_aliases:
            if self._contains_answer(normalized, token):
                return "true"

        for token in false_aliases:
            if self._contains_answer(normalized, token):
                return "false"

        return None

    def _is_true_false_question(self, question):
        expected_labels = {self._to_bool_label(answer) for answer in question.get("answers", [])}
        expected_labels.discard(None)
        return len(expected_labels) == 1

    # check if the user's answer is correct based on the current question's expected answers
    def check_answer(self, user_input):
        normalized_input = self._normalize_text(user_input)

        q = self.current_question
        q_frame = self.current_question_frame
        slots = q_frame["slots"]
        slots["trials"] += 1

        if self._is_true_false_question(q):
            user_label = self._to_bool_label(normalized_input)
            expected_label = self._to_bool_label(q["answers"][0])

            is_correct = user_label is not None and user_label == expected_label
            slots["given"] = user_label
            slots["result"] = is_correct
            slots["confidence"] = 1.0 if is_correct else 0.0
            return is_correct

        if q.get("type") == "multi":
            for answer in q["answers"]:
                if self._contains_answer(normalized_input, answer):
                    slots["matched"][answer] = True

            matched_answers = [answer for answer, matched in slots["matched"].items() if matched]
            is_correct = all(slots["matched"].values())
            slots["given"] = matched_answers
            slots["result"] = is_correct
            slots["confidence"] = len(matched_answers) / len(slots["expected"]) if slots["expected"] else 0.0
            return is_correct

        for answer in q["answers"]:
            if self._contains_answer(normalized_input, answer):
                slots["given"] = answer
                slots["result"] = True
                slots["confidence"] = 1.0
                return True

        slots["given"] = None
        slots["result"] = False
        slots["confidence"] = 0.0
        return False

    # process the user's answer, update memory
    # return 1 for correct
    # return None for incorrect
    def respond(self, user_input):
        self.memory.append(user_input)

        analysis = self.analyze(user_input)
        self.common_ground.append({
            "question": self.current_question_frame["question"],
            "type": self.current_question_frame["type"],
            "slots": dict(self.current_question_frame["slots"]),
            "correct": analysis,
        })

        if analysis:
            return 1
        else:
            return 

    # provide a final verdict based on the user's performance and print memory
    def verdict(self, asked, correct):
        if asked == 0:
            return

        ratio = correct / asked

        print(f"Score: {correct}/{asked}")

        print("\n--- MEMORY ---")
        for m in self.memory[:]:
            print("> " + m)

        print("\n--- COMMON GROUND ---")
        for item in self.common_ground:
            print(f"> Q: {item['question']}")
            print(f"Slots: {item['slots']}")
            print(f"Correct: {item['correct']}")

        if ratio > 0.6:
            if self.current_frame["tone"] == "calm":
                print("\n> " + random.choice(self.good_responses))
            else:
                print("\n> " + random.choice(self.good_responses).upper())

            
            print("> " + self.current_frame[f"approved_{self.language}"])
        else:
            if self.current_frame["tone"] == "calm":
                print("\n> " + random.choice(self.bad_responses))
            else:
                print("\n> " + random.choice(self.bad_responses).upper())

            print("> " + self.current_frame[f"rejected_{self.language}"])