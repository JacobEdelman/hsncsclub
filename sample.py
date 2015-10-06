# Written in 2015 by Jacob Edelman based off work by nickolas360 (https://github.com/nickolas360)
#
# To the extent possible under law, the author(s) have
# dedicated all copyright and related and neighboring
# rights to this software to the public domain worldwide.
# This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain
# Dedication along with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.


from pyrcb import IRCBot
from datetime import datetime
import random

chan = "#hsncsclub"
class ExampleBot(IRCBot):
    def on_message(self, message, nickname, channel, is_query):
        if is_query:
            pass
        else:
            self.send(channel, nickname + ": " + msg)


def main():
    bot = ExampleBot(debug_print=True)
    bot.connect("irc.freenode.net", 6667)
    bot.register("testbot" + str(random.randint(0,1000)))
    bot.join("#hsncsclub")

    # Blocking; will return when disconnected.
    bot.listen()
    print("Disconnected from server.")

if __name__ == "__main__":
    main()

