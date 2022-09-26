from Bot import cmdmgr
import random

msgs = [
    "Ay AY AY! its UltimateBot Back with another Youtube Tutorial Where We will- \nOh Wait im a bot,\noh well @UltimateBot help for commands.",
    "sup dudez its UltimateBot Here! Use @UltimateBot help For help Broz!",
    "UltimateBot Version ?.?.?, Use @UltimateBot help For help",
    "Hey guys its loser- I mean UltimateBot Here",
    "Hello and welcome to UltimateBot's lessons of the science of yyiyasiyahiyahiyyahi-- \n oh wait I'm a bot I can't give lessons in the science of yyiyasiyahiyahiyyahi",
    "@UltimateBot help /ref",
    "are you /j or /srs? Also hello",
    "@UltimateBot help And yyiyasiyahiyahiyyahi yyiyasiyahiyahiyyahi /ref",
    "Actually, UltimateBot isnt a real bot 🤓🤓🤓🤓",
    "Meower Dope, Meower all day",
    "Eat Sleep Meower Repeat",
    "Uhhhhh Hi."
]

def test(func):
    func.__code__.args.one = "two"

from MeowerBot import Client

def send_msg(msg):
    c._wss.sendPacket(
        {
            "cmd": "direct",
            "val": {
                "cmd": "post_chat",
                "val": {"chatid": "", "p": msg},
            },
        }
    )

def on_raw_msg(msg):
    if "post_origin" in msg.keys():
        cmdmgr.cbcheck_home(msg,c)

def on_login():
    randommsg = msgs[random.randint(0,len(msgs)-1)]
    send_msg(randommsg)
    c.send_msg(randommsg)

def on_error(data):
    print(data)
    send_msg("Internal Bot Error: " + data + ", Closing Websocket Connection Incase of spam.")
    c._wss.close()

def on_status_change(code):
    print("Error code for Bot: "+code)
    send_msg("Statuscode: " + code + " Sent.")

c = Client("","",True)

c.callback(on_raw_msg)
c.callback(on_error)
c.callback(on_login)
c.callback(on_status_change)

c.start()