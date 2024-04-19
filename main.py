import random

name = input("Please enter a name for your hero: ")
print("Welcome", name, ", to your great adventure! ")

print( name, "  finds themselves at a crossroads in a dense forest."
                      " Ahead, there are three paths diverging into the unknown."
                      " A weathered signpost stands nearby, barely legible but indicating three possible directions:"
                      " OPTION 1 Path of Mystery: A dark, foreboding trail disappearing into the depths of the forest."
                      " OPTION 2 Path of Diplomacy: A winding path leading towards a distant castle, rumored to be the "
                      "seat of a king known for his wisdom and diplomacy. "
                      " OPTION 3 Path of Bravery: A rugged trail ascending into the mountains, where rumors speak of a "
                      "fearsome dragon that has been terrorizing nearby villages.")

answer = input('Your choice awaits - forge your path and discover where fate leads you! Please press 1, 2 or 3: ')

if str(answer) == '1':
    # Path of Mystery
    print(name, "enters the Path of Mystery and ventures deeper into the forest. Three choices await: "
                "OPTION 1 decipher cryptic glyphs for hidden power, OPTION 2 follow a strange creature towards "
                "treasures or peril, or OPTION 3 seek guidance from mystical forest spirits. Each path offers both "
                "promise and peril, shaping", name, "'s destiny in the shadowy depths.")

    answer = input("Step into the shadows! Unveil ancient enigmas (Tap 1), bargain with ethereal beings (Tap 2), "
                   "or pursue elusive entities (Tap 3). Adventure beckons!:  ")

    if str(answer) == '1':
        # Investige the ruins
        outcomes = {1: 'Through meticulous study and deciphering of the ancient glyphs, {} unveils long-forgotten '
                       'knowledge, unlocking the key to defeating the ancient evil. Armed with this newfound wisdom, '
                       '{} embarks on a journey to confront the darkness, ensuring the safety of the realm and '
                       'earning the admiration of all who hear of their triumph.'.format(name, name),
                    2: 'Through a humble offering, {} earns the favor of the ancient entity, quelling its wrath and '
                       'earning its benevolent protection. With the darkness appeased, light returns to the land, '
                       'and peace is restored. {}\'s act of reverence becomes a legend, celebrated for its wisdom and '
                       'humility'.format(name, name),
                    3: 'In their reckless pursuit of answers, {} disturbs the ancient relics, unknowingly unleashing '
                       'a malevolent force upon the land. Chaos reigns as the darkness spreads unchecked, '
                       'consuming all in its path. {}\'s actions serve as a cautionary tale of the dangers of '
                       'meddling with forces beyond mortal comprehension.'.format(name, name),
                    4: 'Ignoring the warnings of ancient prophecies, {} forges ahead, heedless of the peril that '
                       'awaits. Their arrogance leads to dire consequences as the darkness overtakes the land, '
                       'plunging it into an eternal night. {}\'s disregard for the wisdom of the ancients serves as a '
                       'tragic lesson in the importance of heeding the warnings of history.'.format(name, name)}

        res = random.choice(list(outcomes.items()))
        print(res[1])

    elif str(answer) == '2':
        # Follow the strange creature
        outcomes = {1: '{} cautiously approaches the creature, offering it food & gifts as a gesture of goodwill, '
                       'establishing trust and friendship. {} befriends the creature, which guides them to a hidden '
                       'cache of treasures'.format(name, name),
                    2: 'Instead of rushing in, the player watches the creature from a safe distance, patiently '
                       'earning its trust through observation and non-threatening behavior. The creature guides {} '
                       'out of the forest safely'.format(name, name),
                    3: 'With bravado, {} confronts the creature head-on, underestimating its power and ferocity. '
                       'Their reckless actions provoke the creature\'s wrath, leading to a harrowing battle in which '
                       'they emerge battered and defeated. {}\'s failure to approach with caution serves as a harsh '
                       'lesson in the dangers of hubris and the importance of respecting unknown '
                       'adversaries.'.format(name, name),
                    4: 'Driven by curiosity or recklessness, {} blindly follows the creature without caution, '
                       'falling to tragic end into traps laid by its malevolent master.'.format(name)}

        res = random.choice(list(outcomes.items()))
        print(res[1])

    elif str(answer) == '3':
        # Seek Guidance from the Forest Spirits
        outcomes = {1: '{} accepts the challenges presented by the forest spirits  and completes them with integrity. '
                       '{} earns the favor of the forest spirits, receiving blessings that protect from harm & aid '
                       'them in their future endeavors.'.format(name, name),
                    2: 'Recognizing the importance of the forest spirits, {} offers prayers or offerings as a sign of '
                       'respect, earning their favor and blessings in return.'.format(name),
                    3: "{} approaches the trials with arrogance & overconfidence, underestimating the challenges and "
                       "failing to respect the spirits' power, leading to their displeasure. {} is cursed with "
                       "misfortune forever".format(name, name),
                    4: 'Ignoring the traditions and customs of the forest spirits, {} acts impulsively & '
                       'disrespectfully during the trials, angering the spirits and inviting their wrath. {} is sent '
                       'on a perilous quest as penance, leading to lasting hardship & danger. '.format(name, name)}

        res = random.choice(list(outcomes.items()))
        print(res[1])
    else:
        print('This was not a valid option.', name, 'has lost out on their great adventure')

