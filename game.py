#!/usr/bin/env python3
# Game Title: Realm of Eldoria
# Story Author: Elijah Cannon
# Created By: Elijah Cannon

import sys
import getopt

narratives = {
    "0": "\nYou are Eric, a fearless warrior in the fantasy realm of Eldoria. You have been chosen to embark on a perilous quest to find the legendary Enchanted Amulet, a powerful artifact that can restore peace to the war-torn land. Your fate and the future of Eldoria lie in your hands. Choose your path wisely!\n",
    "1": "As you set foot on the treacherous path, you encounter a wounded traveler seeking help. They appear to have been attacked by bandits. What do you do?",
    "2": "You try to save the man’s life, but after 1 day and 1 night of work, he dies in your arms. You notice clenched tightly in his fist is a magnificent key. Do you take it?",
    "3": "After getting a good night’s sleep, you continue on your journey. As you enter the city you find a group of bandits harassing the locals in the marketplace. What action do you take?",
    "4": "You take a close look at the key and notice a chest hidden in the back room of the dead man’s house. So that's the family treasure he was protecting from the bandits he was talking about. You open it up and find a dragon egg. You know it’s of great value and want to buy better equipment for your adventure. Do you keep it or sell it?",
    "6": "You feel an incredible attachment to the ancient monster sleeping in the egg. And apparently so did he, because as soon as you pick it up it starts to glow,  and hatches. It becomes immediately attached to you and your love and care for it will help it grow to be big strong.",
    "7": "As you pick up the dragon egg, it begins to glow. You immediately start thinking about how much money you can make from selling it. You use your smarts combined with your business experience to gain an audience with several of the kingdom’s most capable buyers. The auction runs smoothly and you end up with pile of gold and set of the best armor money can buy.",
    "8": "You fight against the bandits to become a hero to the people. Several of them go down before a slash to your leg brings you to your knees. The bandits’ hearts fill with joy as they see victory is near. You continue to put up a fight but to no avail. Your story ends here.",
    "8.6": "You try and protect the people by standing up to the bandits. They weren’t scared of you at first because there were so many of them and only one of you, but after killing a few of them they took a hint and ran away. However, because of your inexperience, you ended up getting hurt pretty badly. You laid down to take a short rest when you realized you weren’t going to make it. Just then, the pet dragon you got came to lick your wounds. Its magical properties instantly healed you and you were left feeling a great sense of appreciation for your new friend. Among the defeated bandits",
    "8.7": "You decide to protect the good people of the capital. As you began to contend with the bandits they were scared because of the armor you were wearing and ran away. The locals were so happy for saving them that they threw you a grand party with lots of amazing food, drinks and pretty girls. Word spread through the capital and you receive a royal invitation from the King who wants to receive you. On your way to the Castle you meet a young witch who says she can grant you powers but mustn’t go to see the king. Where do you go?",
    "9": "You enter the Bandit’s camp at night and locate the tent of the Leader. As you approached his bed you noticed on the table a map revealing the location of the Enchanted Amulet. What do you do?",
    "10": "You find a hidden map revealing the location of the Enchanted Amulet. What do you do?",
    "11": "While following the map, you stumble upon a mystical forest. How do you proceed?",
    "12": "Sorry, you wasted your time. The village elder doesn’t know anything helpful, but tells you the old stories of legend which you already knew. You are paranoid someone followed you after leaving the village to steal the map. Do you fall asleep?",
    "13": "The king is actually the one who hired the bandits and wants to punish you for thwarting his plans. You get locked up in prison and rot. Your story ends here.",
    "14": "The young witch turns out to be very friendly (and hot) and tells you of your unlimited potential for magic. She helps you envision where the enchanted amulet is and tells you that if you bring it to her, she promises to grant you unlimited powers.",
    "15": "You plunge a dagger into the heart of the Bandit leader to become a hero. He lets out a yelp and as you exited the camp you are swarmed by other bandits. Several of them go down before a slash to your leg brings you to your knees. The bandits’ hearts fill with joy as they see victory is near. You continue to put up a fight but to no avail. Your story ends here.",
    "15.6": "You plunge a dagger into the heart of the Bandit leader to become a hero. He lets out a yelp and as you exited the camp you are swarmed by other bandits. Several of them go down before a slash to your leg brings you to your knees. The bandits’ hearts fill with joy as they see victory is near. You continue to put up a fight but to no avail. Your dragon is captured and your story ends here.",
    "15.7": "You plunge a dagger into the heart of the Bandit leader to become a hero. He lets out a yelp and as you exited the camp you are swarmed by other bandits. Several of them go down before a slash to your leg brings you to your knees. The bandits’ hearts fill with joy as they see victory is near. You continue to put up a fight but to no avail. Your armor is stripped from your body and they plunge a spear through your heart. Your story ends here.",
    "16": "You take the map and quietly leave as fast as you can. They’ll never catch you. Is this really the enchanted amulet from the legends? What do you do?",
    "17": "Within the mystical forest, you encounter a wise old hermit who promises to aid you in your quest. What do you do?",
    "18": "On the outskirts of the forest, you encounter a group of trolls blocking your way. How do you handle the situation?",
    "19": "The hermit grants you the ability to fly and tells you you are destined for greatness.",
    "20": "The hermit tell you you are destined for failure and shrinks back into his shell.",
    "21": "After overcoming the trolls, you reach a treacherous mountain pass. What approach do you take?",
    "22": "While traversing the mountain pass, a snowstorm engulfs you. What do you do?",
    "23": "You stumble upon an ancient temple buried deep within the mountains. How do you proceed?",
    "24": "You end up freezing to death in the snow. Your story ends here.",
    "24.6": "The magic of your dragon keeps you warm enough to survive and make it through the storm.",
    "26": "Inside the temple, you encounter a guardian who challenges your worthiness. What action do you take?",
    "27": "You successfully pass the trial and the guardian reveals the location of the Enchanted Amulet. What do you do next?",
    "28": "As you approach the amulet's location, you find a group of mercenaries guarding it. How do you proceed?",
    "29": "When you wake up from a long sleep, you are lost in the temple deep beneath the mountains. You are forever unable to find the exit and fail to escape the temple prison.",
    "29.6": "When you wake up from a long sleep, you are lost in the temple deep beneath the mountains. Though you are lost, your dragon seems to remember the way out. Be happy your friend saved you again. ",
    "29.14": "When you wake up from a long sleep, you are lost in the temple deep beneath the mountains. You recall the beauty of the young witch who sent you on this journey and suddenly remember which way you must go to get to the enchanted amulet.",
    "30": "After a hard battle, you emerge victorious.",
    "31": "The mercenaries don't let you pass so you beat them up.",
    "31.7": "The mercenaries agree to let you buy their service with the set of armor you are wearing.",
    "31.19": "They still won't let you pass so you simply fly over them.",
    "31.37": "The mercenaries don’t let you pass so and you are exhausted from your journey so you give up. Better luck next time.",
    "32": "You successfully retrieve the Enchanted Amulet, but a powerful sorcerer appears, demanding its surrender. How do you respond?",
    "33": "You feel the power of the amulet surging through your veins. Once again because of you amazing adventurer skills you emerge victorious. After defeating the sorcerer, you now possess the Enchanted Amulet. What is your next course of action?",
    "34": "The sorcerer agrees to a magical race in which the winner gets the amulet. It’s a flying race. You do net yet have the ability to fly, so you concede and give up the amulet.",
    "34.6": "You agree and let your dragon take your place in the race. He wins and you are so proud of him. The powerful sorcerer agrees to leave you alone. What is your next course of action? ",
    "34.19": "The sorcerer agrees to a magical race in which the winner gets the amulet. It’s a flying race. You fly with ease and take the win by a long shot. The powerful sorcerer agrees to leave you alone. What is your next course of action?",
    "35": "To Be Continued...",
    "36": "You get a good night’s rest and feel refreshed for your journey ahead.",
    "37": "You stay up all night gripping the map because you are scared the village elder or bandits sent someone to follow you and take it for themselves. When morning comes you are depleted of energy and your journey ahead becomes more difficult.",
    "38": "You return to the capital and enter the King’s Castle.  Turns out, the King was the one who hired the Bandits to retrieve the enchanted amulet. When he hears you brought it to him, he rejoices and offers you half of his kingdom in exchange for the amulet. Do you accept?",
    "39": "You return to the house of the young witch, victorious from your long journey. She builds a magical rig to help you harness the power of the amulet. She falls in love with you and asks you to make her yours. Your goodness combined with her love makes your power infinitely stronger. Will you marry her?",
    "40": "You give the enchanted amulet to the king in exchange for half of his kingdom. Now you are the second most powerful person in all of the land. The end.",
    "41": "Why would you accept such terms when you are already the most powerful man in the kingdom. You overthrow the kingdom and become a ruler with the power to stop anyone who goes against you. You get all the food, wine, and girls you could ever want - except for the young witch who will forever despise you for succumbing to corruptness.",
    "42": "You beat them up and they give you all their money.",
    "43": "They are happy to grant you passage after trading some health potions.",
    "44": "You encounter a booby trap and get hurled off the mountain. Your story ends here.",
    "44.19": "You encounter a booby trap and get hurled off the mountain. Luckily, your new ability to fly saves your life. You continue to enter the temple carefully.",
    "45": "You fight a mighty battle against the guardian. It lasts a long time and you begin to grow tired. That’s when you realized the guardian has the uncanny ability to heal. You try to retreat but you are trapped. You are unable to find any sort of weakness in your opponent and end up getting yourself killed. Good job.",
    "46": "You marry the lovely witch Rosalina who loves to go on adventures with you. Together, you will keep the land safe from harm, continue to innovate, and bring good for generations to come. The end.",
    "47": "You decide that you don't need love. You will never reach your full potential. The End."
}

