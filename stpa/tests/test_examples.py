from importlib import import_module
from pathlib import Path
from textwrap import dedent
from unittest import TestCase

from stpa.control_structures import (
    ControlActionOrFeedback,
    ControlStructure,
    ControlType,
    Entity,
)
from stpa.definitions import Definition


class ExamplesTestCase(TestCase):
    def tearDown(self) -> None:
        Definition.clear()


class STPAHandbookExamplesTestCase(ExamplesTestCase):
    pass


class STPAHandbookChapter2ExamplesTestCase(STPAHandbookExamplesTestCase):
    def test_definitions(self) -> None:
        definitions = import_module(
            'stpa.examples.stpa_handbook.chapter_2.definitions',
        )
        losses = definitions.LOSSES
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

        self.assertEqual(len(losses), len(raw_losses))

        for loss, raw_loss in zip(losses, raw_losses):
            self.assertEqual(str(loss), raw_loss)

        hazards = definitions.HAZARDS
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

        self.assertEqual(len(hazards), len(raw_hazards))

        for hazard, raw_hazard in zip(hazards, raw_hazards):
            self.assertEqual(str(hazard), raw_hazard)

        system_level_constraints = definitions.SYSTEM_LEVEL_CONSTRAINTS
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

        self.assertEqual(
            len(system_level_constraints),
            len(raw_system_level_constraints),
        )

        for system_level_constraint, raw_system_level_constraint in zip(
                system_level_constraints,
                raw_system_level_constraints,
        ):
            self.assertEqual(
                str(system_level_constraint),
                raw_system_level_constraint,
            )

        sub_hazards = definitions.SUB_HAZARDS
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

        self.assertCountEqual(sub_hazards.keys(), raw_sub_hazards.keys())

        for key, value in sub_hazards.items():
            self.assertEqual(len(value), len(raw_sub_hazards[key]))

            for sub_hazard, raw_sub_hazard in zip(value, raw_sub_hazards[key]):
                self.assertEqual(str(sub_hazard), raw_sub_hazard)

        responsibilities = definitions.RESPONSIBILITIES
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

        self.assertEqual(len(responsibilities), len(raw_responsibilities))

        for responsibility, raw_responsibility in zip(
                responsibilities,
                raw_responsibilities,
        ):
            self.assertEqual(str(responsibility), raw_responsibility)

        unsafe_control_actions = definitions.UNSAFE_CONTROL_ACTIONS
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

        self.assertEqual(
            len(unsafe_control_actions),
            len(raw_unsafe_control_actions),
        )

        for unsafe_control_action, raw_unsafe_control_action in zip(
                unsafe_control_actions,
                raw_unsafe_control_actions,
        ):
            self.assertEqual(
                str(unsafe_control_action),
                raw_unsafe_control_action,
            )

        controller_constraints = definitions.CONTROLLER_CONSTRAINTS
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

        self.assertEqual(
            len(controller_constraints),
            len(raw_controller_constraints),
        )

        for controller_constraint, raw_controller_constraint in zip(
                controller_constraints,
                raw_controller_constraints,
        ):
            self.assertEqual(
                str(controller_constraint),
                raw_controller_constraint,
            )

        scenarios = definitions.SCENARIOS
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

        self.assertEqual(len(scenarios), len(raw_scenarios))

        for scenario, raw_scenario in zip(scenarios, raw_scenarios):
            self.assertEqual(str(scenario), raw_scenario)

    def test_figure_2_11(self) -> None:
        chapter_2 = import_module('stpa.examples.stpa_handbook.chapter_2')
        pathname = chapter_2.__file__

        assert isinstance(pathname, str)

        path = Path(pathname).parent / 'figure-2.11.drawio.xml'
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


