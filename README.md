# WHY

1. [Apple got rid of the Python2 interpreter in 12.3](https://developer.apple.com/documentation/macos-release-notes/macos-12_3-release-notes)
2. the original iTermocil then breaks and [hasn't been updated in a while](https://github.com/TomAnthony/itermocil)
3. there's [another fork](https://github.com/PythonicNinja/itermocil) but it only creates panes, not windows

so here's an update of iTermocil running with Python3.

# DOCUMENTATION

check out the [original one](https://github.com/TomAnthony/itermocil).

# INSTALLATION

1. clone the repo
2. go in and install with `python3 setup.py install --install-scripts=$(brew --prefix)/bin`

zero knowledge in 🐍, but It Just Works™.