decisions = [
    {"path_from": "0", "path_to": 1, "decision": ""},
    {"path_from": "1", "path_to": 2, "decision": "Offer your assistance."},
    {"path_from": "1", "path_to": 3,
        "decision": "Ignore the traveler and continue on your journey."},
    {"path_from": "2", "path_to": 4, "decision": "Yes"},
    {"path_from": "2", "path_to": 3, "decision": "No"},
    {"path_from": "4", "path_to": 6, "decision": "Keep"},
    {"path_from": "4", "path_to": 7, "decision": "Sell"},
    {"path_from": "6", "path_to": 3, "decision": ""},
    {"path_from": "7", "path_to": 3, "decision": ""},
    {"path_from": "3", "path_to": 8,
        "decision": "Engage the bandits in combat to teach them a lesson"},
    {"path_from": "3", "path_to": 9,
        "decision": "Follow them and sneak into their camp at night"},
    {"path_from": "8", "path_to": -1, "decision": ""},
    {"path_from": "8.6", "path_to": 10, "decision": ""},
    {"path_from": "8.7", "path_to": 13, "decision": "The King’s Castle"},
    {"path_from": "8.7", "path_to": 14, "decision": "The Witch’s lair"},
    {"path_from": "10", "path_to": 11, "decision": "Follow the map's directions."},
    {"path_from": "10", "path_to": 12,
        "decision": "Seek guidance from the village elder"},
    {"path_from": "13", "path_to": -1, "decision": ""},
    {"path_from": "14", "path_to": 11,
        "decision": "You follow the vision because you are drawn to the magic of the amulet."},
    {"path_from": "14", "path_to": 11,
        "decision": "You follow the vision because you are drawn to the beauty of the witch."},
    {"path_from": "9", "path_to": 15, "decision": "Assassinate the leader"},
    {"path_from": "9", "path_to": 16, "decision": "Take the map"},
    {"path_from": "15", "path_to": -1, "decision": ""},
    {"path_from": "15.6", "path_to": -1, "decision": ""},
    {"path_from": "15.7", "path_to": -1, "decision": ""},
    {"path_from": "16", "path_to": 11, "decision": "Follow the map's directions."},
    {"path_from": "16", "path_to": 12,
        "decision": "Seek guidance from the village elder."},
    {"path_from": "11", "path_to": 17, "decision": "Venture into the forest."},
    {"path_from": "11", "path_to": 18,
        "decision": "Go around the forest to avoid any potential danger."},
    {"path_from": "12", "path_to": 36, "decision": "Yes"},
    {"path_from": "12", "path_to": 37, "decision": "No"},
    {"path_from": "36", "path_to": 11, "decision": ""},
    {"path_from": "37", "path_to": 11, "decision": ""},
    {"path_from": "19", "path_to": 18, "decision": ""},
    {"path_from": "20", "path_to": 18, "decision": ""},
    {"path_from": "17", "path_to": 19, "decision": "Accept the hermit's guidance"},
    {"path_from": "17", "path_to": 20,
        "decision": "Decline the hermit's help and trust your own instincts"},
    {"path_from": "18", "path_to": 42, "decision": "Engage the trolls in combat."},
    {"path_from": "18", "path_to": 43,
        "decision": "Try to negotiate a peaceful passage."},
    {"path_from": "42", "path_to": 21, "decision": ""},
    {"path_from": "43", "path_to": 21, "decision": ""},
    {"path_from": "21", "path_to": 22, "decision": "Brave the mountain pass."},
    {"path_from": "21", "path_to": 23, "decision": "Look for an alternate route."},
    {"path_from": "22", "path_to": 23, "decision": "Seek shelter in a nearby cave."},
    {"path_from": "22", "path_to": 24, "decision": "Press on through the storm."},
    {"path_from": "23", "path_to": 26, "decision": "Enter the temple cautiously."},
    {"path_from": "23", "path_to": 44,
        "decision": "Search the perimeter for clues before entering."},
    {"path_from": "44", "path_to": -1, "decision": ""},
    {"path_from": "44.19", "path_to": 26, "decision": ""},
    {"path_from": "24", "path_to": -1, "decision": ""},
    {"path_from": "24.6", "path_to": 28, "decision": ""},
    {"path_from": "26", "path_to": 45, "decision": "Engage the guardian in combat."},
    {"path_from": "26", "path_to": 27,
        "decision": "Attempt to prove your worth through a trial."},
    {"path_from": "45", "path_to": -1, "decision": ""},
    {"path_from": "27", "path_to": 28,
        "decision": "Proceed to the amulet's location."},
    {"path_from": "27", "path_to": 29,
        "decision": "Rest and regain your strength before continuing."},
    {"path_from": "29", "path_to": -1, "decision": ""},
    {"path_from": "29.6", "path_to": 28, "decision": ""},
    {"path_from": "29.14", "path_to": 28, "decision": ""},
    {"path_from": "28", "path_to": 30,
        "decision": "Launch a surprise attack on the mercenaries."},
    {"path_from": "28", "path_to": 31,
        "decision": "Seek a peaceful resolution with the mercenaries."},
    {"path_from": "30", "path_to": 32, "decision": ""},
    {"path_from": "31", "path_to": 32, "decision": ""},
    {"path_from": "31.7", "path_to": 32, "decision": ""},
    {"path_from": "31.19", "path_to": 32, "decision": ""},
    {"path_from": "32", "path_to": 33,
        "decision": "Engage the sorcerer in a magical duel."},
    {"path_from": "32", "path_to": 34,
        "decision": "Offer a peaceful negotiation and propose an alternative solution."},
    {"path_from": "34", "path_to": -1, "decision": ""},
    {"path_from": "34.6", "path_to": 38,
        "decision": "Return to Eldoria and present the amulet to the King."},
    {"path_from": "34.6", "path_to": 39,
        "decision": "Bring the amulet to the young witch."},
    {"path_from": "34.19", "path_to": 38,
        "decision": "Return to Eldoria and present the amulet to the King."},
    {"path_from": "34.19", "path_to": 39,
        "decision": "Bring the amulet to the young witch."},
    {"path_from": "33", "path_to": 38,
        "decision": "Return to Eldoria and present the amulet to the King."},
    {"path_from": "33", "path_to": 39,
        "decision": "Bring the amulet to the young witch."},
    {"path_from": "38", "path_to": 40, "decision": "Yes"},
    {"path_from": "38", "path_to": 41, "decision": "No"},
    {"path_from": "39", "path_to": 46, "decision": "Yes"},
    {"path_from": "39", "path_to": 47, "decision": "No"},
    {"path_from": "40", "path_to": -1, "decision": ""},
    {"path_from": "41", "path_to": -1, "decision": ""},
    {"path_from": "46", "path_to": -1, "decision": ""},
    {"path_from": "47", "path_to": -1, "decision": ""},
]


