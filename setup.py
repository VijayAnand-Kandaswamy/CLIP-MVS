from setuptools import setup, find_packages

setup(
    name="clip_video_processor",
    version="0.1.0",
    description="A library for processing video frames and storing CLIP embeddings in Qdrant",
    author="Vijay Anand Kandaswamy, Anto Nobel",
    url="https://github.com/yourusername/clip_video_processor",
    packages=find_packages(),
    install_requires=[
        "transformers==4.39.3",
        "qdrant-client",
        "opencv-python",
        "Pillow",
        "matplotlib",
        "protobuf==3.19.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
