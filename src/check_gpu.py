import torch

def check_gpu():
    print("--- Environment & GPU Test ---")
    print(f"PyTorch Version : {torch.__version__}")
    cuda_ready = torch.cuda.is_available()
    print(f"CUDA Available  : {cuda_ready}")
    
    if cuda_ready:
        print(f"GPU Model       : {torch.cuda.get_device_name(0)}")
        print(f"VRAM Available  : {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f} GB")
        print("\nSUCCESS: Environment is fully configured for GPU training!")
    else:
        print("\nWARNING: CUDA is not available. PyTorch is running on CPU.")

if __name__ == "__main__":
    check_gpu()