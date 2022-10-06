<samp>

# SAMPLE CHATBOT WITH SARUFI.IO

To follow up with this example, make sure you have registered with sarufi.io.

- Go to [sarufi.io](https://sarufi.io) to create an account.

Sarufi.io provides various ways for a developer to create a chat bot faster and with ease.
One the ways is using configuration files i.e.
- flows.yaml
- intents.yaml
- metadata.yaml

## clone repo
Get this code base working on your machine right away.
```shell
git clone https://github.com/jackkweyunga/sarufi-chatbot-demo.git
# install requirements
cd sarufi-chatbot-demo
pip install -r requirements.txt
```

## create bot

create a `.env` file or add the following as environment variables
```
SARUFI_EMAIL=<user@example.com>
SARUFI_PASS=<sarufi-password>
```

run create-bot.py
```shell
python create-bot.py
```

Note the .env or environment variables with the bot id `SARUFI_CHATBOT_ID=`
```
SARUFI_EMAIL=<user@example.com>
SARUFI_PASS=<sarufi-password>
SARUFI_CHATBOT_ID=<bot-id>
```

To update your bot, just run `create.py` again with the `SARUFI_CHATBOT_ID` environment variable set.

## Test your bot
To test your bot run `playground.py` for a cmd based testing groung.

## Next step
> Learn more about sarufi. Go to [sarufi documentation](https://docs.sarufi.io/docs/intro)

### -- end ---

</samp>