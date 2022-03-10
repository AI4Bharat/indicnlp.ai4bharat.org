# The path to the local git repo for Indic NLP library
INDIC_NLP_LIB_HOME="/share03/draj/data/monolingual_corpora/indic/xsum/indic_nlp_library"

# The path to the local git repo for Indic NLP Resources
INDIC_NLP_RESOURCES="/share03/draj/data/monolingual_corpora/indic/xsum/indic_nlp_resources"

import sys
infname=sys.argv[1]
outfname=sys.argv[2]

inlang=sys.argv[3]
outlang=sys.argv[4]

sys.path.append('{}'.format(INDIC_NLP_LIB_HOME))

import re
import os
from tqdm import tqdm
import shutil

from indicnlp import common
from indicnlp import loader

common.set_resources_path(INDIC_NLP_RESOURCES)

from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator as script_conv

print()
print(infname)
print(outfname)
print(inlang)
print(outlang)

with open(outfname,'w',encoding='utf-8') as outfile, \
	 open(infname,'r',encoding='utf-8') as infile:

	for line in infile:
		outline = script_conv.transliterate(line.strip(),inlang,outlang)
		outfile.write(outline+'\n')
