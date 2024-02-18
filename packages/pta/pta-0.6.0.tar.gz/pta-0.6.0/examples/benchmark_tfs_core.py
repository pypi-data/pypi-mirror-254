import os
import time

import enkie
import psutil

import pta
from pta.sampling.tfs import TFSModel, sample_drg

if __name__ == "__main__":

    pta.enable_all_logging()
    num_cores = psutil.cpu_count(logical=False)
    num_chains = num_cores * 4
    num_steps = 100e6

    print("============================================================")
    print("   Sampling benchmark started")
    print("============================================================")
    print(f"Benchmark running in process {os.getpid()}")

    # Load test model.
    model = pta.load_example_model("e_coli_core")
    model.reactions.BIOMASS_Ecoli_core_w_GAM.lower_bound = 0.5

    # Prepare the model for PTA.
    start_time = time.perf_counter()
    pta.prepare_for_pta(model)
    elapsed_time_1 = time.perf_counter() - start_time

    # Create the thermodynamic space.
    start_time = time.perf_counter()
    thermodynamic_space = pta.ThermodynamicSpace.from_cobrapy_model(
        model, parameters=enkie.CompartmentParameters.load("e_coli")
    )
    elapsed_time_2 = time.perf_counter() - start_time

    tfs_model = TFSModel(model, thermodynamic_space, solver="GUROBI")

    # Generate initial points for the chains.
    start_time = time.perf_counter()
    initial_points = tfs_model.get_initial_points(num_chains)
    elapsed_time_3 = time.perf_counter() - start_time

    # Run the sampler.
    start_time = time.perf_counter()
    result = sample_drg(
        tfs_model,
        initial_points=initial_points,
        num_chains=num_chains,
        num_initial_steps=num_steps,
    )
    elapsed_time_4 = time.perf_counter() - start_time

    print(f" > prepare_for_pta():                       {elapsed_time_1:.2f}s")
    print(f" > ThermodynamicSpace.from_cobrapy_model(): {elapsed_time_2:.2f}s")
    print(f" > get_initial_points():                    {elapsed_time_3:.2f}s")
    print(f" > sample_drg():                            {elapsed_time_4:.2f}s")
    print("   Sampling benchmark completed")
    print("============================================================")
