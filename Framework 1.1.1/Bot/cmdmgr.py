import traceback

prefixes = []

blocked = []
blockreason = []

#BotFramework V1.1.1

home = True

client = ""

bots = ["CodeBot","Linux_Anarchy","Comics","Webhooks","UltimateBot"]

def parsecmd(client,command,ctx):
    if not ctx["user"] in blocked:
        if command == "ping":
            send_msg("piong\nhi")
        else:
            #TODO: Random Msgs for invalid command
            send_msg("Sorry but that command, isnt an option.")
    else:
        for i in range(len(blocked)):
            if blocked[i] == ctx["user"]:
                send_msg(blocked[i] + ", You Have been Banned From The  Club For "+blockreason[i]+".")
































































































def transferargs(ctx):
    global client
    client = ctx["client"]
    command = ctx["post"].split(" ")[1]
    parsecmd(client, command, ctx)

def send_msg(msg):
    try:
        if not home:
            client._wss.sendPacket(
                {
                    "cmd": "direct",
                    "val": {
                        "cmd": "post_chat",
                        "val": {"chatid": "", "p": msg},
                    },
                }
            )
        else:
            client.send_msg(msg)
    except:
        pass

"""
    cbcheck_home

    args: data:dict

    check if a messsage is from home then parses the msg
"""
def cbcheck_home(data,c):
    try:
        if not home and data["post_origin"] == "" or home and data["post_origin"] == "home":
            if data["u"] != c.username:
                if data["u"] == "Discord":
                    post = data["p"].split(":")[1][1:]
                    ctx = {
                        "user": data["u"],
                        "post": post,
                        "args": post.split(" ")[2:],
                        "client": c,
                        "raw_msg": "Not currently supported for Discord",
                        "isdiscord": True
                    }
                    if post.startswith(tuple(prefixes)):
                        transferargs(ctx)
                else:
                    ctx = {
                        "user": data["u"],
                        "post": data["p"],
                        "args": data["p"].split(" ")[2:],
                        "client": c,
                        "raw_msg": data,
                        "isdiscord": False
                    }
                    if data["p"].startswith(tuple(prefixes)):
                        transferargs(ctx)
        else:
            if data["p"].startswith(tuple(prefixes)):
                c.send_msg("You dont use the bot here, silly! use it in home (or if its being used in home the group chat)")
    except Exception as e:
        error = traceback.format_exc()
        c.send_msg("Uh oh, I got an error.\nTraceback error:\n"+error)