def get_step(step):
    match step:
        case 8:
            if (6 in path):
                return "8.6"
            if (7 in path):
                return "8.7"
        case 15:
            if (6 in path):
                return "15.6"
            if (7 in path):
                return "15.7"
        case 24:
            if (6 in path):
                return "24.6"
        case 29:
            if (14 in path):
                return "29.14"
            if (6 in path):
                return "29.6"
        case 31:
            if (19 in path):
                return "31.19"
            if (7 in path):
                return "31.7"
            if (37 in path):
                return "31.37"
        case 34:
            if (19 in path):
                return "34.19"
            if (6 in path):
                return "34.6"
        case 44:
            if (19 in path):
                return "44.19"
    return str(step)


path = []
step = 0
inputfile = "save_file.txt"
outputfile = "save_file.txt"
loading = False


def load_progress():
    global inputfile
    global step
    with open(inputfile, 'r') as reader:
        count = 0
        for line in reader:
            num = int(line.strip())
            if (count == 0):
                step = num
            else:
                path.append(num)
            count += 1
    print(f'Progress Loaded! Step: {step}, Path: {path}\n')


def save_progress():
    global outputfile
    global step
    with open(outputfile, 'w') as writer:
        writer.write(str(step)+"\n")
        for x in path:
            writer.write(str(x)+"\n")


