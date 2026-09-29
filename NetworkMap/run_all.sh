#!/bin/bash

# Navigate to the NetworkMapProject directory
cd projects/NetworkMap

# Install dependencies
pip install -r requirements.txt

# Run the network scanner
python network_scanner.py

# Display results in index.html (placeholder - needs further implementation)

# Example:  (This is just a placeholder for where the scan results would be displayed)
# echo "Scan results here..."

exit 0