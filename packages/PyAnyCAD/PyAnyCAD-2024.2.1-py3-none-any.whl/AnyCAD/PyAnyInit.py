
import os
import sys

# Initialize the runtime path
_currentPath = os.path.dirname(__file__)
_runtimePath = os.path.abspath(os.path.join(_currentPath, "."))
if os.path.exists(os.path.join(_runtimePath, "_PyAnyCAD.pyd")) == False:
    print("Failed to find AnyCAD Runtime!")
    sys.exit(1)
    
sys.path.append(_currentPath)
sys.path.append(_runtimePath)

print(sys.version)
