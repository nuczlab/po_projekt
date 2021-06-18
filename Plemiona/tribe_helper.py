from Plemiona.tribe import Tribe
import random


class TribeHelper:
    """
    Helper class
    """

    @staticmethod
    def perform_combat(attacker: Tribe, defender: Tribe):
        """
        Static method used to perform combat between two tribes
        Parameters
        ----------
        attacker : Tribe
            Instance of tribe class
        defender : Tribe
            Instance of defender class
        """
        point_ratio = attacker.soldiers / defender.soldiers
        win_threadshold = 50 / attacker.combat_ability / point_ratio + 5
        rand = random.randint(0, 100)
        attacker.kill_soldiers(attacker.soldiers_used_to_fight * ((100 - rand) / 100))
        defender.kill_soldiers(attacker.soldiers_used_to_fight * ((rand) / 100))
        if rand > win_threadshold:
            attacker.soldiers + (attacker.soldiers_used_to_fight * ((rand) / 100)) / 2
            return True
        return False
