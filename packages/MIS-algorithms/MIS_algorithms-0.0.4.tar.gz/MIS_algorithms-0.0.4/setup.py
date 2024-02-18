from setuptools import setup, find_packages

setup(
    name='MIS_algorithms',
    version='0.0.4',
    author='Niek Mooij',
    author_email='mooij.niek@gmail.com',
    description='All algorithms used in the paper "Finding Large Independent Sets in Networks Using Competitive Dynamics"',
    url='https://github.com/NiekMooij/MIS',
    classifiers=[
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent'],
    packages=find_packages(),
    install_requires=[
        'networkx',
        'numpy',
        'scipy',
        'pulp',
        'communities'
    ],
    entry_points={
        'console_scripts': [
            'continuation=MIS.continuation:main',
            'exact=MIS.exact:main',
            'greedy=MIS.greedy:main',
            'lotka_volterra=MIS.lotka_volterra:main',
            'erdos_renyi=MIS.generate_graphs.erdos_renyi:main',
            'random_bipartite=MIS.generate_graphs.random_bipartite:main',
            'random_geometric=MIS.generate_graphs.random_geometric:main',
            'is_maximal_independent_set=MIS.functions.is_maximal_independent_set:main',
            'reduced_graph=MIS.functions.reduced_graph:main'

        ],
    },
)