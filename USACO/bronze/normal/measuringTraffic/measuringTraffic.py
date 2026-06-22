import sys
sys.stdin = open("measuringTraffic.in", "r")
sys.stdout = open("measuringTraffic.out", "w")

n = int(input())
sensor_readings = []

for _ in range(n):
    attributes = input().split()
    ramp_type = attributes[0]
    low = int(attributes[1])
    high = int(attributes[2])
    sensor_readings.append([ramp_type, low, high])


low = 0
high = 1000000

for sensor_reading in sensor_readings:
    ramp_type = sensor_reading[0]
    a = sensor_reading[1]
    b = sensor_reading[2]
    if ramp_type == "none":
        low = max(a, low)
        high = min(b, high)
    elif ramp_type == "on":
        low += a
        high += b
    elif ramp_type == "off":
        low = max(low-b, 0)
        high = max(high-a, 0)
after_low = low
after_high = high

low = 0
high = 1000000
for sensor_reading in reversed(sensor_readings):
    ramp_type = sensor_reading[0]
    a = sensor_reading[1]
    b = sensor_reading[2]
    if ramp_type == "none":
        low = max(a, low)
        high = min(b, high)
    elif ramp_type == "off":
        low += a
        high += b
    elif ramp_type == "on":
        low = max(low-b, 0)
        high = max(high-a, 0)
before_low = low
before_high = high

print(f"{before_low} {before_high}\n{after_low} {after_high}")