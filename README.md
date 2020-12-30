# Telekinesis-Helyx-hack
## Inspiration

I Started this project for people with severe impairment or spinal cord injury has loss of ability to do anything.
Because I saw the suffering of my grandmother after getting paralyzed.
The target populations for the mind controlled wheelchair are the patients who are paralyzed below the neck and are unable to use conventional wheelchair interfaces. 
This project is about the controlling electronic devices with brain waves( EEG - electroencephalogram, electrical activity in the brain.)

## What it does

THE MAIN OBJECTIVE of this project is to classify the EEG signal to control the wheelchair’s movement. The specific objectives are: 
i) To acquire EEG through ADS1292R and store the data in PC/Cloud. 
ii) To analyze the EEG signal using FFT and calculating average Power of alpha waves using Python. 
iii) To classify the EEG signal into two basic movements based on power of alpha waves. 
iv) To transfer data from Python to Arduino and control the test object.

Using Welch's algorithm, Power spectral density of EEG is calculated, if it's greater then threshold value the motor rotates else stops. Threshold value is different for different persons as each person has their unique EEG. This threshold value can be determined by training the model.


## How I built it

Metal Electrodes are used to extract EEG near visual cortex of the brain(alpha waves are strong here),electrodes are then connected to ADS1292R(via 3.5mm jack) which is connected to Arduino Uno(via SPI Protocol) because ADS1292R cannot communicate with computer directly, Arduino acts like a Bridge.
After connecting to computer we can store raw EEG signal using a software called BrainBay in the csv format, it can be also used for visualizing the signal. This raw signal(present in csv format) is opened in Python(using pandas library), using Welch's algorithm it calculates power spectral density of EEG, if the value of power in alpha region is greater than the threshold, it means the person has changed his status of mind, so the wheelchair should moves, else it stops. Once, the processing is done in python, data is sent back to Arduino which controls the motor.
Hardware Used:
1. **Arduino Uno** (350 Rupees)
2. **ADS1292R** (4000 Rupees): This is a breakout board for the TI ADS1292R Analog front-end IC for ECG and respiration measurement. This is a simple board to add ECG/Respiration measurement capability to your Arduino, Raspberry Pi or other microcontroller of choice.
3. **EEG Headband** (800 Rupees)

## Challenges I ran into

1. Filtering the EEG signal.
2. Python-Arduino communication.
3. My plan is to link machine learning algorithms to train the model for calculating the threshold value, But, I am not familiar with machine learning, still working on it, hopefully it will be achieved in the future.

## Accomplishments that I'm proud of

Built a working low-cost prototype (cost : 5000 rupees)

## What I learned

I learnt about biosignals, Arduino, Python, Machine Learning

## What's next for Telekenisis

1. Link machine learning algorithms for determining threshold values.
2. Store the raw EEG signal in cloud instead of PC, So that doctors can view EEG from anywhere, anytime.
    EEG can be used to detect brain disorders, brain tumors, epilepsy, dementia, strokes, sleeping disorders, internal injuries and many more.
3. We can use the spectral features for drowsiness detection and many more useful applications.
