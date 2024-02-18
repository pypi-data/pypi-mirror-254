from setuptools import setup, find_packages

setup(
    name='maldinio_ai',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        "tiktoken>=0.4.0",
        "openai>=1.3.7",
    ],
    description='A utility package for AI prompt management and prompt processing.',
    author='Mehdi Nabhani',
    author_email='mehdi@nabhani.de',
    keywords=['AI', 'NLP', 'LLM', 'Prompt Management'],

)
