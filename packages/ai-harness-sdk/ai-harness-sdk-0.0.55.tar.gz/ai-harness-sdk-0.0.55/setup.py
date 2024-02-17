"""Python setup.py for AI-Harness package"""
from setuptools import setup, find_packages

setup(
    name='ai-harness-sdk',
    version='0.0.55',
    packages=find_packages(),
    description='AI Harness SDK',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Navneet',
    author_email='navneet@ai-harness.com',
    license='LICENSE',
    install_requires=[
        # List your package dependencies here
    ],
)
