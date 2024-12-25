"""
First create a Python virtual environment:
    pip install virtualenv 
    virtualenv my_env # create a virtual environment named my_env
    source my_env/bin/activate # activate my_env


# installing Gradio in my_env
    python3.11 -m pip install gradio==4.44.1 ibm-watson-machine-learning==1.0.349 email-validator==2.1.1 numpy==1.23.5 pandas==1.5.3

"""




import gradio as gr

"""

#calculate the sum
def add_numbers(Num1, Num2):
    return Num1 + Num2

# Define the interface
demo = gr.Interface(
    fn=add_numbers, 
    inputs=["number", "number"], # Create two numerical input fields where users can enter numbers
    outputs="number" # Create numerical output fields
)

"""


#combine two input sentences together
def combine(a, b):
    return a + " " + b


demo = gr.Interface(
    fn=combine,
    inputs = [
        gr.Textbox(label="Input 1"),
        gr.Textbox(label="Input 2")
    ],
    outputs = gr.Textbox(value="", label="Output")
)


# Launch the interface
demo.launch(server_name="0.0.0.0", server_port= 7860)