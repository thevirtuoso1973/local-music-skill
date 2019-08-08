# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel

import os

class LocalMusic(CommonPlaySkill):
    def CPS_match_query_phrase(self, phrase):
        """
        This method checks if phrase is valid song to play.

        This method is invoked by PlayBackControlSkill.

        returns: tuple ((str) matched phrase,
                        CPSMatchLevel,
                        (dict) optional data)
                 or None if no match found.
        """
        path = os.path.join(os.path.expanduser("~"), "Music", "Tomb-Mold-Manor-Of-Infinite-Forms.mp3")
        return (phrase, CPSMatchLevel.CATEGORY, {"Tomb Mold": path}) if phrase=="metal" else None

    def CPS_start(self, phrase, data):
        """
        Starts playback.
        Called if this skill has best match.
        """
        url = list(data.values())[0]
        self.audioservice.play(url)


    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, there is no need to override it.  If you DO
    # need to implement stop, you should return True to indicate you handled
    # it.
    #
    # def stop(self):
    #    return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return LocalMusic()

