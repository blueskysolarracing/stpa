from pathlib import Path
from textwrap import dedent
from unittest import TestCase

from stpa import ControlActionOrFeedback, ControlStructure, ControlType, Entity


class ExamplesTestCase(TestCase):
    def test_stpa_handbook_chapter_2_definitions(self) -> None:
        import stpa.examples.stpa_handbook.chapter_2.definitions as definitions

        losses = definitions.LOSSES  # type: ignore[attr-defined]
        raw_losses = (
            'L-1: Loss of life or injury to people',
            'L-2: Loss of or damage to vehicle',
            'L-3: Loss of or damage to objects outside the vehicle',
            (
                'L-4: Loss of mission (e.g. transportation mission,'
                ' surveillance mission, scientific mission, defense mission,'
                ' etc.)'
            ),
            'L-5: Loss of customer satisfaction',
            'L-6: Loss of sensitive information',
            'L-7: Environmental loss',
            'L-8: Loss of power generation',
        )

        for loss, raw_loss in zip(losses, raw_losses):
            self.assertEqual(str(loss), raw_loss)

        hazards = definitions.HAZARDS  # type: ignore[attr-defined]
        raw_hazards = (
            (
                'H-1: Aircraft violate minimum separation standards in flight'
                ' [L-1, L-2, L-4, L-5]'
            ),
            'H-2: Aircraft airframe integrity is lost [L-1, L-2, L-4, L-5]',
            (
                'H-3: Aircraft leaves designated taxiway, runway, or apron on'
                ' ground [L-1, L-2, L-5]'
            ),
            (
                'H-4: Aircraft comes too close to other objects on the ground'
                ' [L-1, L-2, L-5]'
            ),
            'H-5: Satellite is unable to collect scientific data [L-4]',
            (
                'H-6: Vehicle does not maintain safe distance from terrain and'
                ' other obstacles [L-1, L-2, L-3, L-4]'
            ),
            'H-7: UAV does not complete surveillance mission [L-4]',
            (
                'H-8: Nuclear power plant releases dangerous materials [L-1,'
                ' L-4, L-7, L-8]'
            ),
        )

        for hazard, raw_hazard in zip(hazards, raw_hazards):
            self.assertEqual(str(hazard), raw_hazard)

        system_level_constraints = (
            definitions.SYSTEM_LEVEL_CONSTRAINTS  # type: ignore[attr-defined]
        )
        raw_system_level_constraints = (
            (
                'SC-1: Aircraft must satisfy minimum separation standards from'
                ' other aircraft and objects [H-1]'
            ),
            (
                'SC-2: Aircraft airframe integrity must be maintained under'
                ' worst-case conditions [H-2]'
            ),
            (
                'SC-3: If Aircraft violate minimum separation standards in'
                ' flight, then the violation must be detected and measures'
                ' taken to prevent collision [H-1]'
            ),
            (
                'SC-6.1: Deceleration must occur within TBD seconds of landing'
                ' or rejected takeoff at a rate of at least TBD m/s^2'
            ),
            (
                'SC-6.2: Asymmetric deceleration must not lead to loss of'
                ' directional control or cause aircraft to depart taxiway,'
                ' runway, or apron'
            ),
            (
                'SC-6.3: Deceleration must not be provided after V1 point'
                ' during takeoff'
            ),
        )

        for system_level_constraint, raw_system_level_constraint in zip(
                system_level_constraints,
                raw_system_level_constraints,
        ):
            self.assertEqual(
                str(system_level_constraint),
                raw_system_level_constraint,
            )

        sub_hazards = definitions.SUB_HAZARDS  # type: ignore[attr-defined]
        raw_sub_hazards = {
            'H-4': (
                (
                    'H-4.1: Deceleration is insufficient upon landing,'
                    ' rejected takeoff, or during taxiing'
                ),
                (
                    'H-4.2: Asymmetric deceleration maneuvers aircraft toward'
                    ' other objects'
                ),
                'H-4.3: Deceleration occurs after V1 point during takeoff',
                'H-4.4: Excessive acceleration provided while taxiing',
                (
                    'H-4.5: Asymmetric acceleration maneuvers aircraft toward'
                    ' other objects'
                ),
                'H-4.6: Acceleration is insufficient during takeoff',
                (
                    'H-4.7: Acceleration is provided during landing or when'
                    ' parked'
                ),
                (
                    'H-4.8: Acceleration continues to be applied during'
                    ' rejected takeoff'
                ),
                (
                    'H-4.9: Insufficient steering to turn along taxiway,'
                    ' runway, or apron path'
                ),
                (
                    'H-4.10: Steering maneuvers aircraft off the taxiway,'
                    ' runway, or apron path'
                ),
            ),
        }

        for key, value in sub_hazards.items():
            for sub_hazard, raw_sub_hazard in zip(value, raw_sub_hazards[key]):
                self.assertEqual(str(sub_hazard), raw_sub_hazard)

        responsibilities = (
            definitions.RESPONSIBILITIES  # type: ignore[attr-defined]
        )
        raw_responsibilities = (
            (
                'R-1: Decelerate wheels when commanded by BSCU or Flight Crew'
                ' [SC-6.1]'
            ),
            'R-2: Actuate brakes when requested by flight crew [SC-6.1]',
            'R-3: Pulse brakes in case of a skid (Anti-skid) [SC-6.2]',
            (
                'R-4: Automatically engage brakes on landing or rejected'
                ' takeoff (Autobrake) [SC-6.1]'
            ),
            'R-5: Decide when braking is needed [SC-6.1, SC-6.3]',
            (
                'R-6: Decide how braking will be done: Autobrake, normal'
                ' braking, or manual braking [SC-6.1]'
            ),
            (
                'R-7: Configure BSCU and Autobrake to prepare for braking'
                ' [SC-6.1]'
            ),
            (
                'R-8: Monitor braking and disable BSCU, manually brake in case'
                ' of malfunction [SC-6.1, SC-6.2]'
            ),
        )

        for responsibility, raw_responsibility in zip(
                responsibilities,
                raw_responsibilities,
        ):
            self.assertEqual(str(responsibility), raw_responsibility)

        unsafe_control_actions = (
            definitions.UNSAFE_CONTROL_ACTIONS  # type: ignore[attr-defined]
        )
        raw_unsafe_control_actions = (
            (
                'UCA-1: BSCU Autobrake does not provide the Brake control'
                ' action during landing roll when the BSCU is armed [H-4.1]'
            ),
            (
                'UCA-2: BSCU Autobrake provides Brake control action during'
                ' a normal takeoff [H-4.3, H-4.6]'
            ),
            (
                'UCA-5: BSCU Autobrake provides Brake control action with an'
                ' insufficient level of braking during landing roll [H-4.1]'
            ),
            (
                'UCA-6: BSCU Autobrake provides Brake control action with'
                ' directional or asymmetrical braking during landing roll'
                ' [H-4.1, H-4.2]'
            ),
            (
                'UCA-3: BSCU Autobrake provides the Brake control action too'
                ' late (>TBD seconds) after touchdown [H-4.1]'
            ),
            (
                'UCA-4: BSCU Autobrake stops providing the Brake control'
                ' action too early (before TBD taxi speed attained) when'
                ' aircraft lands [H-4.1]'
            ),
            (
                'Crew-UCA-1: Crew does not provide BSCU Power Off when'
                ' abnormal WBS behavior occurs [H-4.1, H-4.4, H-7]'
            ),
            (
                'Crew-UCA-2: Crew provides BSCU Power Off when Anti-Skid'
                ' functionality is needed and WBS is functioning normally'
                ' [H-4.1, H-7]'
            ),
            (
                'Crew-UCA-3: Crew powers off BSCU too early before Autobrake'
                ' or Anti-Skid behavior is completed when it is needed [H-4.1,'
                ' H-7]'
            ),
        )

        for unsafe_control_action, raw_unsafe_control_action in zip(
                unsafe_control_actions,
                raw_unsafe_control_actions,
        ):
            self.assertEqual(
                str(unsafe_control_action),
                raw_unsafe_control_action,
            )

        controller_constraints = (
            definitions.CONTROLLER_CONSTRAINTS  # type: ignore[attr-defined]
        )
        raw_controller_constraints = (
            (
                'C-1: BSCU Autobrake must provide the Brake control action'
                ' during landing roll when the BSCU is armed [UCA-1]'
            ),
            (
                'C-2: BSCU Autobrake must not provide Brake control action'
                ' during a normal takeoff [UCA-2]'
            ),
            (
                'C-3: BSCU Autobrake must provide the Brake control action'
                ' within TBD seconds after touchdown [UCA-3]'
            ),
            (
                'C-4: BSCU Autobrake must not stop providing the Brake control'
                ' action before TBD taxi speed is attained during landing roll'
                ' [UCA-4]'
            ),
            (
                'C-5: BSCU Autobrake must not provide less than TBD level of'
                ' braking during landing roll [UCA-5]'
            ),
            (
                'C-6: BSCU Autobrake must not provide directional or'
                ' asymmetrical braking during landing roll [UCA-6]'
            ),
        )

        for controller_constraint, raw_controller_constraint in zip(
                controller_constraints,
                raw_controller_constraints,
        ):
            self.assertEqual(
                str(controller_constraint),
                raw_controller_constraint,
            )

        scenarios = definitions.SCENARIOS  # type: ignore[attr-defined]
        raw_scenarios = (
            (
                'Scenario 1 for UCA-1: The BSCU Autobrake physical controller'
                ' fails during landing roll when BSCU is armed, causing the'
                ' Brake control action to not be provided [UCA-1]. As a'
                ' result, insufficient deceleration may be provided upon'
                ' landing [H-4.1].'
            ),
            (
                'Scenario 1 for UCA-3: The aircraft lands, but processing'
                ' delays within the BSCU result in the Brake control action'
                ' being provided too late [UCA-3]. As a result, insufficient'
                ' deceleration may be provided upon landing [H-4.1].'
            ),
            (
                'Scenario 1 for Crew-UCA-1: Abnormal WBS behavior occurs and a'
                ' BSCU fault indication is provided to the crew. The crew does'
                ' not power off the BSCU [Crew-UCA-1] because the operating'
                ' procedures did not specify that the crew must power off the'
                ' BSCU upon receiving a BSCU fault indication.'
            ),
            (
                'Scenario 1 for UCA-2: The BSCU is armed and the aircraft'
                ' begins landing roll. The BSCU does not provide the Brake'
                ' control action [UCA-2] because the BSCU incorrectly believes'
                ' the aircraft has already come to a stop. This flawed process'
                ' model will occur if the received feedback momentarily'
                ' indicates zero speed during landing roll. The received'
                ' feedback may momentarily indicate zero speed during'
                ' anti-skid operation, even though the aircraft is not'
                ' stopped.'
            ),
            dedent(
                '''\
                Scenario 2 for UCA-2: The BSCU is armed and the aircraft\
 begins landing roll. The BSCU does not provide the Brake control action\
 [UCA-2] because the BSCU incorrectly believes the aircraft is in the air and\
 has not touched down. This flawed process model will occur if the touchdown\
 indication is not received upon touchdown. The touchdown indication may not\
 be received when needed if any of the following occur:

                - Wheels hydroplane due to a wet runway (insufficient wheel\
 speed)
                - Wheel speed feedback is delayed due to filtering used
                - Conflicting air/ground indications due to crosswind landing
                - Failure of wheel speed sensors
                - Failure of air/ground switches
                - Etc.

                As a result, insufficient deceleration may be provided upon\
 landing [H-4.1].
                '''.rstrip(),
            ),
            (
                'Scenario 1: The BSCU sends the Brake command upon landing,'
                ' but the brakes are not applied due to actuator failure. As a'
                ' result, insufficient deceleration may be provided upon'
                ' landing [H-4.1].'
            ),
            (
                'Scenario 2: The BSCU sends the Brake command upon landing,'
                ' but insufficient braking is applied due to slow actuator'
                ' response. As a result, insufficient deceleration may be'
                ' provided upon landing [H-4.1].'
            ),
            (
                'Scenario 3: The BSCU sends the Brake command upon landing,'
                ' but it is not received by the actuator due to a wiring'
                ' error. As a result, insufficient deceleration may be'
                ' provided upon landing [H-4.1].'
            ),
            (
                'Scenario 4: The BSCU does not send Brake command, but the'
                ' brakes are applied due to hydraulic valve failure. As a'
                ' result, acceleration may be insufficient during takeoff'
                ' [H-4.6].'
            ),
            (
                'Scenario 5: The BSCU sends the Brake command, but the brakes'
                ' are not applied because an adversary executes a denial of'
                ' service attack that blocks the Brake command. As a result,'
                ' insufficient deceleration may be provided upon landing'
                ' [H-4.1].'
            ),
            (
                'Scenario 6: The BSCU sends Brake command, but the brakes are'
                ' not applied because the wheel braking system was previously'
                ' commanded into alternate braking mode (bypassing the BSCU).'
                ' As a result, insufficient deceleration may be provided upon'
                ' landing [H-4.1].'
            ),
            (
                'Scenario 7: The BSCU sends Brake command, but the brakes are'
                ' not applied due to insufficient hydraulic pressure (pump'
                ' failure, hydraulic leak, etc.). As a result, insufficient'
                ' deceleration may be provided upon landing [H-4.1].'
            ),
            (
                'Scenario 8: The BSCU sends Brake command, the brakes are'
                ' applied, but the aircraft does not decelerate due to a wet'
                ' runway (wheels hydroplane). As a result, insufficient'
                ' deceleration may be provided upon landing [H-4.1].'
            ),
            (
                'Scenario 9: The BSCU sends Brake command, but the brakes are'
                ' not applied because an adversary injected a command that put'
                ' the wheel braking system into alternate braking mode. As a'
                ' result, insufficient deceleration may be provided upon'
                ' landing [H-4.1].'
            ),
        )

        for scenario, raw_scenario in zip(scenarios, raw_scenarios):
            self.maxDiff = None
            self.assertEqual(str(scenario), raw_scenario)

    def test_stpa_handbook_figure_2_11(self) -> None:
        import stpa.examples.stpa_handbook.chapter_2 as chapter_2

        path = Path(chapter_2.__file__).parent / 'figure-2.11.xml'
        control_structure = ControlStructure.parse_diagram(path)
        flight_crew = Entity('Flight Crew')
        aircraft = Entity('Aircraft')
        wheel_braking_subsystem = Entity('Wheel Braking Subsytem (WBS)')
        other_subsystems = Entity('Other subsystems')
        brake_system_control_unit = Entity('Brake System Control Unit(BSCU)')
        physical_wheel_brakes = Entity('Physical Wheel Brakes')
        entities = {
            flight_crew,
            aircraft,
            wheel_braking_subsystem,
            other_subsystems,
            brake_system_control_unit,
            physical_wheel_brakes,
        }
        control_actions_or_feedbacks = {
            ControlActionOrFeedback(
                'Manual controls(Engine throttle,Steer, Reverse thrust,etc.)',
                ControlType.ACTION,
                flight_crew,
                other_subsystems,
            ),
            ControlActionOrFeedback(
                '',
                ControlType.FEEDBACK,
                flight_crew,
                other_subsystems,
            ),
            ControlActionOrFeedback(
                'Arm and Set,Disarm,Brake',
                ControlType.ACTION,
                flight_crew,
                brake_system_control_unit,
            ),
            ControlActionOrFeedback(
                '',
                ControlType.FEEDBACK,
                flight_crew,
                brake_system_control_unit,
            ),
            ControlActionOrFeedback(
                'Brake',
                ControlType.ACTION,
                brake_system_control_unit,
                physical_wheel_brakes,
            ),
            ControlActionOrFeedback(
                '',
                ControlType.FEEDBACK,
                brake_system_control_unit,
                physical_wheel_brakes,
            ),
            ControlActionOrFeedback(
                'ManualBraking',
                ControlType.ACTION,
                flight_crew,
                physical_wheel_brakes,
            ),
            ControlActionOrFeedback(
                '',
                ControlType.FEEDBACK,
                flight_crew,
                physical_wheel_brakes,
            ),
        }

        self.assertEqual(
            control_structure,
            ControlStructure(
                frozenset(entities),
                frozenset(control_actions_or_feedbacks),
            ),
        )