class STPAHandbookAppendixAExamplesTestCase(STPAHandbookExamplesTestCase):
    def test_nuclear_power_plant_definitions(
            self,
    ) -> None:
        definitions = import_module(
            (
                'stpa'
                '.examples'
                '.stpa_handbook'
                '.appendix_a'
                '.nuclear_power_plant'
                '.definitions'
            ),
        )
        losses = definitions.LOSSES
        raw_losses = (
            'L1: People injured or killed',
            'L2: Environment contaminated',
            'L3: Equipment damage (economic loss)',
            'L4: Loss of electrical power generation',
        )

        self.assertEqual(len(losses), len(raw_losses))

        for loss, raw_loss in zip(losses, raw_losses):
            self.assertEqual(str(loss), raw_loss)

        hazards = definitions.HAZARDS
        raw_hazards = (
            'H1: Release of radioactive materials [L1, L2, L3, L4]',
            'H2: Reactor temperature too high [L1, L2, L3, L4]',
            'H3: Equipment operated beyond limits [L3, L4]',
            'H4: Reactor shut down [L4]',
        )

        self.assertEqual(len(hazards), len(raw_hazards))

        for hazard, raw_hazard in zip(hazards, raw_hazards):
            self.assertEqual(str(hazard), raw_hazard)

    def test_aircraft_definitions(self) -> None:
        definitions = import_module(
            (
                'stpa'
                '.examples'
                '.stpa_handbook'
                '.appendix_a'
                '.aircraft'
                '.definitions'
            ),
        )
        losses = definitions.LOSSES
        raw_losses = (
            'L1: Loss of life or serious injury to people',
            'L2: Damage to the aircraft or objects outside the aircraft',
        )

        self.assertEqual(len(losses), len(raw_losses))

        for loss, raw_loss in zip(losses, raw_losses):
            self.assertEqual(str(loss), raw_loss)

        hazards = definitions.HAZARDS
        raw_hazards = (
            (
                'H-1: Aircraft violate minimum separation standards in flight'
                ' [L1, L2]'
            ),
            'H-2: Controlled flight of aircraft into terrain [L1, L2]',
            'H-3: Loss of aircraft control [L1, L2]',
            'H-4: Aircraft airframe integrity is lost [L1, L2]',
            'H-5: Aircraft environment is harmful to human health [L1, L2]',
            (
                'H-6: Aircraft departs designated taxiway, runway, or apron on'
                ' ground [L1, L2]'
            ),
            (
                'H-7: Aircraft comes too close to other objects on the ground'
                ' [L1, L2]'
            ),
        )

        self.assertEqual(len(hazards), len(raw_hazards))

        for hazard, raw_hazard in zip(hazards, raw_hazards):
            self.assertEqual(str(hazard), raw_hazard)

    def test_radiation_therapy_definitions(
            self,
    ) -> None:
        definitions = import_module(
            (
                'stpa'
                '.examples'
                '.stpa_handbook'
                '.appendix_a'
                '.radiation_therapy'
                '.definitions'
            ),
        )
        losses = definitions.LOSSES
        raw_losses = (
            (
                'L1: The patient is injured or killed from overexposure or'
                ' undertreatment.'
            ),
            'L2: A nonpatient is injured or killed by radiation.',
            'L3: Damage or loss of equipment.',
            'L4: Physical injury to a patient or nonpatient during treatment.',
        )

        self.assertEqual(len(losses), len(raw_losses))

        for loss, raw_loss in zip(losses, raw_losses):
            self.assertEqual(str(loss), raw_loss)

        hazards = definitions.HAZARDS
        raw_hazards = (
            (
                'H1: Wrong dose: Dose delivered to patient is wrong in either'
                ' amount, location, or timing [L1]'
            ),
            'H2: A nonpatient is unnecessarily exposed to radiation [L2]',
            'H3: Equipment is subject to unnecessary stress [L3]',
            'H4: Persons are subjected to nonradiological injury [L4]',
        )

        self.assertEqual(len(hazards), len(raw_hazards))

        for hazard, raw_hazard in zip(hazards, raw_hazards):
            self.assertEqual(str(hazard), raw_hazard)

        sub_hazards = definitions.SUB_HAZARDS
        raw_sub_hazards = {
            'H1': (
                'H1a: Right patient, right dose, wrong location.',
                'H1b: Right patient, wrong dose, right location.',
                'H1c: Right patient, wrong dose, wrong location.',
                'H1d: Wrong patient.',
            )
        }

        self.assertCountEqual(sub_hazards.keys(), raw_sub_hazards.keys())

        for key, value in sub_hazards.items():
            self.assertEqual(len(value), len(raw_sub_hazards[key]))

            for sub_hazard, raw_sub_hazard in zip(value, raw_sub_hazards[key]):
                self.assertEqual(str(sub_hazard), raw_sub_hazard)

    def test_military_aviation_definitions(
            self,
    ) -> None:
        definitions = import_module(
            (
                'stpa'
                '.examples'
                '.stpa_handbook'
                '.appendix_a'
                '.military_aviation'
                '.definitions'
            ),
        )
        losses = definitions.LOSSES
        raw_losses = (
            (
                'M-1: Loss of or damage to the aircraft or equipment on the'
                ' aircraft'
            ),
            'M-2: Serious injury or fatality to personnel',
            'M-3: Inability to complete the mission',
        )

        self.assertEqual(len(losses), len(raw_losses))

        for loss, raw_loss in zip(losses, raw_losses):
            self.assertEqual(str(loss), raw_loss)

        hazards = definitions.HAZARDS
        raw_hazards = (
            (
                'H-1: Violation of minimum separation standards from fixed or'
                ' moving objects [M-1, M-2, M-3]'
            ),
            'H-2: Inability to control the aircraft [M-1, M-2, M-3]',
            'H-3: Loss of airframe integrity [M-1, M-2, M-3]',
            'H-4: Uncommanded detonation [M-1, M-2, M-3]',
            'H-5: Uncommanded launch [M-1, M-2, M-3]',
            'H-6: Collateral damage or friendly fire [M-1, M-2, M-3]',
            (
                'H-7: Non-deployment (detonation and/or launch) of ordinance'
                ' when commanded [M-3]'
            ),
        )

        self.assertEqual(len(hazards), len(raw_hazards))

        for hazard, raw_hazard in zip(hazards, raw_hazards):
            self.assertEqual(str(hazard), raw_hazard)

    def test_automotive_definitions(self) -> None:
        definitions = import_module(
            'stpa.examples.stpa_handbook.appendix_a.automotive.definitions',
        )
        losses = definitions.LOSSES
        raw_losses = (
            'L1: Loss of life or serious injury to people',
            'L2: Damage to the vehicle or objects outside the vehicle',
        )

        self.assertEqual(len(losses), len(raw_losses))

        for loss, raw_loss in zip(losses, raw_losses):
            self.assertEqual(str(loss), raw_loss)

        hazards = definitions.HAZARDS
        raw_hazards = (
            (
                'H1: Vehicle does not maintain safe distance from nearby'
                ' objects [L1, L2]'
            ),
            'H2: Vehicle enters dangerous area/region [L1, L2]',
            (
                'H3: Vehicle exceeds safe operating envelope for environment'
                ' (speed, lateral/longitudinal forces) [L1, L2]'
            ),
            (
                'H4: Vehicle occupants exposed to harmful effects and/or'
                ' health hazards (e.g. fire, excessive temperature, inability'
                ' to escape, door closes on passengers, etc.) [L1, L2]'
            ),
        )

        self.assertEqual(len(hazards), len(raw_hazards))

        for hazard, raw_hazard in zip(hazards, raw_hazards):
            self.assertEqual(str(hazard), raw_hazard)


