import random


class Hero:
    # We want our hero to have a default "starting_health",
    # so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
            abilities: List
            armors: List
            name: String
            starting_health: Integer
            current_health: Integer
        '''

        # abilities and armors don't have starting values,
        # and are set to empty lists on initialization
        self.abilities = list()
        self.armors = list()

        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is
        # always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
        self.status = "Alive"

    def add_ability(self, ability):
        ''' Add ability to abilities list '''

        # We used the append method to add strings to a list
        # in the Rainbow Checklist tutorial. This time,
        # we're not adding strings, instead we'll add ability objects.
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths'''
        self.deaths += num_deaths

    def attack(self):
        # start our total out at 0
        total_damage = 0
        # loop through all of our hero's abilities
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()
        # return the total damage
        return total_damage

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        # TODO: Create a method that updates self.current_health to the current
        # minus the the amount returned from calling self.defend(damage).
        defense = self.defend()
        self.current_health -= damage - defense

    def is_alive(self):
        '''Return True or False depending on whether the hero is alive or not. '''
    # TODO: Check the current_health of the hero.
    # if it is <= 0, then return False. Otherwise, they still have health
    # and are therefore alive, so return True
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        ''' Current Hero will take turns fighting the opponent hero passed in.'''
        fighting = True
        while fighting == True:
            if self.abilities == None:
                return "Draw"
                fighting = False

            hero1_attack = self.attack()
            hero2_attack = opponent.attack()

            hero1_defense = self.defend()
            hero2_defense = opponent.defend()

            self.take_damage(hero2_attack)
            opponent.take_damage(hero1_attack)

            if self.is_alive() == False:
                opponent.add_kill(1)
                self.add_death(1)
                self.status = "Dead"
                opponent.status = "Alive"
                print(opponent.name + " won!")
                fighting = False
            elif opponent.is_alive() == False:
                self.add_kill(1)
                opponent.add_death(1)
                opponent.status = "Dead"
                self.status = "Alive"
                print(self.name + " won!")
                fighting = False
            else:
                continue


class Ability:
    def __init__(self, name, max_damage):
        '''
       Initialize the values passed into this
       method as instance variables.
        '''

        # Assign the "name" and "max_damage"
        # for a specific instance of the Ability class
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' Return a value between 0 and the value set by self.max_damage.'''

        # Pick a random value between 0 and self.max_damage
        random_value = random.randint(0, self.max_damage)
        return random_value


class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties.
            name: String
            max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
        return random_value


class Weapon(Ability):
    def attack(self):
        random_value = random.randint(self.max_damage//2, self.max_damage)
        return random_value


class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        print(str([i.name for i in self.heroes]))

    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            k = hero.kills
            d = hero.deaths
            print(
                f"{hero.name} - Kills: {k} | Deaths: {d}\n")

    def revive_heroes(self, health=100):
        ''' Reset all heroes health to starting_health'''
        for hero in self.heroes:
            hero.current_health = 100
            hero.status = "Alive"

    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for i in self.heroes:
            if i.status == "Alive":
                living_heroes.append(self.heroes.index(i))

        for x in other_team.heroes:
            if x.status == "Alive":
                living_opponents.append(other_team.heroes.index(x))

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hero = self.heroes[random.choice(living_heroes)]
            opponent = other_team.heroes[random.choice(living_opponents)]

            return hero.fight(opponent)


class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''

        self.team_one = None
        self.team_two = None
        self.winning_team = None
        self.team_amt = 0

    """Creates ability"""

    def create_ability(self):
        name = input("Enter Ability Name: ")
        strength = int(input("Enter Ability Attack Strength: "))
        ability = Ability(name, strength)
        return ability

    """Creates weapon"""

    def create_weapon(self):
        name = input("Enter Weapon Name: ")
        strength = int(input("Enter Weapon Attack Strength: "))
        weapon = Weapon(name, strength)
        return weapon
    """Creates armor"""

    def create_armor(self):
        name = input("Enter Armor Name: ")
        block_power = int(input("Enter Blocking Strength: "))
        armor = Armor(name, block_power)
        return armor

    def create_hero(self):
        name = input("Enter Hero Name: ")
        amt = int(input("Enter Hero HP: "))
        hero = Hero(name, amt)

        ability_creation = True
        while ability_creation:
            ability_option = input("Create ability? (Y/N): ").lower()
            if ability_option.isalpha():
                if ability_option == "y":
                    ability = self.create_ability()
                    hero.add_ability(ability)
                elif ability_option == "n":
                    ability_creation = False
                else:
                    print("Not one of the two choices")
                    continue
            else:
                print('Not a letter')
                continue

        weapon_creation = True
        while weapon_creation:
            weapon_option = input("Create weapon? (Y/N): ").lower()
            if weapon_option.isalpha():
                if weapon_option == "y":
                    weapon = self.create_weapon()
                    hero.add_weapon(weapon)
                elif weapon_option == "n":
                    weapon_creation = False
                else:
                    print("Not one of the two choices")
                    continue
            else:
                print('Not a letter')
                continue

        armor_creation = True
        while armor_creation:
            armor_option = input("Create armor? (Y/N): ").lower()
            if armor_option.isalpha():
                if armor_option == "y":
                    armor = self.create_armor()
                    hero.add_armor(armor)
                elif armor_option == "n":
                    armor_creation = False
                else:
                    print("Not one of the two choices")
                    continue
            else:
                print('Not a letter')
                continue

        return hero

    """Functions will loop until user says no to having more heroes"""

    def build_team_one(self):
        self.team_amt = int(input("How many heroes for both teams?: "))
        name = input("Team 1 Name: ")
        self.team_one = Team(name)

        for i in range(self.team_amt):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

        self.team_one.view_all_heroes()

    """Functions will loop until user says no to having more heroes"""

    def build_team_two(self):
        name = input("Team 2 Name: ")
        self.team_two = Team(name)

        for i in range(self.team_amt):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

        self.team_two.view_all_heroes()

    def team_battle(self):
        self.winning_team = self.team_one.attack(self.team_two)

    # def show_stats(self):
    #     print(f"The winner is team:  {self.team_battle}")

        self.team_one.stats()
        self.team_two.stats()

        if self.winning_team == self.team_one.name:
            for hero in self.team_one.heroes:
                if hero.status == "Alive":
                    print("Surviving Heroes: " + hero.name)
        elif self.winning_team == self.team_two.name:
            for hero in self.team_two.heroes:
                if hero.status == "Alive":
                    print("Surviving Heroes: " + hero.name)


if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        # Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
