# -------------------------
# 1) Base image: includes Python & FFmpeg
# -------------------------
  FROM python:3.12-alpine as base

  # Install FFmpeg (minimal installation)
  RUN apk add --no-cache ffmpeg
  
  # Setup a working directory
  WORKDIR /app
  
  # Ensure local Python installs are on PATH
  ENV PATH="/root/.local/bin:${PATH}"
  
  # -------------------------
  # 2) Builder image: install build tools & Python deps
  # -------------------------
  FROM base as builder
  
  # Install build dependencies for any packages that need compilation
  RUN apk add --no-cache gcc musl-dev
  
  # Copy requirements and install packages as a non-system user (to /root/.local)
  COPY requirements.txt .
  RUN pip install --user --no-cache-dir --upgrade pip \
      && pip install --user --no-cache-dir -r requirements.txt
  
  # Copy the entire project into the builder image
  COPY . .
  
  # -------------------------
  # 3) Final runtime image: only includes what's needed to run
  # -------------------------
  FROM base as final
  
  # Copy installed dependencies from builder
  COPY --from=builder /root/.local /root/.local
  
  # Copy only necessary project files (e.g., exclude tests, docs, etc.)
  COPY app ./app
  
  # Expose port 8000 for FastAPI
  EXPOSE 8000
  
  # Set the default command to run the FastAPI app with Uvicorn
  CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]