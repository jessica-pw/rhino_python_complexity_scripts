import rhinoscriptsyntax as rs

### Split cube into concave and convex halves ###

box = rs.GetObject("Select cube to be split", rs.filter.mesh)
if box:
    model = rs.GetObject("Select model to be cut along", rs.filter.mesh)
    if model: rs.MeshBooleanSplit(box, model)


### Create bounding box around each half of split cube to get relief ###

object_1 = rs.GetObject("Select top half of cube in front view")
object_2 = rs.GetObject("Select bottom cube half in front view")

bb_1 = rs.BoundingBox(object_1, view_or_plane=None, in_world_coords=True)
bb_1_height = bb_1[4].Z - bb_1[0].Z

bb_2 = rs.BoundingBox(object_2, view_or_plane=None, in_world_coords=True)
bb_2_height = bb_2[4].Z - bb_2[0].Z

relief_1 = bb_1_height - bb_2_height

print "Model relief is:", abs(relief_1)