# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fot']

package_data = \
{'': ['*']}

install_requires = \
['chromadb', 'swarms', 'uuid']

setup_kwargs = {
    'name': 'forest-of-thoughts',
    'version': '0.0.2',
    'description': 'Paper - Pytorch',
    'long_description': '[![Multi-Modality](agorabanner.png)](https://discord.gg/qUtxnK2NMf)\n\n# Forest of thoughts\n\n## Install\n\n\n## Usage\n```python\nimport os\nfrom swarms import OpenAIChat, Mixtral\nfrom fot.main import ForestOfAgents\nfrom dotenv import load_dotenv\n\n# Load env\nload_dotenv()\n\n# OpenAI API key\napi_key = os.getenv("OPENAI_API_KEY")\n\n# create llm\nopenai = OpenAIChat(openai_api_base=api_key)\nllm = Mixtral(max_new_tokens=3000, load_in_4bit=True)\n\n# Create a forest of agents\nforest = ForestOfAgents(\n    openai, num_agents=5, max_loops=1, max_new_tokens=100\n)\n\n# Distribute tasks to the agents\nforest.run("What is the meaning of life?")\n\n\n```\n\n\n# License\nMIT\n\n',
    'author': 'Kye Gomez',
    'author_email': 'kye@apac.ai',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/kyegomez/forest-of-thoughts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
