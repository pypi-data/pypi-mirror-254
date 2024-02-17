# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['labelu',
 'labelu.alembic_labelu',
 'labelu.alembic_labelu.versions',
 'labelu.internal',
 'labelu.internal.adapter',
 'labelu.internal.adapter.persistence',
 'labelu.internal.adapter.routers',
 'labelu.internal.application',
 'labelu.internal.application.command',
 'labelu.internal.application.response',
 'labelu.internal.application.service',
 'labelu.internal.common',
 'labelu.internal.dependencies',
 'labelu.internal.domain.models',
 'labelu.internal.middleware',
 'labelu.internal.statics',
 'labelu.tests',
 'labelu.tests.internal',
 'labelu.tests.internal.adapter',
 'labelu.tests.internal.adapter.persistence',
 'labelu.tests.internal.adapter.routers',
 'labelu.tests.internal.common',
 'labelu.tests.utils']

package_data = \
{'': ['*'],
 'labelu.internal.statics': ['assets/*', 'src/icons/*', 'src/img/example/*'],
 'labelu.tests': ['data/*']}

install_requires = \
['aiofiles>=22.1.0,<23.0.0',
 'alembic>=1.9.4,<2.0.0',
 'appdirs>=1.4.4,<2.0.0',
 'email-validator>=1.3.0,<2.0.0',
 'fastapi>=0.86.0,<0.87.0',
 'loguru>=0.6.0,<0.7.0',
 'passlib[bcrypt]>=1.7.4,<2.0.0',
 'pillow>=9.3.0,<10.0.0',
 'python-dotenv>=0.21.0,<0.22.0',
 'python-jose[cryptography]>=3.3.0,<4.0.0',
 'python-multipart>=0.0.5,<0.0.6',
 'sqlalchemy>=1.4.43,<2.0.0',
 'typer[all]>=0.7.0,<0.8.0',
 'uvicorn>=0.19.0,<0.20.0']

entry_points = \
{'console_scripts': ['labelu = labelu.main:cli']}

