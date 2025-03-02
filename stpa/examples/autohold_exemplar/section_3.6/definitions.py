# type: ignore

from stpa.definitions import (
    Definition,
    UnsafeControlAction,
    SystemLevelConstraintType1,
    ScenarioType1,
)


UCAS_SG = (
    UnsafeControlAction(
        name="UCA-SG-2",
        source="ACC w/SG Module",
        type_="It is hazardous to not provide {}",
        control_action="ACCELERATE",
        context="when a vehicle or other mobile object is approaching at TBD rate/distance",
        hazards=Definition.get_all("H-1"),
    ),
    UnsafeControlAction(
        name="UCA-SG-3",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {}",
        control_action="ACCELERATE",
        context="if the vehicle is already at the preset speed",
        hazards=Definition.get_all("H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-4",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {}",
        control_action="ACCELERATE",
        context="before ACC is engaged",
        hazards=Definition.get_all("H-1", "H-2", "H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-5",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {} too long",
        control_action="ACCELERATE",
        context="such that the vehicle exceeds the preset speed",
        hazards=Definition.get_all("H-1", "H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-6",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {}",
        control_action="ACCELERATE",
        context="if the vehicle is closer than the minimum safe distance from a leading vehicle",
        hazards=Definition.get_all("H-1"),
    ),
    UnsafeControlAction(
        name="UCA-SG-7",
        source="ACC w/SG Module",
        type_="It is hazardous to issue {} too late",
        control_action="ACCELERATE",
        context="after the speed is set and ACC is engaged",
        hazards=Definition.get_all("H-1", "H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-8",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {} too long",
        control_action="ACCELERATE",
        context="such that the vehicle violates a minimum safe trailing distance from a leading vehicle in the lane",
        hazards=Definition.get_all("H-1"),
    ),
    UnsafeControlAction(
        name="UCA-SG-9",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {}",
        control_action="ACCELERATE",
        context="if the vehicle is moving to collide with an object within TBD rate/distance in its trajectory",
        hazards=Definition.get_all("H-1", "H-2"),
    ),
    UnsafeControlAction(
        name="UCA-SG-10",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {}",
        control_action="ACCELERATE",
        context="if the vehicle is at rest and the driver has not indicated it is safe to resume motion",
        hazards=Definition.get_all("H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-11",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {}",
        control_action="ACCELERATE",
        context="if ACC is not enabled/engaged",
        hazards=Definition.get_all("H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-12",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {}",
        control_action="ACCELERATE",
        context="if it closes a gap at a high range rate",
        hazards=Definition.get_all("H-1", "H-2", "H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-13",
        source="ACC w/SG Module",
        type_="It is hazardous to not provide {}",
        control_action="DECELERATE",
        context="if there is an obstacle ahead in the lane and the range rate is negative",
        hazards=Definition.get_all("H-1", "H-2"),
    ),
    UnsafeControlAction(
        name="UCA-SG-14",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {} too abruptly",
        control_action="DECELERATE",
        context="",
        hazards=Definition.get_all("H-1", "H-3", "H-4"),
    ),
    UnsafeControlAction(
        name="UCA-SG-15",
        source="ACC w/SG Module",
        type_="It is hazardous if {} is issued too late",
        control_action="DECELERATE",
        context="after an obstacle (fixed or slowing vehicle) has been detected",
        hazards=Definition.get_all("H-1", "H-2"),
    ),
    UnsafeControlAction(
        name="UCA-SG-16",
        source="ACC w/SG Module",
        type_="It is hazardous if {} is not provided long enough",
        control_action="DECELERATE",
        context="to sufficiently decelerate the vehicle",
        hazards=Definition.get_all("H-1", "H-2", "H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-17",
        source="ACC w/SG Module",
        type_="It is hazardous to not provide {}",
        control_action="DECELERATE",
        context="if the vehicle is closer than the minimum safe distance from a leading vehicle and the range rate is not increasing",
        hazards=Definition.get_all("H-1"),
    ),
    UnsafeControlAction(
        name="UCA-SG-18",
        source="ACC w/SG Module",
        type_="It is hazardous to not provide {}",
        control_action="DECELERATE",
        context="if the vehicle is closing faster than some TBD rate/distance on an obstacle ahead",
        hazards=Definition.get_all("H-1", "H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-19",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {}",
        control_action="DECELERATE",
        context="if it slows the vehicle's speed too much for the given roadway traffic conditions",
        hazards=Definition.get_all("H-1", "H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-20",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {}",
        control_action="DECELERATE",
        context="if ACC is not enabled/engaged",
        hazards=Definition.get_all("H-3"),
    ),
    UnsafeControlAction(
        name="UCA-SG-21",
        source="ACC w/SG Module",
        type_="It is hazardous to provide {}",
        control_action="DECELERATE",
        context="when not commanded by the driver and there is no obstacle ahead",
        hazards=Definition.get_all("H-1", "H-3"),
    ),
)


SAFETY_CONSTRAINTS_SG = (
    SystemLevelConstraintType1(
        name="SC-SG-1",
        system="ACC w/SG Module",
        enforcement_condition=(
            "SG may not exceed driver set limits on speed and following distance. "
            "Rationale: UCA-SG-2,3,5,6,8,9,12,13,17,18"
        ),
        hazards=[],
    ),
    SystemLevelConstraintType1(
        name="SC-SG-2",
        system="ACC w/SG Module",
        enforcement_condition=(
            "SG should issue commands that provide smooth vehicle acceleration "
            "(positive and negative). ACC w/SG is intended to aid the driver in maintaining "
            "a safe speed and following distance. It does not have the feedback or intelligence to "
            "override driver input. Rationale: UCA-SG-14,19"
        ),
        hazards=[],
    ),
    SystemLevelConstraintType1(
        name="SC-SG-3",
        system="ACC w/SG Module",
        enforcement_condition=(
            "SG must issue commands to avoid a collision. ACC w/SG should not decrease the ride quality "
            "during normal operation. Rationale: UCA-SG-15,16"
        ),
        hazards=[],
    ),
    SystemLevelConstraintType1(
        name="SC-SG-4",
        system="ACC w/SG Module",
        enforcement_condition=(
            "SG must not issue commands when it has not been enabled by the driver. "
            "Rationale: UCA-SG-4,8,11,20"
        ),
        hazards=[],
    ),
)


uca_sg_9 = next(uca for uca in UCAS_SG if uca.name == "UCA-SG-9")

LOSS_SCENARIOS_ACCELERATE = (
    ScenarioType1(
        name="Scenario 1 for UCA-SG-9",
        description=(
            "Algorithm does not correctly calculate the closing distance and rate to an object ahead."
        ),
        unsafe_control_action=uca_sg_9,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 2 for UCA-SG-9",
        description=(
            "At the time ACC w/SG is engaged, the target is too close to identify, calculate, and mitigate."
        ),
        unsafe_control_action=uca_sg_9,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 3 for UCA-SG-9",
        description=(
            "The controller does not lock onto a target and thus does not anticipate a collision."
        ),
        unsafe_control_action=uca_sg_9,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 4 for UCA-SG-9",
        description=(
            "Distance threshold is incorrect and allows the vehicle to get too close to the target."
        ),
        unsafe_control_action=uca_sg_9,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 5 for UCA-SG-9",
        description=(
            "Radar is unable to detect targets due to road and weather conditions."
        ),
        unsafe_control_action=uca_sg_9,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 6 for UCA-SG-9",
        description=(
            "Radar data is not returned at a sufficient rate to avoid a collision."
        ),
        unsafe_control_action=uca_sg_9,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 7 for UCA-SG-9",
        description=(
            "Noise is not adequately filtered and a small target is not identified."
        ),
        unsafe_control_action=uca_sg_9,
        result=None,
        hazard=None,
    ),
)

uca_sg_14 = next(uca for uca in UCAS_SG if uca.name == "UCA-SG-14")

LOSS_SCENARIOS_DECELERATE = (
    ScenarioType1(
        name="Scenario 1 for UCA-SG-14",
        description=(
            "Tire treads are too low to provide adequate friction for decelerating."
        ),
        unsafe_control_action=uca_sg_14,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 2 for UCA-SG-14",
        description=(
            "Change in tire size unaccompanied by recalibration offsets the wheel speed readings which compromises the closing distance calculations."
        ),
        unsafe_control_action=uca_sg_14,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 3 for UCA-SG-14",
        description=(
            "Brakes degrade over time (alignment, pads, seals, hydraulic lines) and cannot match original performance."
        ),
        unsafe_control_action=uca_sg_14,
        result=None,
        hazard=None,
    ),
    ScenarioType1(
        name="Scenario 4 for UCA-SG-14",
        description=(
            "Brake force is not adequate to meet required deceleration."
        ),
        unsafe_control_action=uca_sg_14,
        result=None,
        hazard=None,
    ),
)
