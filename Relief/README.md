## Relief of substrates

A python script for Rhino used to determine absolute relief of any size area of substrate.

#### Use
The Rhino command "RunPythonScript" allows the .py file to be selected, which then asks the user to select the helper (or user-made) mesh cubes and model mesh. The script has no in-built size scales, so can be used with the 2 provided cube sizes or by any other scale.

Relief will print in the command bar. Units are those set for the model.

#### Assumptions
The script assumes that the model is orientated correctly on all axis. Models can be moved using the Rhino command "Rotate" to correctly align them to match their *in-situ* environment.
