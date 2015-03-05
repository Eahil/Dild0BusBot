import coco.internals
import conf


class Bot(coco.internals.Manager):
    def _p_ok(self, group):
        group.setNameColor("ff0")
        group.setFontColor("3bf")
        print("Connected to "+group.name)
    def _init(self):
        self.run()

    def _on_Message(self, group, user, msg):
        cmds = ["say", "smd", "<3", "ship", "LOL", "help"]
        post = msg.post
        ret = "%s: %s: %s" % (group.name, user, post)
        print(ret)
        #make sure the bot ignores itself.. 
        if user == group.username:
            return

        if post[0] == ".":
            data = post[1:].split(" ", 1)
            if len(data) > 1:
                cmd, args = data[0], data[1]
            else:
                cmd, args = data[0], ""

        if cmd == cmds[0]:
            if(len(args)) < 1:
                group.post("I can't say nothing -_-\"")
            else:
                group.post(args)

        elif cmd == cmds[1]:
            group.post("Suck My Dick.")
        elif cmd == cmds[2]:
            group.post("*h*+50")
        elif cmd == cmds[3]: 
            if (len(args)) < 2: group.post(args[1] + "x" + args[2])
            else:
                group.post("Shipped...\n")
        #elif cmd == cmds[-1]:
        #    top = 0
        #    end = length(cmds) - 1
        #    for c in cmds:
        #         if cmds.index(c) == end:
             




bot = Bot(conf.groups, conf.name, conf.password)._init()
