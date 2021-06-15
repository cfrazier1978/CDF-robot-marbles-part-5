from models.updates import *

partial_state_update_blocks = [
    { 
        'policies': { # The following policy functions will be evaluated and their returns will be passed to the state update functions
            'action': robotic_network
        },
        'states': { # The following state variables will be updated simultaneously
            'network': update_network
            
        }
    }
]