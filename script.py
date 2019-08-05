# background code_______________________
class TreeNode:
    def __init__(self, story_element):
        self.story_element = story_element
        self.next_part_of_story = []

    def assign(self, new_story_element):
        self.next_part_of_story.append(new_story_element)

    def traverse(self):
        current_node = self
        print(current_node.story_element)

        while len(current_node.next_part_of_story) > 0:
            choice_index = input("Please enter 1 or 2 to continue the story.")
            valid_choice = [1, 2]

            if int(choice_index) not in valid_choice:
                choice_index = input("Please enter the numbers 1 or 2.")

            if int(choice_index) in valid_choice:
                   chosen_index = int(choice_index)
                   chosen_index -= 1
                   chosen_child = current_node.next_part_of_story[chosen_index]
                   print(chosen_child.story_element)
                   current_node = chosen_child
        while True:
            again = input("Do you want to play this story again? Y/N")
            valid_answers = ["Y","y","N","n"]
            if again not in valid_answers:
                again = input("Please type Y or N.")
            if again == "N" or again == "n":
                print("See you next time!")
                break
            if again == "Y" or again =="y":
                root.traverse()
                break
                   
###### Story elements #########
print("Welcome to the story of Grizzlebeard\'s treasure!")
user_input = input("\n What is your name, explorer?")

root = TreeNode("""
Drawn by the legends of invaluable pirate treasure, you, {x}, the fearless and intrepid explorer, enter into the Cursed Caverns
of the pirate Grizzlebeard. Lighting your torch, you step into the darkness. The ground gives way, and you tumble into a pit!
Looking up, you see the ghost of Grizzlebeard looking back at you. \"What arrr ye doin\' in my cave? Who arrrr ye?\" He moans.
You see a small opening behind him.
Do you:
1 ) Tell the ghost your name
2 ) Run for it!!
""".format(x = user_input))

choice_a = TreeNode("""
\"... {x}, eh? Yer brave to stay and face me! Most run when they see a ghost - right into me pet spider\'s lair. Not left but
bones now, all became supper. I\'ll make ye a deal. If me treasure ye seek, first ye need to do a favor for me. I lost me
eyepatch in the caverns when I fell, and I can\'t rest till I find it. Me mum gave it to me! Do that, and me treasure\'s yers.
What say ye?\"
Do you:
1 ) Tell him you work alone
2 ) Agree to help him
""".format(x = user_input))

choice_b = TreeNode("""
You run headlong down the corridor as Grizzlebeard laughs. Fear overtaking you, you turn the corner of the cavern. Entering a
clearing, you see light in the tunnel above! Then a giant, hideous spider blocks your path. \"I see ye\'ve met me pet! Yer sure
to get along with her.\" Grizzlebeard laughs. You freeze in panic as the monster overtakes you.

YOU BECAME A SPIDER\'S SUPPER.
""")

choice_ab_a = TreeNode("""
Grizzlebeard laughs. \"Arrr, have it yer way, fool.\" He says. A sudden gust blows out your torch as the ghost vanishes, leaving
you alone in the darkness.

YOU WERE LOST IN THE CURSED CAVERNS.
""")

choice_ab_b = TreeNode("""
Grizzlebeard smiles, showing his ghostly yellow teeth. He hands you a piece of paper. The only writing on it is \"RLR\". No sooner
do you take it than the ghost whisks you away! You wake up in a room with two tunnels - one to the left, one to the right.
Do you:
1 ) Take the right tunnel.
2 ) Take the left tunnel.
""")
                       
choice_aba_a = TreeNode("""
You begin to feel disoriented. Did you just walk back into the same room? It is hard to tell if you went anywhere at all.
What looks like the same two tunnels are right in front of you!
Do you:
1 ) This paper is a trap! Go right
2 ) Trust the paper! Time to go left
""")

choice_aba_b = TreeNode("""
The floor collapses under your weight, and you fall into an underground river! It carries you out of the cave.

YOU SURVIVED, BUT YOU DID NOT GET THE TREASURE.
""")

choice_abaa_a = TreeNode("""
So it WAS a trap! You emerge into a giant room, filled with treasure. Gold coins are piled up all around you. In your excitement,
you scramble to gather it up. Fame and glory are soon to be yours!
Something is wrong though. As you touch the treasure, you feel cold. Wispy. Your body fades away until nothing is left but a
skeleton! Grizzlebeard calls from nowhere. \"Ahhh, a new worker! I needed one since my last few fell apart. Get to work, slave,
there\'s much to do!\"

YOU BECAME THE UNDEAD SERVANT OF GRIZZLEBEARD.
""")

choice_abaa_b = TreeNode("""
What? This has to be a trick. You appear to be in the same room again!! You feel yourself growing impatient, and more than a little
nervous. According to the pirate\'s paper, it is time to go right one last time. To your left, however, you see the sunlight off in
the distance.
Do you:
1 ) See this through - go to the right
2 ) I\'ve had enough! Go to the left
""")

choice_abaab_a = TreeNode("""
What? A dead end. That was a waste. Wait... there, on the ground, is a skeleton. Next to it is an eyepatch. You place the eyepatch on
the skeleton, and Grizzlebeard speaks from behind you. \"Arrrr, that feels SO much better! Thankee friend. A promise is a promise. I
remove me curse, and me treasure is all yers.\" You walk back the way you came. But now the tunnel leads to an exit! There, right before
the exit, is a treasure chest filled to the brim with coins and rare jewels. Cheering, you lift up your newfound bounty and walk out
into the open air.

CONGRATULATIONS! THE LEGEND OF {X} WILL BE TOLD FOR YEARS TO COME, AND YOU LIVE THE REST OF YOUR DAYS OUT IN WEALTH AND FAME.
""".format(X=user_input))

choice_abaab_b = TreeNode("""
Finally! You feel the open air against your face, and rush to meet it. Freedom! What a nightmare.
No sooner do you step out than the exit collapses into rubble. Disappointed but glad to be alive, you run to safety.
For years to come, you entertain pub goers with your harrowing adventure, speculating that there was never really any treasure
to begin with. At least, that\'s what you tell yourself to sleep at night.

THE FABLED TREASURE OF GRIZZLEBEARD WAS LOST TO THE MISTS OF TIME.
""")
                       
root.assign(choice_a)
root.assign(choice_b)
choice_a.assign(choice_ab_a)
choice_a.assign(choice_ab_b)
choice_ab_b.assign(choice_aba_a)
choice_ab_b.assign(choice_aba_b)
choice_aba_a.assign(choice_abaa_a)
choice_aba_a.assign(choice_abaa_b)
choice_abaa_b.assign(choice_abaab_a)
choice_abaa_b.assign(choice_abaab_b)

#########

######## Story Time ####

root.traverse()


