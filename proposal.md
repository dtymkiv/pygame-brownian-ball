Robotics-Academy: new exercise using Deep Learning for Visual Control
for Google Summer of Code 2023.

Table of content
================
1. **Abstract** 
    1. Goals
    2. Benefits
2. **Updating Web Interface to Accept PyTorch/TensorFlow Models**
3. **Adding New Exercise for Visual Control using Deep Learning**
4. **Schedule and milestones** 
   1. Updating Web Interface to Accept PyTorch/TensorFlow Models 
   2. Adding New Exercise for Visual Control using Deep Learning
5. **About me**
---------------
**1. Abstract**
===========

1.1 Goals
---------

The goal for this project is to develop a new deep learning exercise for visual robotic 
control within the Robotics-Academy context. In order to implement it, we need build a 
web-based interface that allows the user to input a trained model that matches as input 
the camera installed on a drone or a car, and as outputs the linear speed and angular 
velocity of the vehicle.

1.2 Benefits
------------

Updating the web interface to accept PyTorch/TensorFlow models and adding a new exercise for 
visual control using deep learning in the Robotics-Academy project provide several benefits:

**Updating Web Interface to Accept PyTorch/TensorFlow Models**
1. Improved compatibility: PyTorch and TensorFlow are two of the most popular deep learning 
    frameworks, and enabling the Robotics-Academy web interface to accept models trained using 
    these frameworks will increase the compatibility of the platform with the wider deep learning community.

2. Enhanced usability: Allowing users to upload PyTorch/TensorFlow models to the web interface will 
  enhance the usability of the platform, as it will allow users to easily test 
  and deploy their models in a real-world robotics environment.

3. Better performance: PyTorch/TensorFlow models are known for their high performance, and enabling 
  the Robotics-Academy platform to accept these models will provide users with access to the latest 
  state-of-the-art deep learning techniques for robotics applications.

**Adding New Exercise for Visual Control using Deep Learning**
1. Enhancing learning experience: Adding a new exercise for visual control using deep learning will 
  enhance the learning experience for Robotics-Academy users by exposing them to the latest deep 
  learning techniques for robotics applications.

2. Increasing versatility: The new exercise will increase the versatility of the Robotics-Academy 
  platform by providing users with a wider range of exercises to choose from, and exposing 
  them to new use cases for robotics applications.

3. Improving competitiveness: Robotics research is moving rapidly in the direction of deep learning 
  for perception and control, and adding a new exercise for visual control using deep learning will 
  keep the Robotics-Academy project competitive and up-to-date with the latest research trends.


**2. Updating Web Interface to Accept PyTorch/TensorFlow Models**
====================

To update the web interface of Robotics-Academy to accept models trained with PyTorch/Tensorflow 
as input, we will need to modify the existing file upload functionality to accept model files 
with the appropriate extensions. Here are the steps to do this:

**Modify the frontend code:** Modify the frontend code to allow users to upload model files with the 
appropriate extensions (e.g. .h5 for Keras/TensorFlow models, .pth or .pt for PyTorch models). 
This can be done by adding the appropriate file extensions to the accept attribute of the file 
input element in the HTML code.

Code snippet of html template update
```html
<input type="file" id="model-upload" accept=".h5,.pth,.pt">
```

**Modify the backend code:** Modify the backend code to handle the uploaded model files. This can 
be done by checking the file extension of the uploaded file and using the appropriate library to load the model.
Here's an small part of possible implementation for loading a Keras/TensorFlow or PyTorch model:

```python
from keras.models import load_model as keras_load
from torch import load as torch_load

@app.route('/upload-model', methods=['POST'])
def upload_model():
    model_file = request.files['model']
    if model_file and allowed_file(model_file.filename, ['.h5']):
        model = keras_load(model_file)
    elif model_file and allowed_file(model_file.filename, ['.pth', '.pt']):
        model = torch_load(model_file)
    # use of the model and rest of the code
```

**3. Updating Web Interface to Accept PyTorch/TensorFlow Models**
========================

Here are the steps to add a new exercise using Deep Learning for Visual Control in Robotics-Academy:

Choose a deep learning framework: Choose a deep learning framework 
such as TensorFlow, PyTorch, or Keras to implement the visual control algorithm.

**Define the exercise configuration**: Create a new JSON file in the ``roboticsAcademy/exercises`` directory 
to define the exercise configuration. This file should contain information about the exercise, 
such as its name, description, and the resources required to run it. You should also define any new 
parameters that the exercise will need, such as the path to the model file.

