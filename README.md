# Abnormal_Activity_Detection_DL_Model
This project consists of a deep learning classifier model to predict any unusual activity in a given CCTV footage. 
This prototype consists of 4 modules namely data organization, video to frame conversion, feature extraction and model evaluation. UCF Crime Dataset is chosen as it contains a variety of video clips based on real-world anomalies to make sure the outcomes are tangible.
The entire dataset of videos is transformed into individual frames using the FFmpeg library to get the features from each frame. Using Convolutional Neural Networks, the feature extraction process is made possible and the data is saved for training. The features are appended to the frames in a fixed sequence which is fed to LSTM to train the entire dataset. Added callbacks ensure that the model saves the best weights in each epoch to attain more accuracy.
Research Paper: https://www.jardcs.org/abstract.php?id=3954
