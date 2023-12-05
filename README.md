
# GeoGuesser_BB

# (Update) Main code can be found in codefinal.ipynb of the above notebooks # 
(Please bear with us incase there are too many files as we are currently working on improving the accuracy)
This is a CNN model that does the popular TikTok game Geoguesser, in the town of Blacksburg, Virginia 

Geo-guesser is a famous game that picked up throughout the internet where the player guess's where a certain image is taken from based on no information but the image. Apart from being a hobby, this is primary test in CIA exams as well as in military, knowing the location based off a single image. So, we familiarized this game by making a Convolution Neural Network (CNN) model that can identify where the input picture was taken in Blacksburg, Virginia. The approach we took is first preparing datasets with images throughout Blacksburg and then labelling them. This data is fed to a CNN model that can learn to identify based on this labelled input data. The result is that we feed an image to it, and it gives us a ballpark result as to the area we are in, for E.g. feeding an input image of Torgersen bridge should give the result: 'squires student center'. 

More about geoguesser https://www.geoguessr.com/

How is CNN used for Geo-guesser game? 
CNNs (Convolutional Neural Networks) are a class of deep learning, which is extremely effective for analyzing and processing image data. These can be applied to the Geo-guesser game in the following ways: 
Image Classification: CNNs can be trained to identify and recognize various elements in the images (for example, building architecture, roads, vegetation, signage, and so on). 
Feature Extraction: After identifying various unique elements in the images, CNN can narrow down the possible geographical location. For instance, it can distinguish between a cold temperate location and a hot tropical location. 
Scene Recognition: CNN can also be used for recognition of various scenes, such as cityscapes, hilly regions, water bodies, etc. 
Object Detection: Specific objects within the images that might provide clues about the location, such as vehicles, which may have region-specific models or license plates. These can be detected using CNN. 
Integration with Geographic Information: By integrating CNN-identified features with geographic databases, it's possible to map the recognized elements to specific locations or regions. 


# Methodology # 
The main part of any Machine Learning project is the data, if you have a good data, that solves most of your problem 
So for this particular problem, i had to create the data manually as it is easily not available 

# Dataset Creation # 

The data was created in 3 different ways 
First i manually took a video of prime locations of Blacksburg and parsed them to give me images 
Second, I made use of Google street View images where i set up an python automater code that takes screen shots as i progress through the city manually in the street view 
Third was making using of GoogleStreetViewAPI which basically uses a link of your current streetview page and processes it, allowing you to download the image or have it display on colab etc 
So this was a challenging way, but would solve the tedious task of manually sitting and creating a dataset 
A python script that mimics front arrow key and mouse button was created and then the link kept sending itself to the streetview API, this helped me create a dataset with minimal supervision 

Next the data preprocessing step 
Data was preprocessed to see if there are any defective images that might hinder the model
This was done manually as i could not find any other way to do so, other than this conventional data pre processing steps were done such as data augmentation , resizing etc all of which you can find in the code


For each location we captured around 1000 to 1500 images for preprocessing.  The images were manually overseen to be in such a way that it helps the model with proper feature extraction, as CNN works using the principle of feature extraction, we ensured that the images that we took had plenty of features that could distinguish one area of the town from the other.  
Each area was taken and stored as a class, and each class is expected to have its own distinguishable features.  
For E.g. The downtown streets in Blacksburg are unique and distinguishable in that they have red pedestrian path, and buildings made out of red brick design, these are very useful features that the CNN model will make use of by extracting, and then later using it to distinguish the different classes  


# Model summary #
Here i have made use of Tensorflow and built CNN model from scratch without using any transfer learning 

<img width="675" alt="Screenshot 2023-12-04 at 7 07 31 PM" src="https://github.com/Sathyanarayanan-ops/GeoGuesser_BB/assets/57038667/febb9b94-5b09-400c-851d-6f8158b5befc">

This is the model summary 

# Results # 

Considering that the dataset was created manually and was comparitively small 
The loss and accuracy curve showed promising results 

<img width="297" alt="Screenshot 2023-12-04 at 7 12 02 PM" src="https://github.com/Sathyanarayanan-ops/GeoGuesser_BB/assets/57038667/6850877a-e878-4fea-97f0-f1ea47e9eee1">

In terms of accuracy, the model got a 85% accuracy in our first try (present code might have more), however the biggest difficulty faced was the loss as we had the problem of overfitting , which was solved after hours and hours of trial and error and expanding the dataset 

<img width="313" alt="Screenshot 2023-12-04 at 7 15 56 PM" src="https://github.com/Sathyanarayanan-ops/GeoGuesser_BB/assets/57038667/7f638fb3-9779-4bf2-8ee4-33fe1928cfc7">


<img width="299" alt="Screenshot 2023-12-04 at 7 16 17 PM" src="https://github.com/Sathyanarayanan-ops/GeoGuesser_BB/assets/57038667/43391de4-cf65-460c-9136-a0b156ccc43b">







