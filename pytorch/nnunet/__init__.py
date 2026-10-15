from __future__ import absolute_import
import sys

_citation = (
    "\nPlease cite the following paper when using nnUNet:\nFabian Isensee, Paul F. Jäger, Simon A. A. Kohl, "
    "Jens Petersen, Klaus H. Maier-Hein \"Automated Design of Deep Learning Methods for Biomedical Image "
    "Segmentation\" arXiv preprint arXiv:1904.08128 (2020).\n"
    "If you have questions or suggestions, feel free to open an issue at https://github.com/MIC-DKFZ/nnUNet\n"
)
try:
    print(_citation)
except UnicodeEncodeError:
    encoding = getattr(sys.stdout, "encoding", None) or "utf-8"
    sys.stdout.buffer.write(_citation.encode(encoding, errors="replace"))

from . import *