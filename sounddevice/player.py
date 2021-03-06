import Queue as queue
import sounddevice as sd
import soundfile as sf

class player:
	def __init__(self, _folder, _device, _channel):
		self.folder = _folder
		self.device = _device
		device_info = sd.query_devices(self.device, 'input')
		# soundfile expects an int, sounddevice provides a float:
		self.samplerate = int(device_info['default_samplerate'])
		self.channel = _channel
		self.buffersize = 25
		self.blocksize = 2048

		# Transport attribute
		self.isPlaying = False

	def playFileFromIndex(self, index):

		if(index != -1 ):
			self.playFile(str(index)+".wav")


	def playFile(self, filename):

		self.isPlaying = True
		
		self.stop()
		data, fs = sf.read(self.folder+"/"+filename, dtype='float32')
		sd.play(data, fs, device=self.device)
		print('#' * 80)
		print('PLAYING')
		print('#' * 80)

		#status = sd.wait()

	def stop(self):

		sd.stop()




