import os
from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read()


def collect_ext():
    extensions = []
    for dirpath, dirnames, filenames in os.walk('src'):
        for filename in filenames:
            if filename in ['assembly.py','library.py','stdlib.py']:
                continue
            filepath = os.path.join(dirpath, filename)
            if filepath.endswith('py'):
                mod = filepath.replace(
                    '/', '.').replace('\\', '.').replace('.py', '')[4:]
            elif filepath.endswith('pyx'):
                mod = filepath.replace('/', '.').replace('.pyx', '')[4:]
            else:
                continue
            extensions.append(
                Extension(
                    mod,
                    [filepath],
                    include_dirs=['src'],
                ))
    return extensions


setup(
    name="systemq",
    version='6.0.0',
    author="baqis",
    author_email="baqis@baqis.ac.cn",
    url="https://gitee.com/",
    license="MIT",
    keywords="quantum lab",
    description="control, measure and visualization",
    long_description='long_description',
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=['dev*', 'home*', 'lib*', 'src*']),
    ext_modules=cythonize(module_list=collect_ext(),
                          exclude=[],
                          build_dir=f"build"),
    package_data={"": ["*.pyd", "*.so"]},
    include_package_data=True,
    install_requires=requirements,
    python_requires='>=3.10.0',
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    project_urls={
        'source': 'https://gitee.com',
    },
)
