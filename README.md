# SNMP Monitoring Tool with InfluxDB Integration

This project is a Python-based SNMP (Simple Network Management Protocol) monitoring tool that collects data from custom SNMP-enabled devices using the `easysnmp` library. The collected data is then logged into an InfluxDB database for further analysis and visualization.

## Features

- Monitors SNMP-enabled devices for specific OIDs (Object Identifiers).
- Calculates the rate of change for the monitored OIDs over time.
- Integrates with InfluxDB for storing the collected data.
- Customizable sampling interval and number of samples.
- Handles SNMP counter wraparound for accurate rate calculations.

## Requirements

- Python 2.7 or above
- `easysnmp` library for SNMP communication
- `influxdb` library for InfluxDB integration

## Usage

1. Install the required dependencies using pip:

```pip install easysnmp influxdb```
- Run the prober.py script with the following command-line arguments:
  ```python prober.py <hostname:community> <sampling_interval> <sample_count> <oid1> <oid2> ...```
- `<hostname:community>`: SNMP agent hostname and community string (e.g., localhost:public).
- `<sampling_interval>`: Time in seconds between consecutive samples.
- `<sample_count>`: The number of samples to collect. Use -1 for continuous monitoring.
- `<oid1> <oid2> ...`: SNMP Object Identifiers to monitor.
The script will continuously collect data from the specified OIDs and calculate the rate of change for each OID over time. The output will be in the format timestamp|rate1|rate2|..., where timestamp is the Unix timestamp and rate1, rate2, etc., are the calculated rates for the respective OIDs.

The data will be logged into the InfluxDB database specified in the prober.py script. Make sure to configure the InfluxDB settings in the monitor_and_log.py script before running it.

### InfluxDB Integration
The monitor_and_log.py script is responsible for reading the output of the prober.py script, extracting the collected data, and writing it to an InfluxDB database.

### Sample Use Case
Monitor the network interface traffic of a router with the following OIDs:

`ifInOctets` (1.3.6.1.2.1.2.2.1.10)
`ifOutOctets` (1.3.6.1.2.1.2.2.1.16)
``` python prober.py localhost:public 5 -1 1.3.6.1.2.1.2.2.1.10 1.3.6.1.2.1.2.2.1.16 ```
``` python monitor_and_log.py```
The above commands will continuously monitor the specified OIDs on the local SNMP agent, calculate the rates of change for each OID, and log the data into the InfluxDB database for further analysis.

**Note**: The specifics of the SNMP-enabled devices, OIDs, and InfluxDB database configuration should be customized to suit the monitoring requirements.