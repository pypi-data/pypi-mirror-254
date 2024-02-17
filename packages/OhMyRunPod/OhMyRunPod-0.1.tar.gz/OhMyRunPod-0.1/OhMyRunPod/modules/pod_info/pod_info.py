import os
import subprocess

def get_pod_info():
    pod_info = {
        "Pod ID": os.getenv("RUNPOD_POD_ID", "Not Available"),
        "Pod RAM (GB)": os.getenv("RUNPOD_MEM_GB", "Not Available"),
        "Public IP": os.getenv("RUNPOD_PUBLIC_IP", "Pod does not have a Public IP"),
        "GPU Count": os.getenv("RUNPOD_GPU_COUNT", "0"),
        "Datacenter ID": os.getenv("RUNPOD_DC_ID", "Not Available"),
        "vCPU Count": os.getenv("RUNPOD_CPU_COUNT", "Not Available"),
    }

    # Warning if GPU count is 0
    gpu_count = pod_info.get("GPU Count", "0")
    if gpu_count == "0":
        pod_info["GPU Count"] = "0 (Warning: Running with 0 GPUs)"

    # Get Maximum CUDA version supported by the host from nvidia-smi
    try:
        nvidia_smi_output = subprocess.check_output(["nvidia-smi"], text=True)
        for line in nvidia_smi_output.split('\n'):
            if "CUDA Version:" in line:
                # Extracting the CUDA version number
                cuda_version = line.split("CUDA Version:")[1].strip()
                pod_info["Maximum CUDA Version Supported by Host"] = cuda_version
                break
    except subprocess.CalledProcessError:
        pod_info["Maximum CUDA Version Supported by Host"] = "Not Available"


    # Get CUDA version from nvcc (Pod specific)
    try:
        nvcc_output = subprocess.check_output(
            ["nvcc", "--version"], text=True
        )
        # Extract CUDA version from nvcc output
        cuda_version_line = nvcc_output.split('\n')[-2]
        cuda_version = cuda_version_line.split()[-1]
        pod_info["CUDA Version of Pod"] = cuda_version
    except subprocess.CalledProcessError:
        pod_info["CUDA Version of Pod"] = "Not Available"

    return pod_info

def print_pod_info():
    info = get_pod_info()
    print("\nPod Information:\n")
    print(f"  - Pod ID: {info['Pod ID']}")
    print(f"  - Pod RAM (GB): {info['Pod RAM (GB)']}")
    print(f"  - Public IP: {info['Public IP']}")
    print(f"  - GPU Count: {info['GPU Count']}")
    print(f"  - vCPU Count: {info['vCPU Count']}")
    print(f"  - Datacenter ID: {info['Datacenter ID']}")
    print(f"  - Maximum CUDA Version Supported by Host (from nvidia-smi): {info['Maximum CUDA Version Supported by Host']}")
    print(f"  - CUDA Version of Pod (from nvcc): {info['CUDA Version of Pod']}\n")

if __name__ == "__main__":
    print_pod_info()
