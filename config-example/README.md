This simple config example runs a bot that relays:

* `#botwar` on [Freenode](https://freenode.net)
* `#bots` on [Rizon](https://rizon.net/)

You can add any number of [chats/channels](bots.conf) to this relay from any of Libpurple accounts (including ones provided by 3rd party plugins). Various chat protocols have different naming standards for channels, so see how Libpurple displays them in [config](.purple/blist.xml) after you have added them from Finch/Pidgin UI. Use exactly the same name in Rainbow Bridge config and don't forget to make Finch auto-join the chat, so the script will start to relay without a need for further assistance.

The directory [.purple](.purple) is copied here just for example. Presuming you haven't configured Finch/Pidgin yet you can set everything up for a test run using:

	$ ln -s $(pwd)/.purple ~
	$ ./start.sh

Make sure you have installed packages for `screen` and `finch`. In Debian based systems probably something like:

	$ sudo apt-get install finch screen

This bridge is meant to be a generic one to be easily modified, so have a look at [source code](../rainbow-bridge.py) and fork it any way you want to.