setup_kwargs = {
    'name': 'labelu',
    'version': '0.9.2',
    'description': '',
    'long_description': '<div align="center">\n<article style="display: flex; flex-direction: column; align-items: center; justify-content: center;">\n    <p align="center"><img width="300" src="https://user-images.githubusercontent.com/25022954/209616423-9ab056be-5d62-4eeb-b91d-3b20f64cfcf8.svg" /></p>\n    <h1 style="width: 100%; text-align: center;"></h1>\n    <p align="center">\n        English | <a href="./README_zh-CN.md" >简体中文</a>\n    </p>\n</article>\n    \n   \n</div>\n\n## Introduction\n\nLabelU offers a variety of annotation tools and features, supporting image, video, and audio annotation.\n\n- Image: Multifunctional image processing tools encompassing 2D bounding box, cuboid, semantic segmentation, polylines, keypoints, and many other annotation tools, assist in completing image identification, annotation, and analysis.\n- Video: The video annotation has robust video processing capabilities, able to implement video segmentation, video classification, video information extraction, and other functions, providing high-quality annotated data for model training.\n- Audio: Highly efficient and accurate audio analysis tool can achieve audio segmentation, audio classification, audio information extraction, and other functions, making complex sound information visually intuitive.\n\n<p align="center">\n<img style="width: 600px" src="https://user-images.githubusercontent.com/25022954/209318236-79d3a5c3-2700-46c3-b59a-62d9c132a6c3.gif">\n</p>\n\n## Features\n\n- Simplicity: Provides a variety of image annotation tools that can be annotated through simple visual configuration.\n- Flexibility: A variety of tools can be freely combined to meet most image, video, and audio annotation needs.\n- Universality: Supports exporting to various data formats, including JSON, COCO, MASK.\n\n## Getting started\n\n- <a href="https://opendatalab.github.io/labelU-Kit/">\n    <button>Try LabelU annotation toolkit</button>\n</a>\n\n- <a href="https://labelu.shlab.tech/">\n    <button>Try LabelU online</button>\n</a>\n\n### Local deployment\n\n1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html), Choose the corresponding operating system type and download it for installation.\n\n> **Note：** If your system is MacOS with an Intel chip, please install [Miniconda of intel x86_64](https://repo.anaconda.com/miniconda/)。\n\n2. After the installation is complete, run the following command in the terminal (you can choose the default \'y\' for prompts during the process):\n\n```bash\nconda create -n labelu python=3.7\n```\n\n> **Note：** For Windows platform, you can run the above command in Anaconda Prompt.\n\n3. Activate the environment：\n\n```bash\nconda activate labelu\n```\n\n4. Install LabelU：\n\n```bash\npip install labelu\n```\n\n> To install the test version：`pip install --extra-index-url https://test.pypi.org/simple/ labelu==<test revision>`\n\n5. Run LabelU：\n\n```bash\nlabelu\n```\n\n6. Visit [http://localhost:8000/](http://localhost:8000/) and ready to go.\n\n### Local development\n\n```bash\n# Download and Install miniconda\n# https://docs.conda.io/en/latest/miniconda.html\n\n# Create virtual environment(python = 3.7)\nconda create -n labelu python=3.7\n\n# Activate virtual environment\nconda activate labelu\n\n# Install peotry\n# https://python-poetry.org/docs/#installing-with-the-official-installer\n\n# Install all package dependencies\npoetry install\n\n# Start labelu, server: http://localhost:8000\nuvicorn labelu.main:app --reload\n\n# Update submodule\ngit submodule update --remote --merge\n```\n\n## Supported Scenarios\n\n### Image\n\n- Label Classification: Can help users quickly classify objects in images and can be used for image retrieval, object detection tasks.\n- Text Description: Text transcription can help users quickly extract text information in images and can be used for text retrieval, machine translation tasks.\n- Bounding Box: Can help users quickly select objects in images and can be used for image recognition, object tracking tasks.\n- Point Annotation: Points can help users accurately label key information in the image and can be used for object recognition, scene analysis tasks.\n- Polygon: Can help users accurately label irregular shapes and can be used for object recognition, scene analysis tasks.\n- Line Annotation: Lines can help users accurately label edges and contours in the image and can be used for object recognition, scene analysis tasks.\n- Cuboid: Cuboid can help users accurately label the size, shape, and location of objects within images, and can be used for object recognition, scene analysis tasks.\n\n### Video\n\n- Label Classification: Classifying and labeling videos can be used for video retrieval, recommendation, and classification tasks.\n- Text Description: Converting speech content in videos into text can be used for voice recognition, transcription, and translation tasks.\n- Segment Segmentation: Extracting specific clips or scenes from the video for annotation is very useful for video object detection, action recognition, and video summary tasks.\n- Timestamps: Point to or mark specific parts of the video; users can click on timestamps to jump directly to that part of the video.\n\n### Audio\n\n- Label Classification: By listening to the audio and selecting the appropriate classification for annotation, it\'s applicable for audio retrieval, recommendations, and classification tasks.\n- Text Description: Converting speech content in audio into text makes it easier for users to analyze and process text. It\'s very useful for voice recognition, transcription tasks, and can help users better understand and process voice content.\n- Segment Segmentation: Extracting specific clips from audio for annotation is very useful for audio event detection, voice recognition, and audio editing tasks.\n- Timestamps: Used to point to or mark specific parts of the audio; users can click on timestamps to jump directly to that part of the audio.\n\n## Quick start\n\n- [Guidance](https://opendatalab.github.io/labelU)\n\n## Annotation format\n\n- [Documentation](https://opendatalab.github.io/labelU/#/schema)\n\n## Communication\n\nWelcome to the OpenDataLab official WeChat group！\n\n<p align="center">\n<img style="width: 400px" src="https://user-images.githubusercontent.com/25022954/208374419-2dffb701-321a-4091-944d-5d913de79a15.jpg">\n</p>\n\n## Links\n\n- [LabelU-kit](https://github.com/opendatalab/labelU-Kit) (LabelU is developed using LabelU-kit.)\n\n## License\n\nThis project is released under the [Apache 2.0 license](./LICENSE).\n',
    'author': 'pengjinhu',
    'author_email': 'pengjinhu@pjlab.org.cn',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/opendatalab/labelU',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
