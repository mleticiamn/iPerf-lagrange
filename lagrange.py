import os
import time

def lagrange_interp(x, x_points, y_points):
    n = len(x_points)
    P = 0
    for j in range(n):
        L = 1
        for m in range(n):
            if m != j:
                L *= (x - x_points[m]) / (x_points[j] - x_points[m])
        P += y_points[j] * L
    return P

def gen_traffic(time_points, traffic_levels, duration):
    cur_time = time.localtime().tm_hour + (time.localtime().tm_min/60) + (time.localtime().tm_sec/3600)
    bandwidth = lagrange_interp(cur_time, time_points, traffic_levels)
    
    if bandwidth < 0:
        bandwidth = 0
    if bandwidth > 50:
        bandwidth = 50

    os.system(f"iperf -c 127.0.0.1 -u -b {bandwidth}M -i 1 -t {duration}")
    print(f"\ntraffic interpolated at {cur_time:.2f}h\n")


def main():
    time_points = [6, 9, 12, 15, 18, 21]
    traffic_levels = [5, 20, 50, 30, 40, 10]
    duration = 60
    
    while True:
        gen_traffic(time_points, traffic_levels, duration)
        time.sleep(10) 

if __name__ == '__main__':
    main()
