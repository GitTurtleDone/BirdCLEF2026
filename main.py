import torch
def main():
    print("Hello from birdclef2026!")
    print((f"Torch version: {torch.__version__}"))
    if torch.cuda.is_available():
        print(f"✅ GPU Found: {torch.cuda.get_device_name(0)}") 
    else:
        print("❌ GPU not found. Running on CPU.")

if __name__ == "__main__":
    main()