class STPAHandbookAppendixCExamplesTestCase(STPAHandbookExamplesTestCase):
    def test_automotive_auto_hold_system_definitions(
            self,
    ) -> None:
        definitions = import_module(
            (
                'stpa'
                '.examples'
                '.stpa_handbook'
                '.appendix_c'
                '.automotive_auto_hold_system'
                '.definitions'
            ),
        )
        unsafe_control_actions = definitions.UNSAFE_CONTROL_ACTIONS
        raw_unsafe_control_actions = (
            (
                'UCA-AH-1: AH does not provide HOLD when vehicle stops and'
                ' brake pedal released [H-1, H-2]'
            ),
            (
                'UCA-AH-2: AH provides HOLD when driver is applying the'
                ' accelerator [H-1]'
            ),
            'UCA-AH-3: AH provides HOLD when AH is DISABLED [H-1]',
            'UCA-AH-4: AH provides HOLD when vehicle is moving [H-1]',
            (
                'UCA-AH-5: AH provides HOLD when driver is not applying'
                ' brake [H-1, H-2]'
            ),
            (
                'UCA-AH-6: AH provides HOLD too early before the required time'
                ' at rest has not been met [H-1]'
            ),
            (
                'UCA-AH-7: AH provides HOLD too late after vehicle stops,'
                ' begins to roll [H-1]'
            ),
            (
                'UCA-AH-10: AH does not provide RELEASE when driver applies'
                ' accelerator pedal [H-1, H-2]'
            ),
            (
                'UCA-AH-12: AH provides RELEASE when driver is not applying'
                ' accelerator [H-1, H-2]'
            ),
            (
                'UCA-AH-13: AH provides RELEASE too early before there is'
                ' sufficient wheel torque [H-1, H-2]'
            ),
            (
                'UCA-AH-13: AH provides RELEASE too late after accelerator'
                ' applied, engine torque exceeds wheel torque [H-1, H-2]'
            ),
            (
                'UCA-AH-14: AH does not provide ADDITIONALPRESSURE when'
                ' vehicle is slipping and AH is active [H-1, H-2]'
            ),
            (
                'UCA-AH-15: AH provides ADDITIONALPRESSURE when AH is not'
                ' active [H-1, H-2]'
            ),
            (
                'UCA-AH-16: AH provides ADDITIONALPRESSURE when brake system'
                ' specs are exceeded [H-1, H-2]'
            ),
            (
                'UCA-AH-16: AH provides ADDITIONAL-PRESSURE too late after'
                ' vehicle is slipping [H-1, H-2]'
            ),
        )

        self.assertEqual(
            len(unsafe_control_actions),
            len(raw_unsafe_control_actions),
        )

        for unsafe_control_action, raw_unsafe_control_action in zip(
                unsafe_control_actions,
                raw_unsafe_control_actions,
        ):
            self.assertEqual(
                str(unsafe_control_action),
                raw_unsafe_control_action,
            )

    def test_autonomous_h_ii_transfer_vehicle_operations_definitions(
            self,
    ) -> None:
        definitions = import_module(
            (
                'stpa'
                '.examples'
                '.stpa_handbook'
                '.appendix_c'
                '.autonomous_h_ii_transfer_vehicle_operations'
                '.definitions'
            ),
        )
        unsafe_control_actions = definitions.UNSAFE_CONTROL_ACTIONS
        raw_unsafe_control_actions = (
            (
                'UCA-HTV-1: ISS crew does not provide Abort Cmd when emergency'
                ' condition exists [H-1]'
            ),
            (
                'UCA-HTV-2: ISS crew provides Abort Cmd when HTV is captured'
                ' [H-1]'
            ),
            (
                'UCA-HTV-3: ISS crew provides Abort Cmd when ISS is in Abort'
                ' path [H-1]'
            ),
            (
                'UCA-HTV-4: ISS crew provides Abort Cmd too late to avoid'
                ' collision [H-1]'
            ),
            (
                'UCA-HTV-5: ISS crew provides Abort Cmd too early before'
                ' capture is released [H-1]'
            ),
            (
                'UCA-HTV-6: ISS crew does not provide Free Drift Cmd when HTV'
                ' is stopped in capture box [H-1]'
            ),
            (
                'UCA-HTV-7: ISS crew provides Free Drift Cmd when HTV is'
                ' approaching ISS [H-1]'
            ),
            (
                'UCA-HTV-8: ISS crew provides Free Drift Cmd too late, more'
                ' than X minutes after HTV stops [H-1]'
            ),
            (
                'UCA-HTV-9: ISS crew provides Free Drift Cmd too early before'
                ' HTV stops [H-1]'
            ),
            (
                'UCA-HTV-10: ISS crew does not perform Capture when HTV is in'
                ' capture box in free drift [H-1]'
            ),
            (
                'UCA-HTV-11: ISS crew performs Capture when HTV is not in free'
                ' drift [H-1]'
            ),
            'UCA-HTV-12: ISS crew performs Capture when HTV is aborting [H-1]',
            (
                'UCA-HTV-13: ISS crew performs Capture with'
                ' excessive/insufficient movement (can impact HTV, cause'
                ' collision course) [H-1]'
            ),
            (
                'UCA-HTV-14: ISS crew performs Capture too late, more than X'
                ' minutes after HTV deactivated [H-1]'
            ),
            (
                'UCA-HTV-15: ISS crew performs Capture too early before HTV'
                ' deactivated [H-1]'
            ),
            (
                'UCA-HTV-16: ISS crew continues performing Capture too long'
                ' after emergency condition exists [H-1]'
            ),
        )

        self.assertEqual(
            len(unsafe_control_actions),
            len(raw_unsafe_control_actions),
        )

        for unsafe_control_action, raw_unsafe_control_action in zip(
                unsafe_control_actions,
                raw_unsafe_control_actions,
        ):
            self.assertEqual(
                str(unsafe_control_action),
                raw_unsafe_control_action,
            )

    def test_wheel_braking_system_aircraft_flight_crew_definitions(
            self,
    ) -> None:
        definitions = import_module(
            (
                'stpa'
                '.examples'
                '.stpa_handbook'
                '.appendix_c'
                '.wheel_braking_system_aircraft_flight_crew'
                '.definitions'
            ),
        )
        unsafe_control_actions = definitions.UNSAFE_CONTROL_ACTIONS
        raw_unsafe_control_actions = (
            (
                'CREW.1a1: Crew does not provide manual braking during'
                ' landing, RTO, or taxiing when Autobrake is not providing'
                ' braking or is providing insufficient braking [H4.1]'
            ),
            (
                'CREW.1b1: Crew provides manual braking with insufficient'
                ' pedal pressure [H4.1]'
            ),
            (
                'CREW.1b2: Crew provides manual braking with excessive pedal'
                ' pressure (resulting in loss of control, passenger/crew'
                ' injury, brake overheating, brake fade or tire burst during'
                ' landing) [H4-1, H4-5]'
            ),
            (
                'CREW.1b3: Crew provides manual braking provided during normal'
                ' takeoff [H4-2, H4-5]'
            ),
            (
                'CREW.1c1: Crew provides manual braking before touchdown'
                ' (causes wheel lockup, loss of control, tire burst) [H4.1]'
            ),
            (
                'CREW.1c2: Crew provides manual braking too late (TBD) to'
                ' avoid collision or conflict with another object (can'
                ' overload braking capability given aircraft weight, speed,'
                ' distance to object (conflict), and tarmac conditions) [H4-1,'
                ' H4-5]'
            ),
            (
                'CREW.1d1: Crew stops providing manual braking command before'
                ' safe taxi speed (TBD) is reached [H4.1, H4.4]'
            ),
            (
                'CREW.1d2: Crew provides manual braking too long (resulting in'
                ' stopped aircraft on runway or active taxiway) [H4-1]'
            ),
            (
                'CREW.2a1: Crew does not arm Autobrake before landing (causing'
                ' loss of automatic brake operation when spoilers deploy. Crew'
                ' reaction time may lead to overshoot.) [H4-1, H4-5]'
            ),
            (
                'CREW.2a2: Crew does not arm Autobrake prior to takeoff'
                ' (resulting in insufficient braking during rejected takeoff,'
                ' assuming that Autobrake is responsible for braking during'
                ' RTO after crew throttle down) [H4-2]'
            ),
            (
                'CREW.2b1: Crew does not arm Autobrake to maximum level during'
                ' takeoff. (assumes that maximum braking force is necessary'
                ' for rejected takeoff) [H4-2]'
            ),
            (
                'CREW.2b2: Crew armed autobrake with too high of a'
                ' deceleration rate for runway conditions (resulting in loss'
                ' of control and passenger or crew injury). [H4-1, H4-5]'
            ),
            (
                'CREW.2c1: Crew provides arm command too late (TBD) (resulting'
                ' in insufficient time for BSCU to apply brakes) [H4-1, H4-5]'
            ),
            (
                'CREW.3a1: Crew does not disarm Autobrake during TOGA'
                ' (resulting in loss of acceleration during (re)takeoff)'
                ' [H4-1, H4-2, H4-5]'
            ),
            (
                'CREW.3b1: Crew disarms Autobrake during landing or RTO'
                ' (resulting in loss of automatic brake operation when'
                ' spoilers deploy. Crew reaction time may lead to overshoot)'
                ' [H4-1, H4-5]'
            ),
            (
                'CREW.3c1: Crew disarms Autobrake more than TBD seconds after'
                ' (a) aircraft descent exceeds TBD fps, (b) visibility is less'
                ' than TBD ft, (c) etc…, (resulting in either loss of control'
                ' of aircraft or loss of acceleration during (re)takeoff)'
                ' [H4-1, H4-2, H4-5]'
            ),
            (
                'CREW.4a1: Crew does not power off BSCU in the event of'
                ' abnormal WBS behavior (needed to enable alternate braking'
                ' mode) [H4-1, H4-2, H4-5]'
            ),
            (
                'CREW.4b1: Crew powers off BSCU when Autobraking is needed and'
                ' WBS functioning normally [H4-1, H4-5]'
            ),
            (
                'CREW.4b2: Crew powers off BSCU when Autobrake is needed (or'
                ' about to be used) and WBS if funtioning normally [H4-1,'
                ' H4-5]'
            ),
            (
                'CREW.4b3: Crew powers off BSCU when Anti-Skid functionality'
                ' is needed (or will be needed) and WBS is functioning'
                ' normally [H4-1, H4-5]'
            ),
            (
                'CREW.4c1: Crew powers off BSCU too late (TBD) to enable'
                ' alternate braking mode in the event of abnormal WBS behavior'
                ' [H4-1, H4-5]'
            ),
            (
                'CREW.4c2: Crew powers off BSCU too early before Autobrake or'
                ' Anti-Skid behavior is completed when it is needed [H4-1,'
                ' H4-5]'
            ),
            (
                'CREW.5a1: Crew does not power on BSCU when Normal braking'
                ' mode, Autobrake, or Anti-Skid is to be used and WBS'
                ' functioning normally [H4-1, H4-5]'
            ),
            (
                'CREW.5c1: Crew powers on BSCU too late after Normal braking'
                ' mode, Autobrake, or Anti-Skid is needed [H4-1, H4-5]'
            ),
        )

        self.assertEqual(
            len(unsafe_control_actions),
            len(raw_unsafe_control_actions),
        )

        for unsafe_control_action, raw_unsafe_control_action in zip(
                unsafe_control_actions,
                raw_unsafe_control_actions,
        ):
            self.assertEqual(
                str(unsafe_control_action),
                raw_unsafe_control_action,
            )

    def test_aircraft_brake_system_control_unit_autobrake_definitions(
            self,
    ) -> None:
        definitions = import_module(
            (
                'stpa'
                '.examples'
                '.stpa_handbook'
                '.appendix_c'
                '.aircraft_brake_system_control_unit_autobrake'
                '.definitions'
            ),
        )
        unsafe_control_actions = definitions.UNSAFE_CONTROL_ACTIONS
        raw_unsafe_control_actions = (
            (
                'BSCU.1a1: Autobrake does not provide Brake command during RTO'
                ' to V1 (resulting in inability to stop within available'
                ' runway length) [H4-1, H4-5]'
            ),
            (
                'BSCU.1a2: Autobrake does not provides Brake command during'
                ' landing roll when BSCU is armed (resulting in insufficient'
                ' deceleration and potential overshoot) [H4-1, H4-5]'
            ),
            (
                'BSCU.1a4: Autobrake does not provide Brake command after'
                ' takeoff (needed to lock wheels, results in potential'
                ' equipment damage during landing gear retraction or wheel'
                ' rotation in flight) [H4-6]'
            ),
            (
                'BSCU.1b1: Autobrake provides excessive Braking commands'
                ' during landing roll [H4-1, H4-5]'
            ),
            (
                'BSCU.1b2: Autobrake provides Braking command inappropriately'
                ' during takeoff (resulting in inadequate acceleration) [H4-1,'
                ' H4-2, H4-5]'
            ),
            (
                'BSCU.1b3: Autobrake provides Brake command with insufficient'
                ' level (resulting in insufficient deceleration during landing'
                ' roll) [H4-1, H4-5]'
            ),
            (
                'BSCU.1c1: Autobrake provides Braking command before touchdown'
                ' (resulting in tire burst, loss of control, injury, other'
                ' damage) [H4-1, H4-5]'
            ),
            (
                'BSCU.1c2: Autobrake provides Brake command more than TBD'
                ' seconds after touchdown (resulting in insufficient'
                ' deceleration and potential loss of control, overshoot)'
                ' [H4-1, H4-5]'
            ),
            (
                'BSCU.1c3: Autobrake provides Brake command at any time before'
                ' wheels have left ground and RTO has not been requested'
                ' (brake might be applied to stop wheels before gear'
                ' retraction) [H4-1, H4-2, H4-5]'
            ),
            (
                'BSCU.1c4: Autobrake provides Brake more than TBD seconds'
                ' after V1 during rejected takeoff (assumes that Autobrake is'
                ' responsible for braking during RTO after crew throttle down)'
                ' [H4-2]'
            ),
            (
                'BSCU.1d1: Autobrake stops providing Brake during landing roll'
                ' before TBD taxi speed attained (causing reduced'
                ' deceleration) [H4-1, H4-5]'
            ),
            (
                'BSCU.1d2: Autobrake provides Brake command too long (more'
                ' than TBD seconds) during landing roll (causing stop on'
                ' runway) [H4-1]'
            ),
            (
                'BSCU.1d3: Autobrake provides Brake command for tire lock'
                ' until less than TBD seconds before touchdown during approach'
                ' (resulting in loss of control, equipment damage) [H4-1,'
                ' H4-5]'
            ),
        )

        self.assertEqual(
            len(unsafe_control_actions),
            len(raw_unsafe_control_actions),
        )

        for unsafe_control_action, raw_unsafe_control_action in zip(
                unsafe_control_actions,
                raw_unsafe_control_actions,
        ):
            self.assertEqual(
                str(unsafe_control_action),
                raw_unsafe_control_action,
            )
