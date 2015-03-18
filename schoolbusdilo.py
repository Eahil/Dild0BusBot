import coco.internals
import dildobus


class Bot(coco.internals.Manager):
    def _p_ok(self, group):
        group.setNameColor("ff0")
        group.setFontColor("3bf")
        print("Connected to "+group.name)
        group.post("I am a dildo bus. So suck my tirenuts.")

    def _init(self):
        self.run()

    def _on_Message(self, group, user, msg):
        cmds = ["say", "smd", "<3", "ship", "LOL"]
        switch = "."
        post = msg.post
        ret = "%s: %s: %s" % (group.name, user, post)
        print(ret)
        #make sure the bot ignores itself.. 
        if user == group.username:
            return

        if post[0] == switch:
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
                y = args.split(' ')
                if (len(y)) >= 2: 
                    group.post(y[0] + " x " + y[1])
                else:
                    group.post("Shipped...\n")
            elif cmd == "h" or cmd == "help": 
                group.post(post)
             
             




bot = Bot(dildobus.groups, dildobus.name, dildobus.password)._init()
