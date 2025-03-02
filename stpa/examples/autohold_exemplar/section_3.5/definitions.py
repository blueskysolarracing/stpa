# type: ignore

from stpa.definitions import (
    Definition,
    Loss,
    Hazard,
    UnsafeControlAction,
    SystemLevelConstraintType1,
    ScenarioType1,
)


UCAS_ESS = (
    UnsafeControlAction(
        name="UCA-ESS-1",
        source="Engine Stop-Start Module",
        type_="Not providing {} is hazardous",
        control_action="RESTART",
        context="if the driver releases the brake while system is in AUTO-STOPPED",
        hazards=Definition.get_all("H-3"),
    ),
    UnsafeControlAction(
        name="UCA-ESS-2",
        source="Engine Stop-Start Module",
        type_="Providing {} is hazardous",
        control_action="RESTART",
        context="if the car is not AUTO-STOPPED",
        hazards=Definition.get_all("H-1", "H-2", "H-3"),
    ),
    UnsafeControlAction(
        name="UCA-ESS-3",
        source="Engine Stop-Start Module",
        type_="Not providing {} within TBD time is hazardous",
        control_action="RESTART",
        context="after driver releases brake while in 'standstill'",
        hazards=Definition.get_all("H-3"),
    ),
    UnsafeControlAction(
        name="UCA-ESS-4",
        source="Engine Stop-Start Module",
        type_="Not providing {} is hazardous",
        control_action="RESTART",
        context="if a critical non-propulsion power need arises",
        hazards=Definition.get_all("H-3"),
    ),
    UnsafeControlAction(
        name="UCA-ESS-5",
        source="Engine Stop-Start Module",
        type_="Providing {} is hazardous",
        control_action="RESTART",
        context="if the engine is running - damage to the starter mechanism",
        hazards=Definition.get_all("H-3"),
    ),
    UnsafeControlAction(
        name="UCA-ESS-6",
        source="Engine Stop-Start Module",
        type_="Not providing {} is hazardous",
        control_action="RESTART",
        context="in conditions for a favorable restart change",
        hazards=Definition.get_all("H-3"),
    ),
    UnsafeControlAction(
        name="UCA-ESS-7",
        source="Engine Stop-Start Module",
        type_="Providing {} is hazardous",
        control_action="STOP",
        context="if driver has not brought vehicle to stop with brake",
        hazards=Definition.get_all("H-1", "H-3"),
    ),
    UnsafeControlAction(
        name="UCA-ESS-8",
        source="Engine Stop-Start Module",
        type_="Providing {} is hazardous",
        control_action="STOP",
        context="if it is done before vehicle is at rest",
        hazards=Definition.get_all("H-1", "H-3"),
    ),
    UnsafeControlAction(
        name="UCA-ESS-9",
        source="Engine Stop-Start Module",
        type_="Providing {} is hazardous",
        control_action="STOP",
        context="if there will not be sufficient power for RESTART",
        hazards=Definition.get_all("H-3"),
    ),
)


SAFETY_CONSTRAINTS_ESS = (
    SystemLevelConstraintType1(
        name="SC-ESS-1",
        system="Engine Stop-Start Module",
        enforcement_condition=(
            "ESS should not STOP the engine when the vehicle is in motion. "
            "Rationale: UCA-ESS-7,8"
        ),
        hazards=[],
    ),
    SystemLevelConstraintType1(
        name="SC-ESS-2",
        system="Engine Stop-Start Module",
        enforcement_condition=(
            "ESS should RESTART the engine before motion resumes once AUTO-STOPPED. "
            "Rationale: UCA-ESS-1,3"
        ),
        hazards=[],
    ),
    SystemLevelConstraintType1(
        name="SC-ESS-3",
        system="Engine Stop-Start Module",
        enforcement_condition=(
            "ESS should not start the engine unless it is currently AUTO-STOPPED. "
            "Rationale: UCA-ESS-2"
        ),
        hazards=[],
    ),
    SystemLevelConstraintType1(
        name="SC-ESS-4",
        system="Engine Stop-Start Module",
        enforcement_condition=(
            "ESS should not prevent the operation of other vehicle subsystems. "
            "Rationale: UCA-ESS-4,5"
        ),
        hazards=[],
    ),
    SystemLevelConstraintType1(
        name="SC-ESS-5",
        system="Engine Stop-Start Module",
        enforcement_condition=(
            "ESS should not operate when it is not able to complete a full operational cycle. "
            "Rationale: UCA-ESS-6,9"
        ),
        hazards=[],
    ),
)


uca_ess_1 = next(uca for uca in UCAS_ESS if uca.name == "UCA-ESS-1")

LOSS_SCENARIOS_ESS = (
    ScenarioType1(
        name="Scenario 1 for UCA-ESS-1",
        description=(
            "Algorithm does not correctly predict battery voltage drain and is unable to engage the starter."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 2 for UCA-ESS-1",
        description=(
            "ESS does not abstract Vehicle Held correctly when combining inputs from various braking systems and believes the vehicle is held when it is not."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 3 for UCA-ESS-1",
        description=(
            "Auxiliary power needs are not monitored, or are not sufficiently anticipated, and the controller reports Low when the value should be High leading to an inability to Restart."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 4 for UCA-ESS-1",
        description=(
            "Brake sensor fails or reports a false value such that the brake release is not captured and ESS does not anticipate motion."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 5 for UCA-ESS-1",
        description=(
            "Noise is not adequately filtered and the brake release is not identified."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 6 for UCA-ESS-1",
        description=(
            "Sensors do not detect sufficiently small/slow changes in value. E.g., the brake sensor does not detect a small shift in pedal position that may allow the vehicle to begin slipping."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 7 for UCA-ESS-1",
        description=(
            "Engine performance changes over time such that the actual torque does not match that assumed by the ESS algorithm."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 8 for UCA-ESS-1",
        description=(
            "Engine misfires during startup and allows the vehicle to roll."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 9 for UCA-ESS-1",
        description=(
            "Engine does not receive the proper air/fuel mixture and cannot start."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 10 for UCA-ESS-1",
        description=(
            "Starter degrades over time due to weathering and exposure and does not execute the RESTART command."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 11 for UCA-ESS-1",
        description=(
            "Starter degrades due to excessive cycles."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 12 for UCA-ESS-1",
        description=(
            "Starter does not operate within an acceptable timeframe (TBD seconds)."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 13 for UCA-ESS-1",
        description=(
            "The driver attempts to shut-off the vehicle as ESS commands a RESTART."
        ),
        unsafe_control_action=uca_ess_1,
        result=None,
        hazard=None,
    ),
)
