#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Rainbow 🌈 Bridge: simple relay bot for Libpurple via Pidgin/Finch
# Copyright (C) 2016  Märt Põder <tramm@p6drad-teel.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

from pydbus import SessionBus
from gi.repository import GObject

chat = {}

if len(sys.argv) >= 2: # path to config (same as below) on command prompt

    execfile(sys.argv[1])

else: # names of channels to relay (using libpurple naming standards)

	bridge_me = [
		"#botwar",
		"19:bf984b822da9402c98aa8021323a817f@thread.skype",
		]

class Protocol(object):
    FACEBOOK = "Facebook"
    IRC = "IRC"
    SKYPE = "Skype (HTTP)"

def debug_print(target_conv, send_me):
    print target_conv, ">>>", "\"" + send_me + "\"" #+ " [" + send_me.encode('hex_codec') + "]"
    
def chat_msg_cb(account, sender, message, conv, flags):
    print sender + " said: " + message, "///", conv, flags, account #, message.encode('hex_codec')
    
    if conv in chat and chat[conv]["nick"] != sender:
        if chat[conv]["protocol"] == Protocol.FACEBOOK:
            sender = purple.PurpleBuddyGetAlias(purple.PurpleFindBuddy(account, sender))

        for target_conv in iter(set(chat)-set([conv])):
            
            if message[:4] == "/me " or message[:5] == "\01/me ":
                if chat[target_conv]["protocol"] == Protocol.IRC:
                    send_me = "\01ACTION " + sender + " " + message.split("/me ")[1] + "\01"
                else:
                    send_me = "/me " + sender + " " + message.split("/me ")[1]
            else:
                if chat[target_conv]["protocol"] in (Protocol.SKYPE, Protocol.FACEBOOK):
                    send_me = "&lt;" + sender + "&gt; " + message
                else:
                    send_me = "<" + sender + "> " + message
            
            if chat[target_conv]["protocol"] != Protocol.SKYPE and "<e_m ts=\"" in send_me:
                send_me = send_me.split("<e_m ts=\"")[0] + " (ed)"

            purple.PurpleConvChatSend(purple.PurpleConversationGetChatData(target_conv), send_me)
            debug_print(target_conv, send_me)

def chat_joined_cb(conv, nick, new_arrival, flags):
    print nick + " joined:", conv, new_arrival, flags

    if conv in chat:
        send_me = nick + "++"

        for target_conv in iter(set(chat)-set([conv])):
            purple.PurpleConvChatSend(purple.PurpleConversationGetChatData(target_conv), send_me)
            debug_print(target_conv, send_me)
        
def chat_left_cb(conv, nick, reason):
    print nick + " left:", conv, "because: " + reason

    if conv in chat:
        send_me = nick + "--"

        if len(reason) > 0:
            send_me += " (" + reason + ")"

        for target_conv in iter(set(chat)-set([conv])):
            purple.PurpleConvChatSend(purple.PurpleConversationGetChatData(target_conv), send_me)
            debug_print(target_conv, send_me)

# start main proc

bus = SessionBus()
purple = bus.get("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")

print ">>> Rainbow 🌈 Bridge for Libpurple/Finch/Pidgin <<<"

for conv in purple.PurpleGetConversations():
    if purple.PurpleConversationGetName(conv) in bridge_me:
    	chat[conv] = {
            "nick": purple.PurpleConvChatGetNick(purple.PurpleConversationGetChatData(conv)),
            "protocol": purple.PurpleAccountGetProtocolName(purple.PurpleConversationGetAccount(conv))
            }

for conv in chat.keys():
	print "<->", chat[conv]["nick"], "on", purple.PurpleConversationGetName(conv), "(" + str(conv) + ")", "using", chat[conv]["protocol"]

purple.ReceivedChatMsg.connect(chat_msg_cb)
purple.ChatBuddyJoined.connect(chat_joined_cb)
purple.ChatBuddyLeft.connect(chat_left_cb)

print "((( listening )))"

GObject.MainLoop().run()
