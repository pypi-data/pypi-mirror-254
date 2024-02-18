from setuptools import setup, find_packages

setup(
    version="1.0.2",
    name="auto_subtitle_llama",
    packages=find_packages(),
    py_modules=["auto_subtitle_llama"],
    author="Youngjun Kim",
    author_email="ai.yjun42@gmail.com",
    url="https://github.com/YJ-20/auto-subtitle-llama",
    install_requires=[
        'openai-whisper',
        'ffmpeg-python',
        'transformers',
        'sentencepiece',
        'protobuf',
    ],
    description="Automatically generate, translate and embed subtitles into your videos",
    keywords=['subtitles', 'translate', 'video', 'whisper', 'llama2'],
    entry_points={
        'console_scripts': ['auto_subtitle_llama=auto_subtitle_llama.cli:main'],
    },
    include_package_data=True,
)
