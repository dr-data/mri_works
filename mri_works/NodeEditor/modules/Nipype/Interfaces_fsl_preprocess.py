class fsl_FAST:
    def __init__(self, in_files=['path'], **options):
        from nipype.interfaces import fsl
        fastr = fsl.FAST()
        fastr.inputs.in_files = in_files
        for ef in options:
            setattr(fastr.inputs, ef, options[ef])
        self.res = fastr.run()

    def tissue_class_map(self: 'path'):
        return self.res.outputs.tissue_class_map

    def tissue_class_files(self: 'list_path'):
        return self.res.outputs.tissue_class_files

    def restored_image(self: 'list_path'):
        return self.res.outputs.restored_image

    def mixeltype(self: 'path'):
        return self.res.outputs.mixeltype

    def partial_volume_map(self: 'path'):
        return self.res.outputs.partial_volume_map

    def partial_volume_files(self: 'list_path'):
        return self.res.outputs.partial_volume_files

    def bias_field(self: 'list_path'):
        return self.res.outputs.bias_field

    def probability_maps(self: 'list_path'):
        return self.res.outputs.probability_maps

##############################################################################


class fsl_BET:

    def __init__(self, in_file='path', **options):
        from nipype.interfaces import fsl
        btr = fsl.BET()
        btr.inputs.in_file = in_file
        for ef in options:
            setattr(btr.inputs, ef, options[ef])
        self.res = btr.run()

    def out_file(self: 'path'):
        return self.res.outputs.out_file

    def mask_file(self: 'path'):
        return self.res.outputs.mask_file

    def outline_file(self: 'path'):
        return self.res.outputs.outline_file

    def meshfile(self: 'path'):
        return self.res.outputs.meshfile

    def inskull_mask_file(self: 'path'):
        return self.res.outputs.inskull_mask_file

    def inskull_mesh_file(self: 'path'):
        return self.res.outputs.inskull_mesh_file

    def outskull_mask_file(self: 'path'):
        return self.res.outputs.outskull_mask_file

    def outskull_mesh_file(self: 'path'):
        return self.res.outputs.outskull_mesh_file

    def outskin_mask_file(self: 'path'):
        return self.res.outputs.outskin_mask_file

    def outskin_mesh_file(self: 'path'):
        return self.res.outputs.outskin_mesh_file

    def skull_mask_file(self: 'path'):
        return self.res.outputs.skull_mask_file
