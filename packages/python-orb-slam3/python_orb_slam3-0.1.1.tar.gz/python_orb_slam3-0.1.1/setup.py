# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_orb_slam3']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.20.0,<2.0.0', 'opencv-python>=4,<5']

setup_kwargs = {
    'name': 'python-orb-slam3',
    'version': '0.1.1',
    'description': 'A Python wrapper of ORB-SLAM3 algorithm',
    'long_description': '# python-orb-slam3\n\nA Python wrapper for the [ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3) feature extraction algorithm.\n\n## Installation\n\n### From PyPI\n\n> **Note**\n> This package\'s pre-built binaries are only available for AMD64 architectures.\n\n```bash\npip install python-orb-slam3\n```\n\n### From source\n\nThere are a few steps to follow to install this package from the source code, please refer to the CI configuration file [here](.github/workflows/ci.yml) for more details.\n\n## Usage\n\n```python\nimport cv2\nfrom matplotlib import pyplot as plt\n\nfrom python_orb_slam3 import ORBExtractor\n\nsource = cv2.imread("path/to/image.jpg")\ntarget = cv2.imread("path/to/image.jpg")\n\norb_extractor = ORBExtractor()\n\n# Extract features from source image\nsource_keypoints, source_descriptors = orb_extractor.detectAndCompute(source)\ntarget_keypoints, target_descriptors = orb_extractor.detectAndCompute(target)\n\n# Match features\nbf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)\nmatches = bf.match(source_descriptors, target_descriptors)\n\n# Draw matches\nsource_image = cv2.drawKeypoints(source, source_keypoints, None)\ntarget_image = cv2.drawKeypoints(target, target_keypoints, None)\nmatches_image = cv2.drawMatches(source_image, source_keypoints, target_image, target_keypoints, matches, None)\n\n# Show matches\nplt.imshow(matches_image)\nplt.show()\n```\n\n## License\n\nThis repository is licensed under the [GPLv3](LICENSE) license.\n\n<!--markdownlint-disable-file MD046-->\n\n    A Python wrapper for the ORB-SLAM3 feature extraction algorithm.\n    Copyright (C) 2022  Johnny Hsieh\n\n    This program is free software: you can redistribute it and/or modify\n    it under the terms of the GNU General Public License as published by\n    the Free Software Foundation, either version 3 of the License, or\n    (at your option) any later version.\n\n    This program is distributed in the hope that it will be useful,\n    but WITHOUT ANY WARRANTY; without even the implied warranty of\n    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n    GNU General Public License for more details.\n\n    You should have received a copy of the GNU General Public License\n    along with this program.  If not, see <https://www.gnu.org/licenses/>.\n',
    'author': 'Mix',
    'author_email': '32300164+mnixry@users.noreply.github.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
