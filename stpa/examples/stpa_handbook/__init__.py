
from .appendix_a import *
from .chapter_2 import definitions as c2_defs
from .appendix_c.aircraft_brake_system_control_unit_autobrake import (
    definitions as app_c_abscua_defs,
)
from .appendix_c.automotive_auto_hold_system import (
    definitions as app_c_aas_defs,
)
from .appendix_c.autonomous_h_ii_transfer_vehicle_operations import (
    definitions as app_c_ahtvo_defs,
)
from .appendix_c.wheel_braking_system_aircraft_flight_crew import (
    definitions as app_c_wbscafc_defs,
)

UNSAFE_CONTROL_ACTIONS = (
    *c2_defs.UNSAFE_CONTROL_ACTIONS,
    *app_c_abscua_defs.UNSAFE_CONTROL_ACTIONS,
    *app_c_aas_defs.UNSAFE_CONTROL_ACTIONS,
    *app_c_ahtvo_defs.UNSAFE_CONTROL_ACTIONS,
    *app_c_wbscafc_defs.UNSAFE_CONTROL_ACTIONS,
)

