# Rainbow 🌈 Bridge

Simple relay bot for Libpurple chats using D-Bus with Pidgin/Finch

> Orginally created as replacement for maliciously deprecated P2P chatrooms on Skype [1], but should work for most of the protocols supported by Libpurple, that is AIM, ICQ, Google Talk, Jabber/XMPP, MSN Messenger, Yahoo!, Bonjour, Gadu-Gadu, IRC, Novell GroupWise Messenger, Lotus Sametime, SILC, SIMPLE, MXit, Zephyr [2] and even more with plugins [3]. You can run it on console, if you use Finch instead of Pidgin to run your Libpurple instance for the chatrooms you want to bridge.

Requirements:

* [libpurple](https://developer.pidgin.im/wiki/WhatIsLibpurple)
* [pydbus](https://github.com/LEW21/pydbus)
* [skype4pidgin](https://github.com/EionRobb/skype4pidgin/tree/master/skypeweb) (for original intention)

See [test.sh](test.sh) for an example.

Alternatives:

* https://github.com/bill-auger/bridgin-php

[1] https://github.com/boamaod/skype2irc/issues/7  
[2] https://www.pidgin.im/about/  
[3] https://developer.pidgin.im/wiki/ThirdPartyPlugins#AdditionalProtocols  
