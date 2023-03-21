# SimpleSynthPython
Simple python synthesiser

This repository defines a very simply synthesiser (synth.py) which defines the class: Synth().

A user can import and initialise the class:

    import synth     
    my_synth = synth.Synth()

Add notes, or a tune:

    my_synth.add_tune()
    my_synth.append_note_to_output('sine', freq=1000, duration=0.5, amplitude=0.5)

And then play the output:

    my_synth.play_output

# Coding Task
The task here is to understand the code and add the functionality to include a square wave in the synthesiser. Along 
the way you may spot some small optimizations/improvements that could be made to the code. These are not part of the 
task, but may be things we will talk about during the interview.

If you would like to edit/add to/improve other parts of the code you are more than welcome to experiment, but please 
don't feel the need to go above and beyond. This is a simple task, and we appreciate simple solutions.

# Setting up a Virtual Environment
In order to run this code on your computer, you will need to set up python and install some basic packages. To do 
this we recommend setting up a Virtual Environment. We have provided a requirements file to help with this. Once 
python is installed you can create a virtual environment with:

    python -m venv venv

then activate and install it with:

    .\venv\Scripts\activate
    py -m pip install -r requirements.txt

Alternatively, you can use conda and install the packages manually
