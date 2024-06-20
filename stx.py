#!/home/mano/scripts/PythonEnv/stxxxx/bin/python3

import speech_recognition as sr
import pyttsx3
import pyautogui
import psutil
import subprocess




def excuteCommand(command):
	try:
	    result = subprocess.run(command,capture_output=True,text=True, shell=True)
	    return result.stdout.rstrip()
	except subprocess.CalledProcessError as e:
	    print(f"Command '{command}' failed with error code {e.returncode}")

def mercyCheck(pids):
	pids = pids.split("\n")
	print(pids)
	if len(pids)>2:
		mercyBullet(pids)
	else:
		excuteCommand(command='notify-send "Hey Nate, How is Life"')

def mercyBullet(pids):
	excuteCommand(command='notify-send "Nate Cant Hear you anymore"')
	for i in pids:
		result = subprocess.run(f"kill -9 {i}",capture_output=True,text=True, shell=True)

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Main function
def main():
    while True:
        try:
            # Use the microphone as source for input
            with sr.Microphone() as source2:
                # Adjust the energy threshold based on the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # Listen for the user's input
                audio2 = r.listen(source2)

                # Use Google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.capitalize().replace("nate","Nate").replace("sincere home buyers", "Sincere Home Buyers").replace("since your home buyers","Sincere Home Buyers").replace("sincere home bars","Sincere Home Buyers")

                # If user says 'exit', break the loop
                if MyText == "exit":
                    break

                # Type the recognized text
                pyautogui.write(MyText)

                # Optionally, convert recognized text to speech
                # SpeakText(MyText)

        except sr.RequestError as e:
            pass  # Suppress request error messages

        except sr.UnknownValueError:
            pass  # Suppress unknown value error messages

        except KeyboardInterrupt:
            break  # Break the loop if interrupted by user

if __name__ == "__main__":
	x = excuteCommand(command="ps aux | grep 'stx.py' | grep -v grep | awk '{print $2}'")
	mercyCheck(x)
	main()
