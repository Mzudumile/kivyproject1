import kivy
kivy.require('2.3.0')
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
import numpy as np
import sounddevice as sd


class Left(FloatLayout):
    pass

class Right(FloatLayout):
    pass

class container(BoxLayout):

    leftFrequency = 50
    rightFrequency = 150
    forwardFrequency = 250
    stopFrequency    = 350
    carrierFrequency = 1500
    samplingFrequency = 40000
    duration_s = 5

    t = np.linspace(0, duration_s, samplingFrequency*duration_s)
    
    leftSignal = np.cos(2*np.pi*leftFrequency*t)
    rightSignal = np.cos(2*np.pi*rightFrequency*t)
    forwardSignal = np.cos(2*np.pi*forwardFrequency*t)
    stopSignal = np.cos(2*np.pi*stopFrequency*t)
    carrierSignal = np.cos(2*np.pi*carrierFrequency*t)
    
    # mpdulation
    modulatedLeftSignal = (1 + leftSignal)*carrierSignal
    modulatedRightSignal = (1 + rightSignal)*carrierSignal
    modulatedForwardSignal = (1 + forwardSignal)*carrierSignal
    modulatedStopSignal = (1 + stopSignal)*carrierSignal


    def leftTurn(self):
        sd.play(self.modulatedLeftSignal, self.samplingFrequency, loop=True)
    
    def rightTurn(self):
        sd.play(self.modulatedRightSignal, self.samplingFrequency, loop=True)
    
    def forward(self):
        sd.play(self.modulatedForwardSignal, self.samplingFrequency, loop=True)
    
    def stopCar(self):
        sd.play(self.modulatedStopSignal, self.samplingFrequency, loop=True)

    def stopSound(self):
        sd.stop()

class MyApp(App):

    def build(self):
        return container()
        
    
MyApp().run()