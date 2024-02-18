from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name="futurevision", 
    version="0.0.1",  
    description="Library that combines Robotics Hardware, iPhone and AI for Everyone",  
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/AliEdis/futurevision",
    author="Ali Edis",  
    author_email="aliedis34@gmail.com",  
    keywords = [
    'iPhone',
    'Raspberry Pi',
    'Arduino',
    'Computer Vision',
    'Artificial Intelligence',
    'Image Processing',
    'Robotics Hardware',
    'OpenCV',
    'MediaPipe',
    'numpy',
    'pyserial',
    'scipy',
    'dlib',
    'pyautogui',
    'pyaudio',
    'gtts',
    'pygame',
    ],
    
    package_dir={'futurevision': 'futurevision'},
    
    install_requires=[
        'opencv-python',
        'mediapipe',
        'numpy',
        'pyserial',
        'scipy',
        'dlib',
        'pyautogui',
        'pyaudio',
        'gtts',
        'pygame',
        'flask',
    ],
    license="MIT",
    project_urls={
        "Bug Reports": "https://github.com/AliEdis/futurevision/issues",
        "Funding": "https://donate.pypi.org",
        "Source": "https://github.com/AliEdis/futurevision",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],

)
