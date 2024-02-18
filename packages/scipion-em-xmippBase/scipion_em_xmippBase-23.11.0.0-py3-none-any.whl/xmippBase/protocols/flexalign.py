# -*- coding: utf-8 -*-
# **************************************************************************
# *
# * Authors:     Jose Luis Vilas (jlvilas@cnb.csic.es)
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************
from pyworkflow.protocol.params import (IntParam, StringParam, BooleanParam, FloatParam, EnumParam, USE_GPU, GPU_LIST)
import pyworkflow.protocol.constants as cons
from pwem.protocols import EMProtocol

class FlexalignBase(EMProtocol):
    def flexAlignParams(self, form):

        # FlexAlign does not support cropping
        form._paramsDict['Alignment']._paramList.remove('Crop_offsets__px_')
        form._paramsDict['Alignment']._paramList.remove('Crop_dimensions__px_')

        form.addHidden(USE_GPU, BooleanParam, default=True,
                       label="Use GPU for execution",
                       help="This protocol has both CPU and GPU implementation.\
                       Select the one you want to use.")

        form.addHidden(GPU_LIST, StringParam, default='0',
                       expertLevel=cons.LEVEL_ADVANCED,
                       label="Choose GPU IDs",
                       help="Add a list of GPU devices that can be used")

        form.addParam('maxResForCorrelation', FloatParam, default=30,
                       label='Maximum resolution (A)',
                       help="Maximum resolution in A that will be preserved during correlation.")

        form.addParam('doComputePSD', BooleanParam, default=True,
                      label="Compute PSD?",
                      help="If Yes, the protocol will compute PSD for each movie "
                           "before and after the alignment")

        form.addParam('maxShift', IntParam, default=50,
                      expertLevel=cons.LEVEL_ADVANCED,
                      label="Maximum shift (A)",
                      help='Maximum allowed distance (in A) that each '
                           'frame can be shifted with respect to the next.')

        #Local alignment params
        group = form.addGroup('Local alignment')

        group.addParam('doLocalAlignment', BooleanParam, default=True,
                      label="Compute local alignment?",
                      help="If Yes, the protocol will try to determine local shifts, similarly to MotionCor2.")

        group.addParam('autoControlPoints', BooleanParam, default=True,
                      label="Auto control points",
                      expertLevel=cons.LEVEL_ADVANCED,
                      condition='doLocalAlignment',
                      help="If on, protocol will automatically determine necessary number of control points.")
        line = group.addLine('Number of control points',
                    expertLevel=cons.LEVEL_ADVANCED,
                    help='Number of control points use for BSpline.',
                    condition='not autoControlPoints')
        line.addParam('controlPointX', IntParam, default=6, label='X')
        line.addParam('controlPointY', IntParam, default=6, label='Y')
        line.addParam('controlPointT', IntParam, default=5, label='t')

        group.addParam('autoPatches', BooleanParam, default=True,
                      label="Auto patches",
                      expertLevel=cons.LEVEL_ADVANCED,
                      condition='doLocalAlignment',
                      help="If on, protocol will automatically determine necessary number of patches.")
        line = group.addLine('Number of patches',
                    expertLevel=cons.LEVEL_ADVANCED,
                    help='Number of patches used for local alignment.',
                    condition='not autoPatches')
        line.addParam('patchesX', IntParam, default=7, label='X')
        line.addParam('patchesY', IntParam, default=7, label='Y')

        group.addParam('minLocalRes', FloatParam, default=500,
                       expertLevel=cons.LEVEL_ADVANCED,
                       label='Min size of the patch (A)',
                       help="How many A should contain each patch?")

        group.addParam('groupNFrames', IntParam, default=3,
                    expertLevel=cons.LEVEL_ADVANCED,
                    label='Group N frames',
                    help='Group every specified number of frames by adding them together. \
                        The alignment is then performed on the summed frames.',
                    condition='doLocalAlignment')

        form.addSection(label="Gain orientation")
        form.addParam('gainRot', EnumParam,
                      choices=['no rotation', '90 degrees',
                               '180 degrees', '270 degrees'],
                      label="Rotate gain reference:",
                      default=self.NO_ROTATION,
                      display=EnumParam.DISPLAY_COMBO,
                      help="Rotate gain reference counter-clockwise.")

        form.addParam('gainFlip', EnumParam,
                      choices=['no flip', 'upside down', 'left right'],
                      label="Flip gain reference:", default=self.NO_FLIP,
                      display=EnumParam.DISPLAY_COMBO,
                      help="Flip gain reference after rotation. "
                           "For tiff movies, gain is automatically upside-down flipped")

        form.addParallelSection(threads=1, mpi=1)

    def citation(self):
        return ['strelak2020flexalign', 'Strelak2023performance']