elif str(answer) == '2':
    # Path of Diplomacy
    print(name, "chooses the Path of Diplomacy!", name,
          "journeys towards the castle, where they are welcomed by the king's courtiers. Through eloquent speech and shrewd negotiation,",
          name, "gains the trust of the king.", name,
          "offers the King assistance services with the following. OPTION 1 Negotiate with Rival Nobles. OPTION 2 Investigate a Conspiracy. OPTION 3 Diplomatic Marriage Proposal.")
    answer = input("Embrace the art of diplomacy! Seek harmony (Press 1), unravel political schemes (Press 2), "
                   "or secure powerful alliances (Press 3). Your choices will shape the destiny of nations: ")

    if str(answer) == '1':
        # Negotiate with Rival Nobles
        print(name, 'decides to mediate between rival noble families vying for power.')

        outcomes = {1: '{} acts as a fair and impartial mediator, listening to the concerns of both factions and '
                       'proposing compromises that benefit all parties involved; bringing stability to the kingdom and '
                       'gaining political influence and recognition.'.format(name),
                    2: 'Recognizing shared interests, {} identifies areas of common ground between the rival nobles and '
                       'facilitates negotiations that lead to a mutually beneficial agreement; bringing stability to the '
                       'kingdom and gaining political influence and recognition.'.format(name),
                    3: '{} shows favoritism towards one faction over the other, alienating the opposing side and '
                       'sabotaging the chances of reaching a peaceful resolution.'.format(name),
                    4: 'Instead of seeking compromise, {} imposes unreasonable demands on one or both factions, '
                       'leading to resentment and hostility that derail the negotiations.'.format(name)}

        res = random.choice(list(outcomes.items()))
        print(res[1])

    elif str(answer) == '2':
        # Investigate a Conspiracy
        print(name, "discovers whispers of a conspiracy threatening the kingdom's stability.", name,
              "embarks on a covert investigation, gathering evidence and uncovering plots.")

        outcomes = {
            1: '{} gathers evidence discreetly, employing stealth and subtlety to avoid detection and uncover the '
               'truth without alerting the conspirators. {} exposes the conspiracy and earns the king\'s trust '
               'and gratitude, gaining valuable rewards and securing their position in the kingdom.'.format(name,
                                                                                                            name),
            2: 'Recognizing the need for support, {} forms alliances with trusted allies who assist in the '
               'investigation, pooling resources and expertise to unravel the conspiracy. {} exposes the '
               'conspiracy and earns the king\'s trust and gratitude, gaining valuable rewards and securing their '
               'position in the kingdom.'.format(name, name),
            3: '{} confronts the suspects openly, drawing attention to their investigation and alerting the '
               'conspirators, who retaliate by silencing {} to a permanent end.'.format(name, name),
            4: 'Misjudging allies, {} inadvertently shares sensitive information with a traitor who betrays '
               'them, sabotaging the investigation. The suspects retaliate by silencing {} to a permanent '
               'end'.format(name, name)}

        res = random.choice(list(outcomes.items()))
        print(res[1])

    elif str(answer) == '3':
        # Diplomatic Marriage Proposal
        print(name, 'receives a proposal for a diplomatic marriage alliance from a neighboring kingdom. The marriage  '
                    'impacts the kingdom\'s relations with the neighboring realm and its internal politics.')

        outcomes = {1: '{} negotiates fair and mutually beneficial terms for the marriage alliance, addressing the '
                       'concerns and interests of both kingdoms involved; thus strengthening the kingdom\'s position '
                       'and securing valuable support, resources, and alliances.'.format(name),
                    2: 'Prioritizing trust and cooperation, {} invests time and effort in building rapport with the '
                       'potential spouse and their kingdom, fostering goodwill and ensuring a successful '
                       'alliance'.format(name),
                    3: '{} demands unreasonable conditions or concessions from the potential spouse or their kingdom, '
                       'souring relations and leading to the rejection of the proposal. {} faces retaliation from the '
                       'neighbouring kingdom and all out war breaks out'.format(name, name),
                    4: 'Through careless words or actions, {} insults or offends the potential spouse or their '
                       'kingdom, leading to the rejection of the proposal. The neighboring kindom forms an alliance '
                       'with the rival faction and their threat looms over the kingdom'.format(name)}

        res = random.choice(list(outcomes.items()))
        print(res[1])

    else:
        print('This was not a valid option.', name, 'has lost out on their great adventure')

