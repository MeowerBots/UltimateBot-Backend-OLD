from Bot import cmdmgr

"""
 Ideas:
  meower and discord:
   Get from gd server
   simple hangman game
   rpg text game
   get profile
   ulist
   moderation commands
   votekick user
  main focus:
   meowy upgrade games, you can also battle and catch, earn money and use a shop
  discord only (maybe):
   snake
  
"""

def test(func):
    func.__code__.args.one = "two"

from MeowerBot import Client

def on_raw_msg(data):
    print(data)
    cmdmgr.cbcheck_home(data,c)

c = Client("Uuser","pass",False)

c.callback(on_raw_msg)

c.start()