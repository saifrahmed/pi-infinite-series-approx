import math

STEPS_TO_RUN = 10000000000

def main():
    series_sum = 0
    for s in range(1, STEPS_TO_RUN, 4):
        
        term = 1/s
        next_term = 1/(s+2)
        series_sum += term
        series_sum -= next_term
        approx = series_sum*4
        diff = abs(approx - math.pi)
        if (s-1)%100000 == 0:
            print(f"On step {s:,} we're adding 1/{s} and subtracting 1/{s+2} for approximation {approx:0.15f} and difference {diff:0.15f}")
        
if __name__ == "__main__":
    main()