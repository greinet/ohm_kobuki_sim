from distutils.core import setup

setup(
    version='0.0.0',
    scripts=['scripts/ohm_kobuki_sim_node.py'],
    packages=['ohm_kobuki_sim'],
    package_dir={'': 'src'}
)
