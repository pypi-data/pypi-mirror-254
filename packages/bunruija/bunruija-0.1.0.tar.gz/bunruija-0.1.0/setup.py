# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bunruija',
 'bunruija.classifiers',
 'bunruija.classifiers.prado',
 'bunruija.classifiers.qrnn',
 'bunruija.data',
 'bunruija.feature_extraction',
 'bunruija.filters',
 'bunruija.modules',
 'bunruija.tokenizers']

package_data = \
{'': ['*']}

install_requires = \
['Cython>=3.0.8,<4.0.0',
 'datasets>=2.16.0,<3.0.0',
 'fugashi>=1.1.1,<2.0.0',
 'hydra-core>=1.2.0,<2.0.0',
 'ipadic>=1.0.0,<2.0.0',
 'lightgbm>=4.2.0,<5.0.0',
 'loguru>=0.7.2,<0.8.0',
 'mmh3>=3.0.0,<4.0.0',
 'ruamel-yaml>=0.18.5,<0.19.0',
 'scikit-learn>=1.0.2,<2.0.0',
 'scipy>=1.8.0,<2.0.0',
 'torch>=2.1.2,<3.0.0',
 'transformers>=4.36.2,<5.0.0',
 'unidic-lite>=1.0.8,<2.0.0']

entry_points = \
{'console_scripts': ['bunruija-evaluate = bunruija.evaluate:cli_main',
                     'bunruija-gen-yaml = bunruija.gen_yaml:cli_main',
                     'bunruija-predict = bunruija.predict:cli_main',
                     'bunruija-train = bunruija.train:cli_main']}

setup_kwargs = {
    'name': 'bunruija',
    'version': '0.1.0',
    'description': 'A text classification toolkit',
    'long_description': '# Bunruija\nBunruija is a text classification toolkit.\nBunruija aims at enabling pre-processing, training and evaluation of text classification models with **minimum coding effort**.\nBunruija is mainly focusing on Japanese though it is also applicable to other languages.\n\nSee `example` for understanding how bunruija is easy to use.\n\n## Features\n- **Minimum requirements of coding**: bunruija enables users to train and evaluate their models through command lines. Because all experimental settings are stored in a yaml file, users do not have to write codes.\n- **Easy to compare neural-based model with non-neural-based model**: because bunruija supports models based on scikit-learn and PyTorch in the same framework, users can easily compare classification accuracies and prediction times of neural- and non-neural-based models.\n- **Easy to reproduce the training of a model**: because all hyperparameters of a model are stored in a yaml file, it is easy to reproduce the model.\n\n## Install\n```\npip install bunruija\n```\n\n## Example configs\nExample of `sklearn.svm.SVC`\n\n```yaml\ndata:\n  train: train.csv\n  dev: dev.csv\n  test: test.csv\n\noutput_dir: models/svm-model\n\npipeline:\n  - type: sklearn.feature_extraction.text.TfidfVectorizer\n    args:\n      tokenizer:\n        type: bunruija.tokenizers.mecab_tokenizer.MeCabTokenizer\n        args:\n          lemmatize: true\n          exclude_pos:\n            - 助詞\n            - 助動詞\n      max_features: 10000\n      min_df: 3\n      ngram_range:\n        - 1\n        - 3\n  - type: sklearn.svm.SVC\n    args:\n      verbose: false\n      C: 10.\n```\n\nExample of BERT\n\n```yaml\ndata:\n  train: train.csv\n  dev: dev.csv\n  test: test.csv\n\noutput_dir: models/transformer-model\n\npipeline:\n  - type: bunruija.feature_extraction.sequence.SequenceVectorizer\n    args:\n      tokenizer:\n        type: transformers.AutoTokenizer\n        args:\n          pretrained_model_name_or_path: cl-tohoku/bert-base-japanese\n  - type: bunruija.classifiers.transformer.TransformerClassifier\n    args:\n      device: cpu\n      pretrained_model_name_or_path: cl-tohoku/bert-base-japanese\n      optimizer:\n        type: torch.optim.AdamW\n        args:\n          lr: 3e-5\n          weight_decay: 0.01\n          betas:\n            - 0.9\n            - 0.999\n      max_epochs: 3\n```\n\n## CLI\n```sh\n# Training a classifier\nbunruija-train -y config.yaml\n\n# Evaluating the trained classifier\nbunruija-evaluate -y config.yaml\n```\n\n## Config\n### data\nYou can set data-related settings in `data`.\n\n```yaml\ndata:\n  train: train.csv  # training data\n  dev: dev.csv # development data\n  test: test.csv # test data\n  label_column: label\n  text_column: text\n```\n\nYou can set local files in `train`, `dev`, and `test`.\nSupported types are `csv`, `json` and `jsonl`.\n`label_column` and `text_column` are field names of label and text.\nWhen you set `label_column` to `label` and `text_column` to `text`, which are the default values, actual data must be as follows:\n\nFormat of `csv`:\n\n```csv\nlabel,text\nlabel_name,sentence\n…\n```\n\nFormat of `json`:\n\n```json\n[{"label", "label_name", "text": "sentence"}]\n```\n\nFormat of `jsonl`:\n\n```json\n{"label", "label_name", "text": "sentence"}\n```\n\n### pipeline\nYou can set pipeline of your model in `pipeline`\n\n\n## Prediction using the trained classifier in Python code\nAfter you trained a classification model, you can use that model for prediction as follows:\n```python\nfrom bunruija import Predictor\n\npredictor = Predictor.from_pretrained("output_dir")\nwhile True:\n    text = input("Input:")\n    label: list[str] = predictor([text], return_label_type="str")\n    print(label[0])\n```\n\n`output_dir` is a directory that is specified in `output_dir` in config.\n',
    'author': 'Takuya Makino',
    'author_email': 'takuyamakino15@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/tma15',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<3.11',
}
from build import *
build(setup_kwargs)

setup(**setup_kwargs)
