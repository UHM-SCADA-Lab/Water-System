# Water-System
Contains all code that runs the water system on our SCADA town.

**Control.py**
The python program that controls 2 pumps based on the input from the two sensors in Tank 1. Requires an external relay module.

**rc.local**
Found in the '/etc' directory. Runs the control program upon startup.
