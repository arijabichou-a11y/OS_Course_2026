#!/bin/bash

# Displaying the system information as per TP requirements
echo "=============================="
echo "SYSTEM INFORMATION"
echo "=============================="

# 1. OS name and kernel version
echo "OS & Kernel: $(uname -a)"

# 2. Current logged-in user
echo "Logged-in User: $(whoami)"

# 3. Current working directory
echo "Current Directory: $(pwd)"

echo "=============================="