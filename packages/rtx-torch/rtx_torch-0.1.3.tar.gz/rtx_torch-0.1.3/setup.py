# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rtx']

package_data = \
{'': ['*']}

install_requires = \
['classifier-free-guidance-pytorch==0.5.2',
 'efficientnet_pytorch==0.7.1',
 'einops==0.7.0',
 'lz4>=4.3.2,<5.0.0',
 'olefile>=0.47,<0.48',
 'tensorboard>=2.15.1,<3.0.0',
 'tensorboardx>=2.6.2.2,<3.0.0.0',
 'torch',
 'torch-tb-profiler>=0.4.3,<0.5.0',
 'torchvision>=0.16.2,<0.17.0',
 'zetascale==1.2.5']

setup_kwargs = {
    'name': 'rtx-torch',
    'version': '0.1.3',
    'description': 'rtx - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# RT-X\nPytorch implementation of the models RT-1-X and RT-2-X from the paper: "Open X-Embodiment: Robotic Learning Datasets and RT-X Models".\n\nHere we implement both model architectures, RTX-1 and RTX-2\n\n[Paper Link](https://robotics-transformer-x.github.io/)\n\n- The RTX-2 Implementation does not natively output for simplicity a 7 dimensional vector but rather text tokens, if you wanted to output 7 dimensional vector you could implement the same token learner as in RTX1\n\n\n# Appreciation\n* Lucidrains\n* Agorians\n\n# Install\n`pip install rtx-torch `\n\n# Usage\nTo see detailed usage, run `python run.py --help`.\n## RTX1\n- RTX1 Usage takes in text and videos\n- Does not use Efficient Net yet, we\'re integrating it now then the implementation will be complete\n- Uses SOTA transformer architecture\n\n```python\n\nimport torch\nfrom rtx.rtx1 import RTX1, FilmViTConfig\n\n# Use a pre-trained MaxVit model from pytorch\nmodel = RTX1(film_vit_config=FilmViTConfig(pretrained=pretrained))\n\nvideo = torch.randn(2, 3, 6, 224, 224)\n\ninstructions = ["bring me that apple sitting on the table", "please pass the butter"]\n\n# compute the train logits\ntrain_logits = model.train(video, instructions)\n\n# set the model to evaluation mode\nmodel.model.eval()\n\n# compute the eval logits with a conditional scale of 3\neval_logits = model.run(video, instructions, cond_scale=3.0)\nprint(eval_logits.shape)\n```\n\n\n## RTX-2\n- RTX-2 takes in images and text and interleaves them to form multi-modal sentences and outputs text tokens not a 7 dimensional vector of x,y,z,roll,pitch,yaw,and gripper\n```python\n\nimport torch\nfrom rtx import RTX2\n\n# usage\nimg = torch.randn(1, 3, 256, 256)\ntext = torch.randint(0, 20000, (1, 1024))\n\nmodel = RTX2()\noutput = model(img, text)\nprint(output)\n\n```\n\n## EfficientNetFilm\n- Extracts the feature from the given image\n```python\nfrom rtx import EfficientNetFilm\n\nmodel = EfficientNetFilm("efficientnet-b0", 10)\n\nout = model("img.jpeg")\n\n\n```\n# Model Differences from the Paper Implementation\n## RT-1\nThe main difference here is the substitution of a Film-EfficientNet backbone (pre-trained EfficientNet-B3 with Film layers inserted) with a MaxViT model.\n\n\n\n# Tests\nI created a single tests file that uses pytest to run tests on all the modules, RTX1, RTX2, EfficientNetFil, first git clone and get into the repository, install the requirements.txt with pip then run this:\n\n`python -m pytest tests/tests.py`\n\n# License\nMIT\n\n# Citations\n```bibtex\n@misc{open_x_embodiment_rt_x_2023,\ntitle={Open {X-E}mbodiment: Robotic Learning Datasets and {RT-X} Models},\nauthor = {Open X-Embodiment Collaboration and Abhishek Padalkar and Acorn Pooley and Ajinkya Jain and Alex Bewley and Alex Herzog and Alex Irpan and Alexander Khazatsky and Anant Rai and Anikait Singh and Anthony Brohan and Antonin Raffin and Ayzaan Wahid and Ben Burgess-Limerick and Beomjoon Kim and Bernhard Schölkopf and Brian Ichter and Cewu Lu and Charles Xu and Chelsea Finn and Chenfeng Xu and Cheng Chi and Chenguang Huang and Christine Chan and Chuer Pan and Chuyuan Fu and Coline Devin and Danny Driess and Deepak Pathak and Dhruv Shah and Dieter Büchler and Dmitry Kalashnikov and Dorsa Sadigh and Edward Johns and Federico Ceola and Fei Xia and Freek Stulp and Gaoyue Zhou and Gaurav S. Sukhatme and Gautam Salhotra and Ge Yan and Giulio Schiavi and Hao Su and Hao-Shu Fang and Haochen Shi and Heni Ben Amor and Henrik I Christensen and Hiroki Furuta and Homer Walke and Hongjie Fang and Igor Mordatch and Ilija Radosavovic and Isabel Leal and Jacky Liang and Jaehyung Kim and Jan Schneider and Jasmine Hsu and Jeannette Bohg and Jeffrey Bingham and Jiajun Wu and Jialin Wu and Jianlan Luo and Jiayuan Gu and Jie Tan and Jihoon Oh and Jitendra Malik and Jonathan Tompson and Jonathan Yang and Joseph J. Lim and João Silvério and Junhyek Han and Kanishka Rao and Karl Pertsch and Karol Hausman and Keegan Go and Keerthana Gopalakrishnan and Ken Goldberg and Kendra Byrne and Kenneth Oslund and Kento Kawaharazuka and Kevin Zhang and Keyvan Majd and Krishan Rana and Krishnan Srinivasan and Lawrence Yunliang Chen and Lerrel Pinto and Liam Tan and Lionel Ott and Lisa Lee and Masayoshi Tomizuka and Maximilian Du and Michael Ahn and Mingtong Zhang and Mingyu Ding and Mohan Kumar Srirama and Mohit Sharma and Moo Jin Kim and Naoaki Kanazawa and Nicklas Hansen and Nicolas Heess and Nikhil J Joshi and Niko Suenderhauf and Norman Di Palo and Nur Muhammad Mahi Shafiullah and Oier Mees and Oliver Kroemer and Pannag R Sanketi and Paul Wohlhart and Peng Xu and Pierre Sermanet and Priya Sundaresan and Quan Vuong and Rafael Rafailov and Ran Tian and Ria Doshi and Roberto Martín-Martín and Russell Mendonca and Rutav Shah and Ryan Hoque and Ryan Julian and Samuel Bustamante and Sean Kirmani and Sergey Levine and Sherry Moore and Shikhar Bahl and Shivin Dass and Shuran Song and Sichun Xu and Siddhant Haldar and Simeon Adebola and Simon Guist and Soroush Nasiriany and Stefan Schaal and Stefan Welker and Stephen Tian and Sudeep Dasari and Suneel Belkhale and Takayuki Osa and Tatsuya Harada and Tatsuya Matsushima and Ted Xiao and Tianhe Yu and Tianli Ding and Todor Davchev and Tony Z. Zhao and Travis Armstrong and Trevor Darrell and Vidhi Jain and Vincent Vanhoucke and Wei Zhan and Wenxuan Zhou and Wolfram Burgard and Xi Chen and Xiaolong Wang and Xinghao Zhu and Xuanlin Li and Yao Lu and Yevgen Chebotar and Yifan Zhou and Yifeng Zhu and Ying Xu and Yixuan Wang and Yonatan Bisk and Yoonyoung Cho and Youngwoon Lee and Yuchen Cui and Yueh-hua Wu and Yujin Tang and Yuke Zhu and Yunzhu Li and Yusuke Iwasawa and Yutaka Matsuo and Zhuo Xu and Zichen Jeff Cui},\nhowpublished  = {\\url{https://arxiv.org/abs/2310.08864}},\nyear = {2023},\n}\n```\n\n# Todo\n- Integrate EfficientNetFilm with RTX-1\n- Create training script for RTX-1 by unrolling observations and do basic cross entropy in first rt-1\n- Use RTX-2 dataset on huggingface\n- [Check out the project board for more tasks](https://github.com/users/kyegomez/projects/10/views/1)',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/rt-x',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.12',
}


setup(**setup_kwargs)
