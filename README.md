# Real-time Audio Classification of Flute Techniques using MLP

## Description

**realtime.py** is a Python script that demonstrates real-time audio classification of flute techniques using a Multi-Layer Perceptron (MLP) model. The script takes audio input from the system's audio input device, processes the audio in real-time, and predicts the audio class and values using the pre-trained MLP model. The predicted results are sent to a Max Patch application using OSC (Open Sound Control) messages.

## Model Inputs and Outputs
### Model Inputs:
The model expects audio spectrogram data as input, represented as a 2-dimensional numpy array with the shape (1, 1920). The spectrogram is computed on 15 frames of 512 samples using the Mel-Log-Spectrogram transformation with a sampling rate of 24000 Hz, computed on a 2048 samples window (n_fft), and a hop length of 512 samples.

### Model Outputs:
The MLP model predicts the audio class probabilities for 15 different classes. The predicted class probabilities are represented as a 1-dimensional numpy array with a length of 15. Each value in the array represents the probability of the audio belonging to the corresponding class.

## Requirements

To run this script, you need the following dependencies installed:

- pyaudio==0.2.11
- librosa==0.8.1
- tensorflow==2.6.0
- numpy==1.19.5
- pandas==1.3.3
- python-osc==1.7.5
- resampy==0.2.2

You can install these dependencies using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
Additionally, for the Max Patch application to receive and process the OSC messages and launch Python code, you need to have the [shell](https://github.com/jeremybernstein/shell) external object for Max installed. Make sure you have the "shell" object configured and available in your Max environment.

## Usage

1. Ensure that the required dependencies are installed as mentioned in the "Requirements" section.

2. Place the pre-trained MLP model file (**mss23_hyperas.h5**) in the same directory as the **realtime.py** script.

3. Run the **realtime.py** script:

   ```bash
   python realtime.py
   ```
   (or run it through shell object in the provided max patch ```mss23-iptr.maxpatch```)

4. The script will open the audio stream and start processing the incoming audio input in real-time. If the audio stream is active and audio is present, the script will predict the audio class and values using the pre-trained MLP model. The results will be sent to a Max Patch application using OSC messages.

5. The Max Patch application can use the received OSC messages to control and modify audio processing and visualization.

## Important Notes

- The audio input is assumed to have a sample rate of 48000 Hz. If the input sample rate is different, the script will automatically resample it to 24000 Hz using the **resampy** library. If you are running with a different sample rate, please modify ```sampleRate``` in the ```realtime.py``` script.

- The MLP model file **mss23_hyperas.h5** should be trained and saved separately using a compatible version of TensorFlow and Keras. The training code is not provided in this repository.

- OSC messages are sent to the IP address "127.0.0.1" and port number 5005. Make sure the receiving application (Max Patch) is configured to listen to OSC messages on this address and port.

- The script is optimized for a buffer size of 512 samples.

## Recognized Techniques

The **realtime.py** script using the MLP model can recognize the following flute playing techniques:

1. aeolian
2. play-and-sing (+play-and-sing-unison)
3. aeolian-and-ordinario
4. sforzando (+fortepiano)
5. flatterzunge
6. staccato
7. harmonic-fingering
8. tongue-ram
9. key-click
10. trill (trill-minor-second-up+trill-major-second-up)
11. multiphonics
12. whistle-tones
13. ordinario (+note-lasting)
14. whistle-tones-sweeping
15. pizzicato

Please note that the recognition of these techniques is based on the capabilities of the pre-trained MLP model used in the script. The model's precision may be limited, and the recognition performance can vary depending on the input audio and specific playing styles. Users are encouraged to experiment with the script and the model, keeping in mind the disclaimer provided in the README.

## References

1. Brochec, Nicolas and Tanaka, Tsubasa. "ミクスト音楽のためのフルート奏法自動判別手法の検討" (Investigation of Automatic Flute Playing Technique Recognition for Mixed Music). *Japanese Society of Sonic Arts*, vol. 14, no. 3, Dec 2022, pp. 31-34. [PDF](https://hal.science/hal-04073680/file/6.Nicolas.pdf).

## License

This script is licensed under the GNU General Public License version 3.0 (GPL-3.0). You can find the full text of the license in the **LICENSE** file.

## Contact Information

For questions or inquiries, please contact me.

## Disclaimer

**This real-time audio classification script and its underlying MLP model are provided purely for experimental and educational purposes. The script aims to demonstrate the real-time audio classification capabilities using a Multi-Layer Perceptron model. However, it is essential to note that the current model suffers from a lack of precision and may not provide accurate predictions in all scenarios. As with any experimental project, it is subject to limitations and may require further refinement to achieve higher accuracy. Users are encouraged to use this script with caution and should not rely on its predictions for critical or sensitive applications.**

