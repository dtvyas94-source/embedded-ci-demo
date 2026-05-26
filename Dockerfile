# Step 1 — Start with official Python image from Docker Hub
FROM python:3.10-slim

# Step 2 — Set working directory inside container
WORKDIR /app

# Step 3 — Copy everything from your machine into container
COPY . .

# Step 4 — Install dependencies
RUN pip install pytest

# Step 5 — Run tests when container starts
CMD ["pytest", "tests/", "-v"]