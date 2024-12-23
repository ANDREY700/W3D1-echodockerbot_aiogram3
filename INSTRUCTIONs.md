# Telegram Bot
<!-- Horizontal Line -->

## A project bot has been prepared in Telegram, which performs the only function of converting any Cyrillic text into Latin.
<!-- Horizontal Line -->


### The main use of this bot is as follows:
Function accepts FULL name in cyrillic and answer full names in Latin as a messages
in accordance with the Order of the Ministry of Foreign Affairs.



### Instructions for using the bot:

1. To use the bot, you need to have docker already installed on your computer.

2. Clone the bot folder to your computer

3. First you need to register the bot in Telegram. To do this, you need to find the @BotFather chat in the Telegram application and run the 
```
    /newbot 
```
command. Нou will be asked for the name of the future bot and you will receive the following type of message :
```
Done! Congratulations on your new bot. You will find it at t.me/<your_bot_name>. You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.

Use this token to access the HTTP API:

<bot_number>:<bot_secret_code>

Keep your token secure and store it safely, it can be used by anyone to control your bot.

For a description of the Bot API, see this page: https://core.telegram.org/bots/api
```

4. You need to copy the <bot_number>:<bot_secret_code> from this message and paste it into the 'dockerfile' at the clonned folder:
```
    ENV TOKEN='<bot_number>:<bot_secret_code>'
```
After these changes, the file should be saved.

5. Go to the project folder via the command prompt and run the image creation command as follows:
```
    docker build .
```

6. After completing the creation of the docker image, you need to find its ID. To do this, run the following command:
```
    docker images
```
```
REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
<none>       <none>    2770da10c0f0   3 hours ago   336MB
```
In this message, docker needs to copy the ID of the created image - "2770da10c0f0". In your case, the image ID will have a different name.

7. run the created image for execution by the following command:
```
    docker run -d -p 81:80 2770da10c0f0 
```

8. Interaction with the bot in Telegram begins with the command 
```
    /Start
```

9. You can stop the bot by using Ctrl-C on the same command line.
