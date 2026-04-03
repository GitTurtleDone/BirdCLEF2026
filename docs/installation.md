# 🐦 BirdCLEF 2026: Setup & Data Guide

This guide covers the local development setup in **WSL2** using **uv** for high-performance environment management.

## 1. Prerequisites
- **WSL2** (Ubuntu/Debian recommended)
- **NVIDIA GPU** (Optional, but recommended for training)
- **uv** installed (`curl -LsSf https://astral.sh | sh`)
- Have a **Kaggle** acount
## 2. Join the competion in the web broswer
- Go to the competition page: https://www.kaggle.com/competitions/birdclef-2026
- Click the competition button. Sign in if requested.
## 3. Project Initialisation
Clone the repository and initialise the environment:
```bash
# Clone and enter directory
uv init BirdCLEF2026 
cd BirdCLEF2026

# Add necessary packages
uv add torch torchvision torchaudio mlflow fastapi kaggle ipykernel # adding ipykernel to be able to run jupyter notebook


# Initialise uv and sync dependencies
uv sync
```
## 4. Create a respository in GitHub
- Go to GitHub and create a new repository named `BirdCLEF2026`
  Notes: do NOT add README.md and .gitignore, which are already added by uv
- in local terminal add the newly created repositiory with:
```bash
git remote add origin git@github.com:GitTurtleDone/BirdCLEF2026.git
# Add /models, /data, /runs to .gitignore
- git add
- git commit
- git push
```
## 5. Kaggle API Setup
### 1. Get API Key:
    - Go to Kaggle Settings
    - Scroll to API and click "Generate New Token"
    - Copy the generated key.
### 2. Export username and key:
    ```bash
    # Add these 2 lines to the ~/.bashrc
    export KAGGLE_USERNAME=<your_username>
    export KAGGLE_API_KEY=<your_key>
    # then in WSL2 terminal:   
    source ~/.bashrc
    #run 
    uv run kaggle competions list 
    #and check that reponses contain .ogg and .txt files
    ```
## 6. Downloading the data set
Use the Kaggle API to download the dataset:
```bash
uv run kaggle competitions download -c birdclef-2026
```