VENV := .camtest
PYTHON := python3.12

# Create a virtual environment
$(VENV)/bin/activate: 
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install --upgrade pip  # Upgrade pip

.PHONY: install run clean

# Install package in editable mode
install: $(VENV)/bin/activate
	$(VENV)/bin/pip install -r requirements.txt

# Run the project using the virtual environment
run: install
	$(VENV)/bin/python ptz_cam.py

# Clean up cache and build artifacts
clean:
	rm -rf $(VENV)