elif str(answer) == '3':
    # Path of bravery
    print(name, "embarks on a courageous journey on the Path of Bravery, where heroes rise to face the ultimate "
                "challenge. Presented with three pivotal choices,",
          name, "navigates the perilous path ahead. OPTION 1 Recruit Allies OPTION 2 Search for Legendary Weapons "
                "OPTION 3 Confront the Dragon's Minions. Choose wisely, for in the realm of bravery, every decision "
                "shapes the destiny of heroes.")

    answer = input("Embark on a journey of courage! Unite fearless allies (Tap 1), seek legendary artifacts (Tap 2), "
                   "or confront the dragon's minions (Tap 3). Your bravery will become the stuff of legends!: ")

    if str(answer) == '1':
        # Recruit Allies
        print(name, "seeks out brave adventurers, skilled warriors, and wise scholars to aid them in their quest.They "
                    "must convince potential allies to join their cause through persuasion, intimidation, "
                    "or diplomacy.")

        outcomes = {1: '{} appeals to potential allies\' sense of honor and duty, emphasizing the importance of their '
                       'cause and the need for unity in facing the dragon\'s threat. Together they journey to the '
                       'mountain peak where they confront the legendary dragon in its lair. A fierce battle ensues, '
                       'with {} displaying unmatched courage and skill. Eentually, they emerge victorious, '
                       'having slain the dragon and saved the villages from its wrath. Grateful villagers shower {} '
                       'with rewards, including treasures from the dragon\'s hoard and the title of the realm\'s '
                       'greatest hero.'.format(name, name, name),
                    2: '{} offers rewards or incentives to potential allies enticing them to join the cause. {} '
                       'recruits a formidable band of allies who prove instrumental in defeating the dragon, '
                       'earning the admiration and loyalty of their companions. Grateful villagers shower {} with '
                       'rewards, including treasures from the dragon\'s hoard and the title of the realm\'s greatest '
                       'hero.'.format(name, name, name),
                    3: 'Potential allies are unconvinced of the dragon\'s threat or {}\'s ability to defeat it, '
                       'dismissing {}\'s pleas for assistance. Without the support of a united front, {}\'s journey '
                       'leads to a harrowing confrontation with the dragon. Overwhelmed and outnumbered, '
                       '{} faces defeat, succumbing to the dragon\'s might in a valiant but tragic last '
                       'stand.'.format(name, name, name, name),
                    4: '{}\'s words or actions inadvertently alienate potential allies, causing them to refuse aid or '
                       'even turn against {}, viewing them as a liability rather than a leader. Without the support '
                       'of a united front, {}\'s journey leads to a harrowing confrontation with the dragon. '
                       'Overwhelmed and outnumbered, {} faces defeat, succumbing to the dragon\'s might in a valiant '
                       'but tragic last stand.'.format(name, name, name, name)}

        res = random.choice(list(outcomes.items()))
        print(res[1])

    elif str(answer) == '2':
        # Search for Legendary Weapons
        print(name, "hears rumors of legendary weapons capable of slaying dragons scattered across the land.They "
                    "embark on a quest to find these weapons, facing challenges and trials along the way.")

        outcomes = {1: '{} diligently researches ancient texts and lore, uncovering clues that lead them to the '
                       'location of the legendary weapons and how to obtain them. Armed with these legendary weapons, '
                       '{} faces the dragon with newfound courage and resolve, ultimately emerging victorious and '
                       'earning fame and renown throughout the land.'.format(name, name),
                    2: 'Through acts of bravery and selflessness, {} earns the favor of the guardians or protectors '
                       'of the legendary weapons, gaining their assistance in obtaining them. Armed with these '
                       'legendary weapons, {} faces the dragon with newfound courage and resolve, ultimately emerging '
                       'victorious and earning fame and renown throughout the land.'.format(name, name),
                    3: 'Misinterpreting the clues or ancient texts, {} searches in the wrong locations & follows '
                       'false leads, wasting valuable time and resources. As they confront the dragon empty-handed, '
                       'their chances of survival diminish. Despite their bravery, {}\'s journey ends tragically as '
                       'they succumb to the might of the dragon, leaving behind a legacy of valor but ultimately '
                       'meeting their demise.'.format(name, name),
                    4: 'In their pursuit of the legendary weapons, {} braves formidable trials of valor. Despite '
                       'their courage, the challenges prove insurmountable, leading to their demise before they can '
                       'claim the coveted artifacts. Their sacrifice echoes through the ages as a testament to their '
                       'bravery, but ultimately, they fail in their quest to confront the dragon.'.format(name)}

        res = random.choice(list(outcomes.items()))
        print(res[1])

    elif str(answer) == '3':
        #
        print(name, "decides to weaken the dragon's forces by targeting its minions first.", name, "undertakes missions to disrupt the dragon's operations, sabotage its lair, and weaken its allies.")

        outcomes = {1: 'In uniting local villages and resistance groups, {} weakens the dragon\'s minions. With '
                       'newfound allies, they confront the dragon and emerge victorious, freeing the land from '
                       'tyranny.'.format(name),
                    2: 'In their mission to gather intelligence, {} infiltrates the dragon\'s minions, extracting '
                       'crucial information to weaken the enemy. With this intelligence, they lead a strategic '
                       'assault against the dragon, exploiting its vulnerabilities and ultimately defeating it, '
                       'securing victory for their cause and freeing the land from its reign of terror.'.format(name),
                    3: 'In their attempt to overextend forces, {}\'s armies suffer heavy losses, leaving their '
                       'territory vulnerable to the dragon\'s counterattacks. {}\'s weakened position only emboldens '
                       'the dragon, leading to a devastating defeat that plunges the land deeper into chaos and '
                       'despair.'.format(name, name),
                    4: 'Underestimating the strength of the dragon\'s minions, {}\'s forces are caught off guard and '
                       'suffer heavy losses, emboldening the dragon and strengthening its resolve, leading to a '
                       'devastating defeat that plunges the land deeper into chaos and despair.'.format(name)}

        res = random.choice(list(outcomes.items()))
        print(res[1])
    else:
        print('This was not a valid option.', name, 'has lost out on their great adventure')
else:
    print('This was not a valid option.', name, 'has lost out on their great adventure')
