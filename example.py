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
		post = msg.post
		ret = "%s: %s: %s" % (group.name, user, post)
		print(ret)
		#make sure the bot ignores itself.. 
		if user == group.username:
			return

		if post[0] == ".":
			data = body[1:].split(" ", 1)
			if len(data) > 1:
				cmd, args = data[0], data[1]
			else:
				cmd, args = data[0], ""

			if cmd == "say":
				if(len(args)) < 1:
					group.post("I can't say nothing -_-\"")
				else:
					group.post(args)




bot = Bot(conf.groups, conf.name, conf.password)._init()
