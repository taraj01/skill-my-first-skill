from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

__author__ = 'fractal13'
LOGGER = LOG.create_logger( __name__ )

class MyFirstSkill( MycroftSkill ):

    def __init__( self ):
        super( MyFirstSkill, self ).__init__( name="MyFirstSkill" )
        LOGGER.info( "__init__" )

    @intent_handler( IntentBuilder( "" ).require( "RocketmanKeyword" ) )
    def handle_rocketman_intent( self, message ):
        LOGGER.info( "rocketman" )
        self.speak_dialog( "rocketman", data={} )

    @intent_handler( IntentBuilder( "" ).require( "GuardiansKeyword" ).require( "GalaxyKeyword" ) )
    def handle_guardians_of_the_galaxy_intent( self, message ):
        LOGGER.info( "guardians" )
        self.speak_dialog( "guardians.galaxy", data={} )

    @intent_handler( IntentBuilder( "" ).require( "WhatKeyword" ).require( "UpKeyword" ) )
    def handle_whats_up_intent( self, message ):
        LOGGER.info( "what's up" )
        self.speak_dialog( "whats.up", data={} )

def create_skill():
    return MyFirstSkill()
