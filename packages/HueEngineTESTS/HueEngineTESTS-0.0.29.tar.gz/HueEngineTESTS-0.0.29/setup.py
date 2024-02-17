from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# BETA
# setup(
#     name='HueEngine-Beta',
#     version='1.1.0',
#     description='Hue Engine ©️',
#     long_description=long_description,
#     long_description_content_type='text/markdown',
#     url='https://github.com/TheDotBat/HueEngine',
#     author='Setoichi',
#     author_email='setoichi.dev@gmail.com',
#     license='Apache-2.0',
#     packages=find_packages(),
#     install_requires=[
#         'psutil', 'pygame-ce', 'pyautogui',
#         'pygame-gui', 'screeninfo', 'pygetwindow'
#     ],
#     classifiers=[
#         'Development Status :: 4 - Beta',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: Apache Software License',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.10',
#         'Programming Language :: Python :: 3.11',
#         'Programming Language :: Python :: 3.12',
#         'Topic :: Software Development :: Libraries :: pygame',
#         'Operating System :: OS Independent',
#     ],
#     entry_points={
#         'console_scripts': [
#             'Hue=Hue.scripts.main:main',
#         ]
#     },
# )

# PROD
# setup(
#     name='HueEngine',
#     version='1.0.0',
#     description='Hue Engine ©️',
#     long_description=long_description,
#     long_description_content_type='text/markdown',
#     url='https://github.com/TheDotBat/HueEngine',
#     author='Setoichi',
#     author_email='setoichi.dev@gmail.com',
#     license='Apache-2.0',
#     packages=find_packages(),
#     install_requires=[
#         'psutil', 'pygame-ce', 'pyautogui',
#         'pygame-gui', 'screeninfo', 'pygetwindow'
#     ],
#     classifiers=[
#         'Development Status :: 5 - Production/Stable',
#         'Intended Audience :: Developers',
#         'License :: OSI Approved :: Apache Software License',
#         'Programming Language :: Python :: 3',
#         'Programming Language :: Python :: 3.10',
#         'Programming Language :: Python :: 3.11',
#         'Programming Language :: Python :: 3.12',
#         'Topic :: Software Development :: Libraries :: pygame',
#         'Operating System :: OS Independent',
#     ],
#     entry_points={
#         'console_scripts': [
#             'Hue=Hue.scripts.main:main',
#         ]
#     },
# )

# TESTS
setup(
    name='HueEngineTESTS',
    version='0.0.29',
    description='Hue Engine ©️',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/TheDotBat/HueEngine',
    author='Setoichi',
    author_email='setoichi.dev@gmail.com',
    license='Apache-2.0',
    packages=find_packages(),
    install_requires=[
        'psutil', 'pygame-ce', 'pyautogui',
        'pygame-gui', 'screeninfo', 'pygetwindow'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: pygame',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'Hue=Hue.scripts.main:main',
        ]
    },
)