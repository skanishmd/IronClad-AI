#!/bin/bash
# secure_memory.sh - Iron-Clad Protocol for Mac/Linux
# Usage: ./secure_memory.sh lock   (to hide)
# Usage: ./secure_memory.sh unlock (to show)

ACTION=$1
TARGET_DIR=$(pwd)

if [ "$ACTION" == "lock" ]; then
    echo "Locking and hiding environment..."
    # On Mac, use chflags
    if [[ "$OSTYPE" == "darwin"* ]]; then
        chflags hidden .
    fi
    # Restrict permissions to user only
    chmod 700 .
    echo "Protocol Active."
elif [ "$ACTION" == "unlock" ]; then
    echo "Unlocking environment..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        chflags nohidden .
    fi
    # Restore standard permissions
    chmod 755 .
    echo "Protocol Standby."
else
    echo "Usage: ./secure_memory.sh {lock|unlock}"
fi
