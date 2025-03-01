# STPA

STPA is a Python framework for the digitalization of STPA for real-life systems.
Calculate Cohen's kappa coefficient for definition linkages between the STPA handbook and an LLM.

## Experiments

Calculate metrics on LLM's definition linkages compared to the STPA handbook.

```console
# Chapter 2
python scripts/experiments/linkages.py gpt-4o 42 1 \
    stpa.examples.stpa_handbook.chapter_2.definitions.LOSSES \
    stpa.examples.stpa_handbook.chapter_2.definitions.HAZARDS \
    stpa.examples.stpa_handbook.chapter_2.definitions.SYSTEM_LEVEL_CONSTRAINTS \
    stpa.examples.stpa_handbook.chapter_2.definitions.SUB_HAZARDS \
    stpa.examples.stpa_handbook.chapter_2.definitions.RESPONSIBILITIES \
    stpa.examples.stpa_handbook.chapter_2.definitions.UNSAFE_CONTROL_ACTIONS \
    stpa.examples.stpa_handbook.chapter_2.definitions.CONTROLLER_CONSTRAINTS \
    stpa.examples.stpa_handbook.chapter_2.definitions.SCENARIOS \
    > scripts/experiments/data/chapter-2-linkages.json

# Appendix A: Aircraft
python scripts/experiments/linkages.py gpt-4o 42 1 \
    stpa.examples.stpa_handbook.appendix_a.aircraft.definitions.LOSSES \
    stpa.examples.stpa_handbook.appendix_a.aircraft.definitions.HAZARDS \
    > scripts/experiments/data/appendix-a-aircraft-linkages.json

# Appendix A: Automotive
python scripts/experiments/linkages.py gpt-4o 42 1 \
    stpa.examples.stpa_handbook.appendix_a.automotive.definitions.LOSSES \
    stpa.examples.stpa_handbook.appendix_a.automotive.definitions.HAZARDS \
    > scripts/experiments/data/appendix-a-automotive-linkages.json

# Appendix A: Military Aviation
python scripts/experiments/linkages.py gpt-4o 42 1 \
    stpa.examples.stpa_handbook.appendix_a.military_aviation.definitions.LOSSES \
    stpa.examples.stpa_handbook.appendix_a.military_aviation.definitions.HAZARDS \
    > scripts/experiments/data/appendix-a-military-aviation-linkages.json

# Appendix A: Nuclear Power Plant
python scripts/experiments/linkages.py gpt-4o 42 1 \
    stpa.examples.stpa_handbook.appendix_a.nuclear_power_plant.definitions.LOSSES \
    stpa.examples.stpa_handbook.appendix_a.nuclear_power_plant.definitions.HAZARDS \
    > scripts/experiments/data/appendix-a-nuclear-power-plant-linkages.json

# Appendix A: Radiation Therapy
python scripts/experiments/linkages.py gpt-4o 42 1 \
    stpa.examples.stpa_handbook.appendix_a.radiation_therapy.definitions.LOSSES \
    stpa.examples.stpa_handbook.appendix_a.radiation_therapy.definitions.HAZARDS \
    > scripts/experiments/data/appendix-a-radiation-therapy-linkages.json
```

Synthesize unsafe control actions and scenarios with an LLM.

```console
# Chapter 2
python scripts/experiments/raw-syntheses.py gpt-4o 42 1 \
    50 \
    ./stpa/examples/stpa_handbook/chapter_2/figure-2.12.drawio.png \
    stpa.examples.stpa_handbook.chapter_2.definitions.LOSSES \
    stpa.examples.stpa_handbook.chapter_2.definitions.HAZARDS \
    stpa.examples.stpa_handbook.chapter_2.definitions.SYSTEM_LEVEL_CONSTRAINTS \
    stpa.examples.stpa_handbook.chapter_2.definitions.SUB_HAZARDS \
    stpa.examples.stpa_handbook.chapter_2.definitions.RESPONSIBILITIES \
    stpa.examples.stpa_handbook.chapter_2.definitions.UNSAFE_CONTROL_ACTIONS \
    stpa.examples.stpa_handbook.chapter_2.definitions.CONTROLLER_CONSTRAINTS \
    stpa.examples.stpa_handbook.chapter_2.definitions.SCENARIOS \
    > scripts/experiments/data/chapter-2-raw-syntheses.json
```

Synthesize unsafe control actions and scenarios with an LLM while filtering low-quality and duplicate outputs.

```console
# Chapter 2
python scripts/experiments/filtered-raw-unsafe-control-actions.py gpt-4o gpt-3.5-turbo 42 1 \
    50 \
    ./stpa/examples/stpa_handbook/chapter_2/figure-2.12.drawio.png \
    stpa.examples.stpa_handbook.chapter_2.definitions.LOSSES \
    stpa.examples.stpa_handbook.chapter_2.definitions.HAZARDS \
    stpa.examples.stpa_handbook.chapter_2.definitions.SUB_HAZARDS \
    stpa.examples.stpa_handbook.chapter_2.definitions.UNSAFE_CONTROL_ACTIONS \
    > scripts/experiments/data/chapter-2-filtered-raw-unsafe-control-actions.txt
python scripts/experiments/filtered-raw-scenarios.py gpt-4o gpt-3.5-turbo 42 1 \
    50 \
    ./stpa/examples/stpa_handbook/chapter_2/figure-2.12.drawio.png \
    stpa.examples.stpa_handbook.chapter_2.definitions.LOSSES \
    stpa.examples.stpa_handbook.chapter_2.definitions.HAZARDS \
    stpa.examples.stpa_handbook.chapter_2.definitions.SUB_HAZARDS \
    stpa.examples.stpa_handbook.chapter_2.definitions.UNSAFE_CONTROL_ACTIONS \
    stpa.examples.stpa_handbook.chapter_2.definitions.SCENARIOS \
    >> scripts/experiments/data/chapter-2-filtered-raw-scenarios.txt
```

Create quality annotations.

```console
# Chapter 2
python scripts/experiments/quality-annotations.py gpt-3.5-turbo 42 1 \
    ./stpa/examples/stpa_handbook/chapter_2/figure-2.12.drawio.png \
    scripts/experiments/data/chapter-2-raw-syntheses.json \
    scripts/experiments/data/chapter-2-filtered-raw-unsafe-control-actions.txt \
    scripts/experiments/data/chapter-2-filtered-raw-scenarios.txt \
    scripts/experiments/data/chapter-2-raw-unsafe-control-action-quality-annotations.csv \
    scripts/experiments/data/chapter-2-raw-scenario-quality-annotations.csv \
    stpa.examples.stpa_handbook.chapter_2.definitions.UNSAFE_CONTROL_ACTIONS \
    stpa.examples.stpa_handbook.chapter_2.definitions.SCENARIOS
```

Create equality annotations.

```console
# Chapter 2
python scripts/experiments/raw-equality-annotations.py gpt-3.5-turbo 42 1 \
    scripts/experiments/data/chapter-2-raw-syntheses.json \
    scripts/experiments/data/chapter-2-raw-unsafe-control-action-raw-equality-annotations.csv \
    scripts/experiments/data/chapter-2-raw-scenario-raw-equality-annotations.csv
```
