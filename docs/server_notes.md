# Feed Filter Server
High-performance media analysis server providing real-time OCR, image captioning, and content filtering.

## Quickstart
1. Requirements:
   - Python 3.10+ (older python easier for driver support)
   - CUDA-capable GPU (recommended)
   - CUDA drivers and cuDNN

2. Setup:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   ```

3. Environment Variables:
   ```bash
   # Create .env file with:
   OPENAI_API_KEY=your_key_here
   SERVER_HOST=0.0.0.0
   SERVER_PORT=8000
   ```

4. Model Weights:
   Download required weights to `weights/` directory:
   - `dlip_caption_production.pth` (DLIP model)
   - `craft_mlt_25k.pth` (OCR support)
   - `english_g2.pth` (Text recognition)

5. Launch Server:
   ```bash
   python main.py
   # or for development:
   # uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## Directory Structure
```
server/proto_server/
├── main.py              # FastAPI server entrypoint
├── config.py           # Configuration and environment
├── services/           # Core service implementations
│   ├── caption_service.py    # DLIP image captioning
│   ├── ocr_service.py        # Text extraction
│   └── openai_service.py     # Content analysis
├── models/             # ML model architectures
├── utils/             # Shared utilities
├── configs/           # Model configurations
└── weights/           # Pretrained model weights
```
Forked from https://github.com/jfan1256/distill-blip/tree/main

## Core Services

### 1. DLIP Caption Service
Distilled version of BLIP optimized for social media content:
- 108M parameters (1.9x compression vs BLIP)
- 2.7x faster inference
- 95% accuracy maintenance
- Mixed precision support

### 2. OCR Service (TrOCR)
Microsoft's Transformer-based OCR:
- Vision encoder-decoder architecture
- GPU acceleration with mixed precision
- Async processing pool
- 98.2% benchmark accuracy

### 3. OpenAI Analysis
Content filtering using GPT-4o-mini:
- Rate-limited (5 concurrent requests)
- Async request handling
- Configurable system prompts
- Standardized response format

## Hardware Requirements

### Recommended Specs
- GPU: CUDA-capable with 8GB+ VRAM
- CPU: 4+ cores
- RAM: 8GB minimum
- Storage: 5GB for models

### Reference Hardware
Our production environment uses:
- GPU: 4x 3090s w/ NVLink
- CPU: AMD EPYC 64 core
- RAM: 256GB
- Storage: 2TB SSD

Note: The server can run on smaller hardware with reduced performance.

## Performance Benchmarks
- Processing latency:
  - DLIP caption: ~90ms
  - OCR extraction: ~120ms
  - Content analysis: ~200ms
  - Total: ~300ms
- Throughput: 20 requests/second
- Memory usage: ~2GB under load
- GPU utilization: 60-80%

### Model Details

#### DLIP Architecture
- Vision Encoder:
  - ViT (Vision Transformer)
  - 384 vision width
  - 12 layers, 6 attention heads
  - Gradient checkpointing for memory efficiency

- Text Decoder:
  - BERT-based architecture
  - 6 transformer layers
  - 384 hidden size
  - Cross-attention for image-text fusion

#### OCR Technology
- Microsoft's TrOCR base model
- Vision encoder: ResNet + Transformer
- Text decoder: BERT-based
- Optimized for both printed and handwritten text

#### OpenAI Integration
- Model: GPT-4o-mini
- Purpose: Content analysis and filtering decisions
- Input format: Combined text, OCR, and image captions
- Output: Structured decision with reasoning


#### fyi requirements for venv

Note that CUDA driver support is tricky to get working.

ted@brute:~/Documents/server$ ls
benv  proto_server  requirements.txt

ted@brute:~/Documents/server$ cat requirements.txt
aiohttp>=3.10.10
fastapi>=0.115.4
numpy>=2.1.2
opencv-python>=4.10.0.84
Pillow>=11.0.0
python-dotenv>=1.0.1
python-multipart>=0.0.16
torch>=2.5.1
torchvision>=0.20.1
transformers>=4.46.1
uvicorn>=0.32.0

ted@brute:~/Documents/server$ source benv/bin/activate

(benv) ted@brute:~/Documents/server$ cd proto_server/

(benv) ted@brute:~/Documents/server/proto_server$ python main.py

