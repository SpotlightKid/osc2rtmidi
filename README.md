# osc2rtmidi

A configurable uni-directional OSC to MIDI gateway.

An extended example of using the [python-rtmidi] package.

[python-rtmidi]: http://chrisarndt.de/projects/python-rtmidi


## Installation

This is how you would install `osc2rtmidi` on a Debian/Ubuntu-like system,
e.g. on a Raspberry Pi running Rasbian:

    # Add ~/.local/bin to PATH environment variable
    # (if you haven't already done so).
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.profile
    source ~/.profile

    # Install requirements
    sudo apt-get install \
        build-essential \
        git \
        libasound2-dev \
        libjack-jackd2-dev \
        libyaml-dev \
        liblo-dev \
        python3-pip

    # Get project sources from GitHub
    git clone https://github.com/SpotlightKid/osc2rtmidi
    cd osc2rtmidi

    # Install Cython for current user
    # This can take a while, esp. on a Raspberry Pi
    pip3 install --user Cython

    # Install osc2rtmidi and it's Python dependencies,
    # i.e. python-rtmidi, pyliblo und PyYAML
    pip3 install --user .


## Usage

    osc2rtmidi examples/Mix16.yaml

This will open a virtual ALSA MIDI ouput port and listen for OSC messages on
UDP port 5555 by default.
