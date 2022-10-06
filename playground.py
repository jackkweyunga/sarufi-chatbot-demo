from sarufi import Sarufi
from decouple import config


def run():
    if not (config("SARUFI_EMAIL", None) or config("SARUFI_PASS", None),
            config("SARUFI_CHATBOT_ID", None)):
        raise Exception("Did you forget to add [SARUFI_EMAIL,SARUFI_PASS] as environment variables. Create a .env "
                        "file instead.")

    sarufi = Sarufi(config("SARUFI_EMAIL"), config("SARUFI_PASS"))
    chatbot = sarufi.get_bot(config("SARUFI_CHATBOT_ID", cast=int))

    print("Dialog. Press Ctrl + c to quit.")
    while True:
        message = input("message > ")
        print("response > ", chatbot.respond(message)["message"])


if __name__ == "__main__":
    run()
