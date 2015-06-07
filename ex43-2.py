from sys import exit

#from random import randint ##artefactual - delete?

#scene#location = 1 ## scene->, scene -> envfeatures
life = 1 ## in Engine->init_self (extraneous function?)
detail = 0 ##
description = 1 ## scene, engine->?
description2 = 1 ## scene, engine ->?
action_des = "you do a thing - global" ##
action = 0 ##
commands = ['look', 'enter'] ##
inventory = [] ##engine get_user_command
enviroment = [] ##scene->envfeatures used
ccdetail = 0
lwadetail = 0
bdetail = 0
ccenviroment = ['armory', 'escape', 'bridge'] ##scene->envfeatures
epenviroment = ['corridor'] ##scene->envfeatures
benviroment = ['corridor']##scene->envfeatures
lwaenviroment = ['corridor']##scene->envfeatures

class Scene(object):
###variables
#location = 1 ##do with an init - delete?
	enviroment = []
	description = "loaded from an instance of scene class"
	description2 = "loaded from within an intance of scene class"

	def __init__(self, location):
		self.location = location
		#why like this?

	def enter(self):
		print "unconfigured instance of a scene."
		exit(1)

	def enviroment_features(location):
		global enviroment
		#bad form?
		if location == 1:
			enviroment = ccenviroment
		elif location == 2:
			enviroment = lwaenviroment
		elif location == 3:
			enviroment = benviroment
		elif location == 4:
			enviroment = epenviroment
			##assign enviroment to global?

#not worth the trouble?
	def describe(detail, room):
		if detail == 0:
			print description
		if detail == 1:
			print description2
		#if detail = 2:
			#print description3
		##neccesary for good practice?#else:
			#pass



class Engine(object):
    action = ""

    def __init__(self):
        #borrowed from teacher ex - what does this do?
        print "Some bad shit went down.  Aliens are all over this fucker.  Watch out."
        self.location = a_place.location



    def get_user_command(self):
        global inventory
        command1 = raw_input("What will you do?")
        if command1 in commands:
            verb = command1
            command2 = raw_input("What will you %s with?" % verb)##escape and replace with verb
            if (command2 in inventory):
                tool = command2
                command3 = raw_input("What will you %s the %s toward?" % verb, tool)
                if command3 in enviroment:
                    action = command1 + " " + command2 + " " + command3
                    action_des = "You try to %s the %s with the %s" % command1, command3, command2
                    return (action, action_des)
            elif command2 in enviroment:
                action = command1 + " " + command2
                action_des = "You try to %s the %s" % command1, command2
                return (action, action_des)
            else:
                print "What?"
        elif command1 == 'help':
			print "Inventory: " + str(inventory) + ", Commands: " + str(commands) + ", Enviroment: " + str(enviroment)
        else:
            """What?  Type 'help' for a list of commands, your inventory, and a list of things in the enviroment you have discovered.  Enter one of the command words for a prompt for another word to use with it."""

    def perform_action(action):
        if self.location == 1:
            a_cc = Central_Corridor()
            a_cc.ccinteraction(action)
        if self.location == 2:
            LaserWeaponArmory.lwainteraction(action)
        if self.location == 3:
            TheBridge.binteraction(action)
        if self.location == 4:
            EscapePod.epinteraction(action)




####
	#def enviroment:


	#def inventory:



class Death(Scene):

	def enter(self):
		print "you die."
		exit(1)

class CentralCorridor(Scene):



	def __init__(self):
		description = """You find yourself in a long corridor, to which several rooms are arrached - the **Bridge**, the lazer weapon **Armory**, and the ship's **Escape Pod**.  A strange pink substance is at your feet - you're not sure you even want to take a careful **Look** at it."""
		description2 = """You find yourself in a long corridor, to which several rooms are arrached - the **Bridge**, the **Lazer Weapon Armory**, and the ship's escape **Pod**.  Alien blood has pooled at your feet.  You can see a set of what you think may be footsteps."""
		location = 1
		describe(ccdetail, location)
		#ccnative = ['Armory', 'Bridge', 'Escape']
		#enviroment = ccnative + ccdiscovered
		##add and preserve discovered enviromental items - this wont work
		print description

	def ccinteraction(self, input):
		if input == "enter armory":
			Laser_Weapon_Armory.enter()
		if input == "enter bridge":
			TheBridge.enter()
		if input == "enter pod":
			EscapePod.enter()

class LaserWeaponArmory(Scene):

	def enter(self):
		description = """Gleaming lazer rifles and pistols line the walls.  You feel a confident stirring in your loins."""
		description2 = "##?"
		location = 2
		describe(lwadetail, location)

	def lwainteraction(input):
		if input == "enter corridor":
			CentralCorridor.enter()

class TheBridge(Scene):

	def enter(self):
		description = """You are in a dark room, which is lit intermitently by sparks of electricity from a huge cable collapsed from the ceiling."""
		description2 = "##?"
		location = 3
		describe(bdetail, location)

	def binteraction(input):
		if input == "enter corridor":
			CentralCorridor.enter()

class EscapePod(Scene):

	def enter(self):
		description = """description 4"""
		location = 4
		describe(epdetail, location)

	def epinteraction(input):
		if input == "enter corridor":
			CentralCorridor.enter()


#from the teacher sug#a_map = Map('central corridor')
#a_game = Engine(a_map)
#a_game.play()

####class initializations#######

#instance of scene class - replace w lower level call
a_place = Scene(1)
#instance of Engine class
a_game = Engine()

while life == 1:
	a_game.get_user_command()
	print action_des ##make this do something
	a_game.perfrom_action(action)
Death.enter()

#a_game.play()
