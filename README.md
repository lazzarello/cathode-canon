# Cathode Canon

A Discord bot to read the contents of a channel of movie schedules hand written by a very nice person. Once parsed into structured data, provide a search/filter interface and some links to letterboxd, streaming and downloads options! Yea!

## Usage

Add the following environment variables into a `.env` file

DISCORD_TOKEN=<your bot token>
DISCORD_USERNAME=<the username who posts messages>
DISCORD_CHANNEL=<the name of the channel with bot access>

## Bot Permissions

The permissions were the most difficult nut to crack, imo. By default, when the bot is added to a server (Guild in their jargon) it can only view the contents of messages written by the bot itself. To give it access to all the message history, the channel and the bot needs some optional permission flags. TODO: what are these flags?

## TODO

* Parse full history to only include movie listings
* Write listings to database
* Create filter UI
* Link data to Letterboxd
* Add public URL!
* Incremental additions with tx/rx bot on the public internet
