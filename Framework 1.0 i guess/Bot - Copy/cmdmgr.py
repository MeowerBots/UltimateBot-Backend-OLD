from Bot.commands import getgd

prefixes = ["@UltimateBot","!"]

def parsecmd(ctx):
    command = ctx["post"][13:]
    if command == "ping":
        ctx["client"].send_msg("piong\nhi")
    elif command == "help":
        ctx["client"].send_msg(
            "Commands:\n" + 
            prefix + 
            "help\n" + 
            prefix + 
            "ping"
        )



































































































"""
    cbcheck_home

    args: data:dict

    check if a messsage is from home then parses the msg
"""
def cbcheck_home(data,c):
    if data["post_origin"] == "home":
        if data["u"] != c.username:
            if data["u"] == "Discord":
                post = data["p"].split(":")[1][1:]
                print(post)
                ctx = {
                    "user": data["u"],
                    "post": post,
                    "client": c,
                    "raw_msg": "Not currently supported for Discord",
                    "isdiscord": True
                }
                print(post)
                if post.startswith(tuple(prefixes)):
                    print("start")
                    parsecmd(ctx)
            else:
                ctx = {
                    "user": data["u"],
                    "post": data["p"],
                    "client": c,
                    "raw_msg": data,
                    "isdiscord": False
                }
                print(data["p"])
                if data["p"].startswith(tuple(prefixes)):
                    print("start")
                    parsecmd(ctx)