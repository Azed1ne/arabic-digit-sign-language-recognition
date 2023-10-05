## About:
A custom hand gesture recognition model, built using cvzone in Python; I applied it to recognise digits in the Arabic sign language ArSL.

Here's a youtube video explaining the digits in ArSL: 

[![Thumbnail](https://img.youtube.com/vi/2Zraggt1tVs/0.jpg)](https://www.youtube.com/watch?v=2Zraggt1tVs)


## Files:
The files in the 'Model' folder contain 2 models trained on the same dataset to recognise the digits: 1 to 4 in Arabic Sign Language [ArSL].

The images that were trained on are removed, but it was approximately around 400 images per class.

## How to use it:
Run the 'test.py' folder, a window will show your webcam and you can start doing signs and it'll recognise them in real time.

## How to train your own model:
1- Create a 'Data' folder and inside it create separate folders for as many classes or "signs" as you would like.

2- Open 'dataCollection.py' and change the **NUMBER_OF_SIGNS** var to the number of signs you want to train on.

3- Run the file, type either 1,2,3 or 4 to switch between the folders, type s to save an image, and type q to quit.

4- Once you're happy with the dataset ( 300 minimum is recommended ), go to [here]([url](https://teachablemachine.withgoogle.com/train)https://teachablemachine.withgoogle.com/train) and select **Image project** > **Standard image project**.

5- Label the classes and upload your dataset here: ![image](https://github.com/Azed1ne/arabic-digit-sign-language-recognition/assets/123888749/25ce1857-9492-4c60-b3d4-bc74d496e8b3).

6- Click on **Train Model** and wait, the default parameters in the advanced section are good for a small dataset, tho you could play with the number of epochs for better accuracy ( higher usually is better ).

7- Export the model, save it to the 'Model' folder.

8- Run test.py and see the performance.
