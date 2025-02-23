# outline.md

## AI Project Overview

The Python AI server (NVIDIA CUDA + PyTorch) currently runs:
- **Microsoft Optical Character Recognition Model** to get words from image text
- **Visual Language Model (VLM)** for image-to-text image description/caption generation

**Goal**: Improve OCR/image-to-text accuracy and reduce latency.

---

## Primary Task: Fine Tune Microsoft OCR Model

1. **Environment Setup**
   - Get a 101 on python vitual environments and SSH if needed
   - Install tailscale and teamviewer on computer - Ted will authentical your comp for remote access to server
   - Use `requirements.txt` for consistent Python/CUDA/PyTorch versions.
   - Document new libraries and versions carefully, important later for model conversions
   - Note: some stuff can be done local on your computer, but CUDA kernels require NVIDA gpu

2. **Baseline Testing & Benchmarking**
   - Run provided scripts and sample commands (`run_ocr.py`) on test data.
   - Record current accuracy & latency time in miliseconds in excel or gsheet

3. **Fine-Tune / Optimize**
   - Research how to fine tune this model
   - Tweak hyperparameters or other settings to boost accuracy.
   - Track each iteration’s changes & results.
   - Coordinate with ted for GPU training sessions

4. **Documentation & Commits**
   - Keep short notes or commit messages for each step.
   - Push all updates to GitHub (except private VLM-related code).
   - Ted/Chris/Server can all have copies of that git repo

---

## Future AI Tasks:

1. **Compare Alternative OCR Models**
   - Search Hugging Face for potential OCR replacements.
   - Filter by parameter size similar to MsftOCR for accuracy, target newest OCR models from 1/1/2025 or later
   - Convert models to right type (hard, ted can help here)
   - Benchmark and keep careful notes

2. **Explore Other Image-to-Text (VLM) Models**
   - Investigate newest 2025 VLMs on Hugging Face and beyond (may not be anything better)
   - Compare speed vs. accuracy.

3. **Investigate “AI CUDA Engineer”**
   - Research ways to speed up PyTorch with custom CUDA kernels.
   - Potentially integrate if results are promising.

---

## Logistics & Expectations

- **Totally Flexible**: This would just be a side gig - your day job takes priority. Plan for weekly checkins / working sessions
- **Server Access**: SSH credentials for GPU servers (home AI server & you can get access to my o1-pro).
- **Data & Code**:
  - Test images/datasets for OCR baseline.
  - I have example (messy) benchmarking scripts in this repo.
- **Publishing**:
  - Public GitHub repo for your work, except the private VLM. Feel free to use to showcase your AI skills!

---

## Starter Resources

1. **Virtual Env Setup** (note you may need multiple diff virt envs for model conversions):
   ```bash
   brew install python@3.10   # recommend installing homebrew for easy library installs
   cd models
   python3 -m venv .venv
   source .venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt   # starting reqs may need to install a few more things
   ```

2. **Quickstart Command**
   ```bash
   python scripts/run_ocr.py --image_path data/test_images/sample1.png
   ```

3. **Comfirm** script runs successfully on at least one test image

4. **IDE** personally I use mac osx unix shell and vim for file edits. cursor might be good too. but if you have msdos you might consider using Git Bash or doing most of your work on the server which is linux. unix shells are easier than powershell - above commands are unix.

---

## Next Steps

1. Clone this repo and set up the environment.
2. Get tailscale and teamviewer set up and confirm you can remote into the brute server.
3. Run the baseline OCR test and confirm the metrics match our reference.
4. Research fine tuning the OCR and come up with a plan to execute (lets collaborate here)
5. Begin experimenting with fine-tuning and share your findings.

🤖🚀🪐🏆🔫👽🛸🐄🥩🍽️🏋️

