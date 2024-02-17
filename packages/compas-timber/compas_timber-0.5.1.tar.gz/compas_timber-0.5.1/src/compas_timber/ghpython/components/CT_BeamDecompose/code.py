"""Extracts main geometric characteristics of a beam."""

from compas_rhino.conversions import box_to_rhino
from compas_rhino.conversions import frame_to_rhino
from compas_rhino.conversions import line_to_rhino_curve
from ghpythonlib.componentbase import executingcomponent as component
from Grasshopper.Kernel.GH_RuntimeMessageLevel import Warning

from compas_timber.ghpython.ghcomponent_helpers import list_input_valid


class BeamDecompose(component):
    def RunScript(self, Beam):
        if not Beam:
            self.AddRuntimeMessage(Warning, "Input parameter Beam failed to collect data")

        Frame = []
        Centerline = []
        Box = []
        Width = []
        Height = []
        if list_input_valid(self, Beam, "Beam"):
            Frame = [frame_to_rhino(b.frame) for b in Beam]
            Centerline = [line_to_rhino_curve(b.centerline) for b in Beam]
            Box = [box_to_rhino(b.shape) for b in Beam]
            Width = [b.width for b in Beam]
            Height = [b.height for b in Beam]

        return (Frame, Centerline, Box, Width, Height)
