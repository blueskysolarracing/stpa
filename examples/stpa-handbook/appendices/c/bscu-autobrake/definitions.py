from stpa import UnsafeControlAction, Definition

unsafe_control_actions = (
    UnsafeControlAction(
        'BSCU.1a1',
        'Autobrake',
        'does not provide',
        'Brake command',
        'during RTO to V1 (resulting in inability to stop within available runway length)',
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'BSCU.1a2',
        'Autobrake',
        'does not provides',
        'Brake command',
        'during landing roll when BSCU is armed (resulting in insufficient deceleration and potential overshoot)',
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'BCSU.1a4', 
        'Autobrake',
        'does not provide',
        'Brake command',
        'after takeoff (needed to lock wheels, results in potential equipment damage during landing gear retraction or wheel rotation in flight)',
        Definition.get_all('H4-6'),
    ),
    UnsafeControlAction(
        'BSCU.1b1',
        'Autobrake',
        'provides',
        'excessive Braking commands',
        'during landing roll',
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'BSCU.1b2',
        'Autobrake',
        'provides',
        'Braking command inappropriately',
        'during takeoff (resulting in inadequate acceleration)',
        Definition.get_all('H4-1', 'H4-2', 'H4-5'),
    ),
    UnsafeControlAction(
        'BSCU1b3',
        'Autobrake',
        'provides',
        'Brake command with insufficient level',
        '(resulting in insufficient deceleration during landing roll)',
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'BSCU.1c1',
        'Autobrake',
        'provides {} before touchdown',
        'Braking command',
        '(resulting in tire burst, loss of control, injury, other damage)',
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'BSCU.1c2',
        'Autobrake',
        'provides {} more than TBD seconds after touchdown',
        'Brake command',
        '(resulting in insufficient deceleration and potential loss of control, overshoot)',
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'BSCU.1c3',
        'Autobrake',
        'provides',
        'Brake command at any time',
        'before wheels have left ground and RTO has not been requested (brake might be applied to stop wheels before gear retraction)',
        Definition.get_all('H4-1', 'H4-2', 'H4-5'),
    ),
    UnsafeControlAction(
        'BSCU.1c4',
        'Autobrake',
        'provides {} more than TBD seconds',
        'Brake',
        'after V1 during rejected takeoff (assumes that Autobrake is responsible for braking during RTO after crew throttle down)',
        Definition.get_all('H4-2'),
    ),
    UnsafeControlAction(
        'BSCU.1d1',
        'Autobrake',
        'stops providing',
        'Brake',
        'during landing roll before TBD taxi speed attained (causing reduced deceleration)',
        Definition.get_all('H4-1', 'H4-5'),
    ),
    UnsafeControlAction(
        'BSCU.1d2',
        'Autobrake',
        'provides {} too long (more than TBD seconds)',
        'Brake command',
        'during landing roll (causing stop on runway)',
        Definition.get_all('H4-1'),
    ),
    UnsafeControlAction(
        'BSCU.1d3',
        'Autobrake',
        'provides {} until less than TBD seconds',
        'Brake command for tire lock',
        'before touchdown (resulting in loss of control, equipment damage)',
        Definition.get_all('H4-1', 'H4-5'),
    ),
)

if __name__ == "__main__":
    print("Unsafe Control Actions\n------")
    for uca in unsafe_control_actions:
        print(uca)