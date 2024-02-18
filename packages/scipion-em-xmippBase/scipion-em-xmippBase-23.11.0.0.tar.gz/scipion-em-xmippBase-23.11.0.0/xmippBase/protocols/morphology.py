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
from pyworkflow.protocol.params import (IntParam, StringParam, BooleanParam, FloatParam, EnumParam)
from pwem.protocols import EMProtocol

MORPHOLOGY_DILATION=0
MORPHOLOGY_EROSION=1
MORPHOLOGY_CLOSING=2
MORPHOLOGY_OPENING=3

class Morphology(EMProtocol):
    def addPostprocessingSection(self, form):
        form.addSection(label='Postprocessing')
        form.addParam('doSmall', BooleanParam, default=False,
                      label='Remove small objects',
                      help="To remove small clusters of points. "
                           "The input mask has to be binary.")
        form.addParam('smallSize', IntParam, default=50,
                      label='Minimum size',condition="doSmall",
                      help='Connected components whose size is smaller than '
                           'this number in voxels will be removed')
        form.addParam('doBig', BooleanParam, default=False,
                      label='Keep largest component',
                      help="To keep cluster greater than a given size. The input mask has to be binary")
        form.addParam('doSymmetrize', BooleanParam, default=False,
                      label='Symmetrize mask')
        form.addParam('symmetry', StringParam, default='c1',
                      label='Symmetry group',condition="doSymmetrize",
                      help="To obtain a symmetric mask. See http://xmipp.cnb.csic.es/twiki/bin/view/Xmipp/Symmetry \n"
                           "for a description of the symmetry groups format. \n"
                           "If no symmetry is present, give c1")
        form.addParam('doMorphological', BooleanParam, default=False,
                      label='Apply morphological operation',
                      help="Dilation (dilate white region). \n"
                           "Erosion (erode white region). \n"
                           "Closing (Dilation+Erosion, removes black spots). \n"
                           "Opening (Erosion+Dilation, removes white spots). \n")
        form.addParam('morphologicalOperation', EnumParam, default=MORPHOLOGY_DILATION,
                      condition="doMorphological",
                      choices=['dilation', 'erosion', 'closing', 'opening'],
                      label='Operation')
        form.addParam('elementSize', IntParam, default=1, condition="doMorphological",
                      label='Structural element size',
                      help="The larger this value, the more the effect will be noticed")
        form.addParam('doInvert', BooleanParam, default=False,
                      label='Invert the mask')
        form.addParam('doSmooth', BooleanParam, default=False,
                      label='Smooth borders',
                      help="Smoothing is performed by convolving the mask with a Gaussian.")
        form.addParam('sigmaConvolution', FloatParam, default=2, condition="doSmooth",
                      label='Gaussian sigma (px)',
                      help="The larger this value, the more the effect will be noticed")

    def removeSmallObjects(self, fn, objectSize):
        self.runJob("xmipp_transform_morphology","-i %s --binaryOperation removeSmall %d" % (fn, objectSize))

    def keepBiggest(self, fn):
        self.runJob("xmipp_transform_morphology","-i %s --binaryOperation keepBiggest" % fn)

    def doSymmetrize(self, fn, typeOfSymmetry):
        if typeOfSymmetry!='c1':
            self.runJob("xmipp_transform_symmetrize","-i %s --sym %s --dont_wrap" % (fn, typeOfSymmetry))
            self.runJob("xmipp_transform_threshold", "-i %s --select below 0.5 --substitute binarize" % fn)

    def doMorphological(self, fn, elementSize, typeOfMorphOp):
            self.runJob("xmipp_transform_morphology","-i %s --binaryOperation %s --size %d"
                        % (fn, typeOfMorphOp, elementSize))

    def doInvert(self, fn):
        self.runJob("xmipp_image_operate","-i %s --mult -1" % fn)
        self.runJob("xmipp_image_operate","-i %s --plus  1" % fn)

    def doSmooth(self, fn, sigmaConv):
        self.runJob("xmipp_transform_filter","-i %s --fourier real_gaussian %f" % (fn, sigmaConv))
        self.runJob("xmipp_transform_threshold", "-i %s --select below 0 --substitute value 0" % fn)
