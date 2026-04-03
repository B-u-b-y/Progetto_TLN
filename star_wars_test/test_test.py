from bot import FrameBot
import random

def start_test():

    print("Select language: it/en")
    language = input("> ").strip().lower()

    if language not in ("it", "en"):
        print("Invalid language. Defaulting to English.")
        language = "en"

    if language == "it":
        print("Chi vuoi che ti testi (Obi-Wan Kenobi/Darth Vader)")
    else:
        print("Who do you want to be tested by? (Obi-Wan Kenobi/Darth Vader)")

    role = input("> ").strip().lower()

    character_map = {
        "obi-wan": "jedi",
        "obi wan": "jedi",
        "kenobi": "jedi",
        "obi-wan kenobi": "jedi",
        "darth vader": "sith",
        "vader": "sith",
        "lord vader": "sith"
    }

    if role not in character_map:
        if language == "it":
            print("Scelta non valida.")
        else:
            print("Invalid choice.")
        return

    frame_role = character_map[role]

    bot = FrameBot(frame_role, language)
    bot.introduction()

    correct_answers = 0
    asked_questions = 0

    user_input = ""
    while True:
        if user_input.strip().lower() in ("exit", "quit"):
            print("Exiting the test.")
            break
        

        has_question = bot.ask_question() 

        if not has_question or asked_questions == 3:
            bot.verdict(asked_questions, correct_answers)
            break

        asked_questions += 1 
        trials = 0
        
        while True:
            user_input = input("")
            
            if user_input.strip().lower() in ("exit", "quit"):
                break

            result = bot.respond(user_input)
            
            if result == 1:
                correct_answers += 1
                break 
            
            elif result is None:
                trials += 1
                if trials < 3:
                    extract_random = random.randint(1, 100)
                    if(extract_random % 2 == 0):
                        random_key = random.choice(list(bot.current_frame[f"no_understanding_{bot.language}"].keys()))
                        message = bot.current_frame[f"no_understanding_{bot.language}"][random_key]
                        print("> " + message)
                        continue
                    else:
                        break
                else:
                    break

        if user_input.strip().lower() in ("exit", "quit"):
            print("Exiting the test.")
            break



if __name__ == "__main__":
    start_test()