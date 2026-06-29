import time
import random

# Simulate a simple machine learning model function
def simple_model(input_data):
    # In a real serverless scenario, this function might be deployed
    # and invoked independently. The inconsistency can arise from
    # factors like cold starts, varying memory allocation, or
    # underlying infrastructure variations.

    # Simulate a slight, random variation in processing time
    processing_delay = random.uniform(0.01, 0.1)
    time.sleep(processing_delay)

    # Simulate a minor, random variation in output based on input
    # This is a simplified representation of how subtle differences
    # in execution environment or timing could lead to slightly
    # different results from the same logical operation.
    base_output = sum(input_data) * 1.5
    output_variation = random.uniform(-0.5, 0.5)
    final_output = base_output + output_variation

    return round(final_output, 2)

if __name__ == "__main__":
    sample_input = [10, 20, 30]
    num_inferences = 5

    print(f"Running {num_inferences} inferences with input: {sample_input}")
    print("--- Results ---")

    for i in range(num_inferences):
        # In a serverless environment, each invocation might hit a different
        # instance or have different initialization overhead.
        start_time = time.time()
        result = simple_model(sample_input)
        end_time = time.time()
        duration = round(end_time - start_time, 4)

        print(f"Inference {i+1}: Result = {result}, Duration = {duration}s")

    print("\nObserve that the results and durations may vary slightly between inferences,"
          "demonstrating potential inconsistencies in serverless environments.")