```json
{
  "name": "Visual Control with Deep Learning",
  "description": "Use deep learning to control a robot's movement based on visual input",
  "resources": [
    "robot",
    "camera"
  ],
  "parameters": {
    "model_path": {
      "type": "string",
      "default": "model.h5",
      "description": "Path to the deep learning model file"
    }
  }
}
```
**Create the exercise files:** Create the files for the new exercise in the ``roboticsAcademy/exercises`` directory.
These files can be any code or configuration files required to run the exercise. 
Here's an example implementation using Keras:
```python
from keras.models import load_model
import numpy as np

class VisualControlExercise:

    def __init__(self, robot, camera, model_path):
        self.robot = robot
        self.camera = camera
        self.model = load_model(model_path)

    def run(self):
        while True:
            # Get image from camera
            image = self.camera.getImage().data

            # Preprocess image
            image = preprocess_image(image)

            # Use model to predict robot movement
            prediction = self.model.predict(image)

            # Convert prediction to robot movement
            movement = convert_prediction_to_movement(prediction)

            # Move robot
            self.robot.move(movement)


def preprocess_image(image) -> np.array:
    # Preprocess image for input to model


def convert_prediction_to_movement(prediction) -> np.array:
    # Convert prediction to robot movement
    
```
**Update the generate-exercises.py script:** Update the ``generate-exercises.py`` script in the 
``roboticsAcademy/scripts`` directory to include the new exercise. This script generates the 
exercise templates and adds them to the roboticsAcademy/exercises directory.

**Create ui widgets:** Implement widgets in ``gui`` directory that we weill need for usage of a
exercise. We will need to implement such widgets as: ``car_configuration``, ``line_drawer``,
``track_build``.

**Create visual assets**: In ``recources`` directory we will need to create pngs and recource
objects to allow users to create tracks and draw line that car will follow.

**Test the new exercise:** Test the new exercise by running the generate-exercises.py script 
and checking that the new exercise appears in the list of available exercises in the 
Robotics-Academy web interface.

**4. Schedule and milestones**
==========================

Before starting coding I would like to do some preparation:

- Discussing all needed functionality with mentor.

- A list of  input values, reuired tests for the validation of an exercise.

- Discussing requirements for required resouces and their style.

4.1 Updating Web Interface to Accept PyTorch/TensorFlow Models (3 weeks)
---------
**4.1.1 Create Upload model react component** (1 week)
In ``react_frontend`` I will create a new component called ``ModelInputButton.js``
to handle PyTorch models input and validate its formatting.

**4.1.2 Update template to use new component** (0.5 weeks)

**4.1.3 Create django view to handle model upload** (1 week)
In ``academy_rest_api`` I will create a new view called ``upload_model``
to handle PyTorch models input and validate its formatting.

**4.1.4 Cover new functionality with tests** (0.5 weeks)

4.2 Updating Web Interface to Accept PyTorch/TensorFlow Models (9 weeks)
---------
**4.2.1 Create static resources** (1 week)

I will create a static resources for ``car``, ``track``, etc.

**4.2.2 Create widgets** (2.5 weeks)

I will implement such widgets as: ``car_configuration``, ``line_drawer``,
``track_build``.

**4.2.3 Create the exercise files:** (4.5 week)

 - ``car.py``: a script for training the deep learning model on a dataset of images and corresponding control commands.

 - ``test.py``: a script for testing the trained model in a simulated or real-world environment.

 - ``data/``: a directory containing the training and testing datasets, organized into subdirectories for images and corresponding control commands.

 - ``config.yaml``: a configuration file specifying the hyperparameters and other settings for the deep learning model.

 - ``README.md``: a file containing instructions and guidance on how to complete the exercise, including information on how to train 
 and test the deep learning model, and any additional resources or requirements.

**4.2.4 Cover new functionality with tests** (1 week)

**5. About me**
===============

My name is Dmytro Tymkiv and I am a student of National Ivan Franko University
of Lviv (Ukraine). My timezone is UTC+02:00. My experience with Python is about
4 years, 2+ years commercially. I have no experience in open-source, but I have
enough of git knowledge due to my occupation.

I have a bunch of personal projects, few of them are private, but you can find one
online, visiting [Teplodim website](https://www.kalush-teplodim.pp.ua/).