def goto(nextStep):
    global step
    path.append(step)
    step = nextStep
    save_progress()


def get_choices(situation):
    mylist = []
    for x in decisions:
        if (x.get("path_from") == situation):
            mylist.append(x)
    return mylist


def main(argv):
    global inputfile
    global outputfile
    global step
    global loading
    opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    for opt, arg in opts:
        if opt == '-h':
            print('game.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            loading = True
            inputf = arg
            if (len(inputf) > 0):
                inputfile = inputf
            load_progress()
        elif opt in ("-o", "--ofile"):
            outputf = arg
            if (len(outputf) > 0):
                outputfile = outputf

    while True:
        while (step != -1):
            situation = get_step(step)
            choices = get_choices(situation)
            print(narratives.get(situation))
            valid = False
            while (not valid):
                if (len(choices) > 1):
                    for x in range(1, len(choices)+1):
                        print(f'{x}. {choices[x-1].get("decision")}')
                else:
                    if (len(choices) > 0):
                        goto(choices[0].get("path_to"))
                        valid = True
                    else:
                        print(
                            "There is a hole in the story. Please contact the author.")
                        exit(1)
                answer = input().strip()
                for x in range(1, len(choices)+1):
                    if (answer == f'{x}'):
                        goto(choices[x-1].get("path_to"))
                        valid = True
                if (not valid):
                    print("Input not valid. Enter a number to choose your path.")

        again = input("Game Over. Retry? (y/n) ")
        if (again == "n" or again == "no"):
            break
        else:
            step = 1
            path = [0]
    exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
