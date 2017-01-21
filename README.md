# Rainbow 🌈 Bridge

Simple relay bot for Libpurple chats using D-Bus with Pidgin/Finch

> Orginally created as a replacement for maliciously deprecated P2P chatrooms on Skype [1], but should work for most of the protocols supported by Libpurple, that is AIM, ICQ, Google Talk, Jabber/XMPP, MSN Messenger, Yahoo!, Bonjour, Gadu-Gadu, IRC, Novell GroupWise Messenger, Lotus Sametime, SILC, SIMPLE, MXit, Zephyr [2] and even more with plugins [3]. You can start it on console, if you use Finch instead of Pidgin to run your Libpurple instance for the chatrooms you want to bridge.

Requirements:

* [libpurple](https://developer.pidgin.im/wiki/WhatIsLibpurple)
* [pydbus](https://github.com/LEW21/pydbus)
* [skype4pidgin](https://github.com/EionRobb/skype4pidgin/tree/master/skypeweb) (for original intention)

See [test.sh](test.sh) for some installation instructions/ideas and use [config-example](config-example) to give it a quick test run. Here are [some real world examples of config files](https://gist.github.com/boamaod/ff8e32634fe42138569cece82ffba6ec).

Alternatives:

* https://github.com/bill-auger/bridgin-php

[1] https://github.com/boamaod/skype2irc/issues/7  
[2] https://www.pidgin.im/about/  
[3] https://developer.pidgin.im/wiki/ThirdPartyPlugins#AdditionalProtocols  

And if you are one of those who think in pictures, maybe this will help you out:

![Pink fluffy unicorns of Libpurple will bridge practically anything!](rainbow.png "Rainbow 🌈 Bridge with pink fluffy unicorns of Libpurple")
