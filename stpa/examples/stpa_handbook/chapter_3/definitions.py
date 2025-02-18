from stpa.definitions import Definition, Hazard, SubHazard

HAZARDS = (
    Hazard('H4', 'aircraft', 'An {} on the ground comes too close to moving or stationary objects or inadvertently leaves the taxiway', []),
)

SUB_HAZARDS = (
    SubHazard('H4-1', Definition.get('H4'), 'Inadequate aircraft deceleration upon landing, rejected takeoff, or taxiing'),
    SubHazard('H4-2', Definition.get('H4'), 'Deceleration after the V116 point during takeoff'),
    SubHazard('H4-4', Definition.get('H4'), 'Unintentional aircraft directional control (differential braking)'),
    SubHazard('H4-4', Definition.get('H4'), 'Unintentional aircraft directional control (differential braking)'),
    SubHazard('H4-5', Definition.get('H4'), 'Aircraft maneuvers out of safe regions (taxiways, runways, terminal gates, ramps, etc.)'),
    SubHazard('H4-6', Definition.get('H4'), 'Main gear wheel rotation is not stopped when (continues after) the landing gear is retracted'),
)

ALIASES = (
    SubHazard('H4.1', Definition.get('H4'), Definition.get('H4-1').description),
    SubHazard('H4.2', Definition.get('H4'), Definition.get('H4-2').description),
    SubHazard('H4.4', Definition.get('H4'), Definition.get('H4-4').description),
    SubHazard('H4.5', Definition.get('H4'), Definition.get('H4-5').description),
    SubHazard('H4.6', Definition.get('H4'), Definition.get('H4-6').description),
)

