import os
import time

import psutil
import pta

if __name__ == "__main__":

    pta.enable_all_logging()
    num_cores = psutil.cpu_count(logical=False)
    num_chains = num_cores
    num_steps = 100e6

    print("============================================================")
    print("   Sampling benchmark started")
    print("============================================================")
    print(f"Benchmark running in process {os.getpid()}")

    # Load test model.
    model = pta.load_example_model("iJO1366")

    # Create the sampling model.
    start_time = time.perf_counter()
    us_model = pta.UniformSamplingModel.from_cobrapy_model(model)
    elapsed_time_1 = time.perf_counter() - start_time

    # Generate initial points for the chains.
    start_time = time.perf_counter()
    initial_points = us_model.get_initial_points(num_chains)
    elapsed_time_2 = time.perf_counter() - start_time

    # Run the sampler.
    start_time = time.perf_counter()
    result = pta.sample_flux_space_uniform(
        us_model,
        num_chains=num_chains,
        initial_points=initial_points,
        max_threads=num_cores,
        num_initial_steps=num_steps,
    )
    elapsed_time_3 = time.perf_counter() - start_time

    print(f" > UniformSamplingModel.from_cobrapy_model():   {elapsed_time_1:.2f}s")
    print(f" > us_model.get_initial_points():               {elapsed_time_2:.2f}s")
    print(f" > sample_flux_space_uniform():                 {elapsed_time_3:.2f}s")
    print("   Sampling benchmark completed")
    print("============================================================")
