# python_freeathome_local

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/python_freeathome_local?logo=python)
[![PyPI release](https://img.shields.io/pypi/v/python_freeathome_local)](https://pypi.org/project/python_freeathome_local/)
![Release status](https://img.shields.io/pypi/status/python_freeathome_local)
![Build Pipeline](https://img.shields.io/github/actions/workflow/status/derjoerg/python_freeathome_local/ci.yml)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=f8b424)](https://github.com/pre-commit/pre-commit)
![License](https://img.shields.io/github/license/derjoerg/python_freeathome_local)

The datamodel of the Free@Home Rest-API is setup the following way:
- The root-node is a SysAp
- The SysAp contains devices and a floorplan
- Each device has 1 to many channels (the behaviour of a channel is defined by the FunctionID)
- A channel has 0 to many Input- and Output-Datapoints (the behaviour of a datapoint is defined by the PairingID)
- An Input-Datapoint is used to set a value (e.g. turn on a switch)
-- To change the value of an such a datapoint a PUT-call is needed
- An Output-Datapoint shows the current state (e.g. switch is on)
-- All modifications are reported through a websocket-connection
- A device and a channel can have 0 to many parameters (the function of a parameter is defined by the ParameterID)

## Drawback
The major drawback I see so far regarding the Rest-API is that the parameters can't be controlled.
E.g. the WeatherStation has a parameter called 'par0039' (TRANSMISSION_INTERVAL), which defines how often updated values are send. This interval can be changed in the mobile app, but not through the Rest-API, additionally (what is even more worse) any modifications are not reported through the websocket. This means that after the initial load of the configuration any modifications to the parameters through the mobile app are not recognized by this library :(

## Implemented channels
| Name | Inputs | Outputs |
|--|--|--|
| BrightnessSensor | - | brightness_level (float) - state<br>brightness_alarm (bool) |
| RainSensor       | - | rain_alarm (bool) - state<br>rain_sensor_activation_percentage (float)<br>rain_sensor_frequency (float) |
| TemperatureSensor | - | outdoor_temperature (float) - state<br>frost_alarm (bool) |
| WindSensor | - | wind_speed (float) - state<br>wind_alarm (bool)<br>wind_force (float) |
| Trigger | timed_start_stop - press | - |
| SwitchActuator | switch_on_off (bool) - turn_on/turn_off<br>forced (bool)<br>timed_start_stop (bool)<br>timed_movement (bool) | info_on_off (bool) - state<br>info_force (bool)<br>info_error (bool) |
| WindowDoorSensor | - | window_door (bool) - state |
| MovementDetector | info_on_off | info_on_off (bool) - state<br>brightness_level (float)<br>timed_movement (bool)<br>timed_presence (bool) |
| SwitchSensor | - | switch_on_off (bool) - state |
| ForceOnOffSensor | - | forced (bool) - state |
| BlindSensor | - | stop_step_up_down (bool) - state |
| DesDoorRingingSensor | - | timed_start_stop (bool) - state |