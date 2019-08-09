# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

from mycroft.util.parse import match_one
from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel
from mycroft import intent_handler
from adapt.intent import IntentBuilder
from mycroft.audio import wait_while_speaking

import random
import os

class LocalMusic(CommonPlaySkill):
    def __init__(self):
        """
        Initializes the playing variable.
        """
        super(LocalMusic, self).__init__(name="LocalMusic")
        self.playing = False

    def CPS_match_query_phrase(self, phrase):
        """
        This method checks if phrase is valid song to play.

        This method is invoked by PlayBackControlSkill.

        returns: tuple ((str) matched phrase,
                        CPSMatchLevel,
                        (dict) optional data)
                 or None if no match found.
        """
        musicPath = os.path.join(os.path.expanduser("~"), "Music")
        songs = []
        for (dirpath, dirnames, songnames) in os.walk(musicPath):
            validSongs = [song for song in songnames if song[-4:] == ".mp3"]
            if validSongs:
                songs.append((dirpath, validSongs))
        if phrase in ("any song", "another song"): # then randomly choose a song
            level = random.randint(0, len(songs)-1)
            choice = random.randint(0, len(songs[level][1])-1)
            songName = songs[level][1][choice]
            return (phrase, CPSMatchLevel.GENERIC, {songName:os.path.join(songs[level][0], songName)})
        else:
            maxConfIndex = 0
            maxConf = -1
            for index, tup in enumerate(songs):
                match, confidence = match_one(phrase, [song[:-4] for song in tup[1]])
                if confidence > maxConf:
                    maxConf = confidence
                    maxConfIndex = index
                    actualMatch = match
            if maxConf > 0.5:
                return (phrase, CPSMatchLevel.TITLE, {actualMatch:os.path.join(songs[maxConfIndex][0], actualMatch+".mp3")})

        return None

    def CPS_start(self, phrase, data):
        """
        Starts playback.
        Called if this skill has best match.
        """
        if len(data) == 1:
            name = list(data.keys())[0]
            url = data[name]
            self.speak_dialog("play", data={"song":name})
            wait_while_speaking()
            self.audioservice.play(url)
            self.playing = True
        #options = list(data.keys())
        #name = options[0]
        #url = data[name]
        #self.speak_dialog("play", data={"song":name})
        #wait_while_speaking()
        #self.audioservice.play(url)

    @intent_handler(IntentBuilder('PauseIntent').require('PauseKeyword'))
    def handle_pause_intent(self, message):
        if self.playing == True:
            self.audioservice.pause()
            self.speak_dialog("pause")
            self.playing = False

    @intent_handler(IntentBuilder('ResumeIntent').require('ResumeKeyword'))
    def handle_resume_intent(self, message):
        if self.playing == False:
            self.speak_dialog("resume")
            wait_while_speaking()
            self.audioservice.resume()
            self.playing = True

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. Returns True to show successfully handled stop.
    def stop(self):
        """
        This skill handles stop if a track is playing.
        """
        if self.playing == True:
            self.audioservice.stop()
            self.speak_dialog("stop")
            self.playing = False
            return True
        return False

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return LocalMusic()

