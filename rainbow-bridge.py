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

# names of channels to relay (according to libpurple naming standards)
# TODO: maybe support more than two

bridge_me = [
    "#botwar",
    "19:bf984b822da9402c98aa8021323a817f@thread.skype"
    ]

chat = {}

from pydbus import SessionBus
from gi.repository import GObject

def debug_print(target_conv, send_me):
    print target_conv, ">>>", "\"" + send_me + "\"" + " [" + send_me.encode('hex_codec') + "]"
    
def chat_msg_cb(account, sender, message, conv, flags):

    print sender + " said: " + message, "///", conv, flags, account, message.encode('hex_codec')
    
    if conv in chat.keys() and chat[conv] != sender:
    
        if message[:4] == "/me ":
            send_me = "/me " + sender + " " + message[4:]
        else:
            send_me = "<" + sender + "> " + message
        	
        if "<e_m ts=\"" in send_me:
        	send_me = send_me.split("<e_m ts=\"")[0] + " (ed)"
        
        target_conv = next(iter(set(chat)-set([conv])))
        purple.PurpleConvChatSend(purple.PurpleConversationGetChatData(target_conv), send_me)
        debug_print(target_conv, send_me)

def chat_joined_cb(conv, name, new_arrival, flags):
    print name + " joined:", conv, new_arrival, flags

    if conv in chat.keys():
    
        send_me = name + "++"

        target_conv = next(iter(set(chat)-set([conv])))
        purple.PurpleConvChatSend(purple.PurpleConversationGetChatData(target_conv), send_me)
        debug_print(target_conv, send_me)
        
def chat_left_cb(conv, name, reason):
    print name + " left:", conv, "because: " + reason

    if conv in chat.keys():
    
        send_me = name + "--"
        
        if len(reason) > 0:
            send_me += " (" + reason + ")"

        target_conv = next(iter(set(chat)-set([conv])))
        purple.PurpleConvChatSend(purple.PurpleConversationGetChatData(target_conv), send_me)
        debug_print(target_conv, send_me)

# start main proc

bus = SessionBus()
purple = bus.get("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")

print ">>> Rainbow 🌈 Bridge for Libpurple/Finch/Pidgin <<<"

for conv in purple.PurpleGetConversations():
    if purple.PurpleConversationGetName(conv) in bridge_me:
    	#print purple.PurpleConversationGetName(conv)
    	chat[conv] = purple.PurpleConvChatGetNick(purple.PurpleConversationGetChatData(conv))

for conv in chat.keys():
	print "<->", chat[conv], "on", purple.PurpleConversationGetName(conv), conv

purple.ReceivedChatMsg.connect(chat_msg_cb)
purple.ChatBuddyJoined.connect(chat_joined_cb)
purple.ChatBuddyLeft.connect(chat_left_cb)

print "((( listening )))"

GObject.MainLoop().run()

