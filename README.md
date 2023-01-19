# Explicitly specifying QoS profiles with the RTI Connext Python API

## Purpose of this example

This repo contains a simple example demonstrating how to create DDS entities (DomainParticipants, DataReaders, etc.) with a specific QoS profile instead of relying on the "default" profile. This is considered best-practice for all DDS applications:
- It is easy to understand the intent of the code from simple inspection.
- "Surprises" caused by other parties chaning which QoS profile is default are eliminated-- the code no longer cares which profile is the default and instead explicitly calls one out. 

This example uses Dynamic Data so that it will be compatible with both the Connext Professional 6.1.1 and 7.0.0 releases.

## Assumptions 

- The `connextdds-py repo` is cloned, built, and installed 
  - https://github.com/rticommunity/connextdds-py
- The `NDDSHOME` environment variable is set for your environment

## Running the example 

```
python3 ./publisher.py -d <Domain ID>
```

```
python3 ./subscriber.py -d <Domain ID>
```
