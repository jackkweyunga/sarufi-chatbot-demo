from sarufi import Sarufi
from decouple import config


def create():
    if not (config("SARUFI_EMAIL", None) or config("SARUFI_PASS", None)):
        raise Exception("Did you forget to add [SARUFI_EMAIL,SARUFI_PASS] as environment variables. Create a .env "
                        "file instead.")

    sarufi = Sarufi(config("SARUFI_EMAIL"), config("SARUFI_PASS"))

    if config("SARUFI_CHATBOT_ID", None) is not None:
        response = sarufi.update_from_file(
            intents="data/intents.yaml",
            flow="data/flows.yaml",
            metadata="data/metadata.yaml",
            id=config("SARUFI_CHATBOT_ID", cast=int)
        )
    else:
        response = sarufi.create_from_file(
            intents="data/intents.yaml",
            flow="data/flows.yaml",
            metadata="data/metadata.yaml",
        )

    print(response)


if __name__ == "__main__":
    create()
