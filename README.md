# Real-time Audio Classification of Flute Techniques using MLP

## Description

**realtime.py** is a Python script that demonstrates real-time audio classification of flute techniques using a Multi-Layer Perceptron (MLP) model. The script takes audio input from the system's audio input device, processes the audio in real-time, and predicts the audio class and values using the pre-trained MLP model. The predicted results are sent to a Max Patch application using OSC (Open Sound Control) messages.

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

4. The script will open the audio stream and start processing the incoming audio input in real-time. If the audio stream is active and audio is present, the script will predict the audio class and values using the pre-trained MLP model. The results will be sent to a Max Patch application using OSC messages.

5. The Max Patch application can use the received OSC messages to control and modify audio processing and visualization.

## Important Notes

- The audio input is assumed to have a sample rate of 48000 Hz. If the input sample rate is different, the script will automatically resample it to 24000 Hz using the **resampy** library.

- The MLP model file **mss23_hyperas.h5** should be trained and saved separately using a compatible version of TensorFlow and Keras.

- OSC messages are sent to the IP address "127.0.0.1" and port number 5005. Make sure the receiving application (Max Patch) is configured to listen to OSC messages on this address and port.

- The script is optimized for a buffer size of 512 samples.

- During periods of silence (no audio input), the script waits for 0.25 seconds before checking for new audio data.

## License

This script is licensed under the GNU General Public License version 3.0 (GPL-3.0). You can find the full text of the license in the **LICENSE** file.

## Contact Information

For questions or inquiries, please contact me.

---

Feel free to modify the contact information, usage instructions, or any other details in the README as needed. Additionally, you can add sections like "Acknowledgments" or "References" if required.
