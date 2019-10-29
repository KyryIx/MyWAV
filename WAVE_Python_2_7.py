##########################################
#  Developed by Everton Pereira da Cruz  #
##########################################

# http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/WAVE.html
# http://www-mmsp.ece.mcgill.ca/Documents/AudioFormats/WAVE/Samples.html
# https://blogs.msdn.microsoft.com/dawate/2009/06/22/intro-to-audio-programming-part-1-how-audio-data-is-represented/
# https://blogs.msdn.microsoft.com/dawate/2009/06/23/intro-to-audio-programming-part-2-demystifying-the-wav-format/
# http://soundfile.sapp.org/doc/WaveFormat/
# https://en.wikipedia.org/wiki/Pulse-code_modulation

import os.path
import math
import copy

class WAVE:
	def __init__(self):
		self.filename = ''
		self.chunkID = ''			# address = 00 (4 bytes)
		self.chunkSize = 0			# address = 04 (4 bytes)
		self.format = ''			# address = 08 (4 bytes)
		self.subchunk1ID = ''		# address = 12 (4 bytes)
		self.subchunk1Size = 0		# address = 16 (4 bytes)
		self.audioFormat = 0		# address = 20 (2 bytes)
		self.numChannels = 0		# address = 22 (2 bytes)
		self.sampleRate = 0			# address = 24 (4 bytes)
		self.byteRate = 0			# address = 28 (4 bytes)
		self.blockAlign = 0			# address = 32 (2 bytes)
		self.bitsPerSample = 0		# address = 34 (2 bytes)
		#self.extraParamSize = 0	# address = 36 (2 bytes) if PCM, then doesn't exist 
		#self.extraParams = ''		# address = 38 (x bytes) x space for extra parameters
		self.subchunk2ID = ''		# address = 36 (4 bytes)
		self.subchunk2Size = 0		# address = 40 (4 bytes)
		self.data = []				# address = 44 (* bytes)
	
	def setFilename(self, filename):
		self.filename = filename
	
	def getFilename(self):
		return self.filename
	
	def setChunkID(self, chunkID):
		self.chunkID = chunkID
	
	def getChunkID(self):
		return self.chunkID
	
	def setChunkSize(self, chunkSize):
		self.chunkSize = chunkSize
	
	def getChunkSize(self):
		return self.chunkSize
	
	def setFormat(self, format):
		self.format = format
	
	def getFormat(self):
		return self.format
	
	def setSubchunk1ID(self, subchunk1ID):
		self.subchunk1ID = subchunk1ID
	
	def getSubchunk1ID(self):
		return self.subchunk1ID
	
	def setSubchunk1Size(self, subchunk1Size):
		self.subchunk1Size = subchunk1Size
	
	def getSubchunk1Size(self):
		return self.subchunk1Size
	
	def setAudioFormat(self, audioFormat):
		self.audioFormat = audioFormat
	
	def getAudioFormat(self):
		return self.audioFormat
	
	def setNumChannels(self, numChannels):
		self.numChannels = numChannels
	
	def getNumChannels(self):
		return self.numChannels
	
	def setSampleRate(self, sampleRate):
		self.sampleRate = sampleRate
	
	def getSampleRate(self):
		return self.sampleRate
	
	def setByteRate(self, byteRate):
		self.byteRate = byteRate
	
	def getByteRate(self):
		return self.byteRate
	
	def setBlockAlign(self, blockAlign):
		self.blockAlign = blockAlign
	
	def getBlockAlign(self):
		return self.blockAlign
		
	def setBitsPerSample(self, bitsPerSample):
		self.bitsPerSample = bitsPerSample
	
	def getBitsPerSample(self):
		return self.bitsPerSample
		
	#def setExtraParamSize(self, extraParamSize):
	#	self.extraParamSize = extraParamSize
	
	#def getExtraParamSize(self):
	#	return self.extraParamSize
	
	#def setExtraParams(self, extraParams):
	#	self.extraParams = extraParams
	
	#def getExtraParams(self):
	#	return self.extraParams
	
	def setSubchunk2ID(self, subchunk2ID):
		self.subchunk2ID = subchunk2ID
	
	def getSubchunk2ID(self):
		return self.subchunk2ID
	
	def setSubchunk2Size(self, subchunk2Size):
		self.subchunk2Size = subchunk2Size
	
	def getSubchunk2Size(self):
		return self.subchunk2Size
	
	def setData(self, data):
		self.data = copy.deepcopy(data)
	
	def getData(self):
		return copy.deepcopy(self.data)
	
	def loadContent(self):
		if not os.path.isfile( self.getFilename() ):
			return False
		else:
			file = open( self.getFilename(), 'rb' )
			state = False
			
			self.setChunkID( file.read(4) )
			
			if self.getChunkID() != 'RIFF':
				state = False
			else:
				self.setChunkSize( int((file.read(4)[::-1]).encode("hex"), 16) )
				self.setFormat( file.read(4) )
				self.setSubchunk1ID( file.read(4) )
				self.setSubchunk1Size( int((file.read(4)[::-1]).encode("hex"), 16) )
				self.setAudioFormat( int((file.read(2)[::-1]).encode("hex"), 16) )
				self.setNumChannels( int((file.read(2)[::-1]).encode("hex"), 16) )
				self.setSampleRate( int((file.read(4)[::-1]).encode("hex"), 16) )
				self.setByteRate( int((file.read(4)[::-1]).encode("hex"), 16) )
				self.setBlockAlign( int((file.read(2)[::-1]).encode("hex"), 16) )
				self.setBitsPerSample( int((file.read(2)[::-1]).encode("hex"), 16) )
				#sself.extraParamSize = 0	# address = 36 (2 bytes) if PCM, then doesn't exist 
				#sself.extraParams = ''		# address = 38 (x bytes) x space for extra parameters
				self.setSubchunk2ID( file.read(4) )
				self.setSubchunk2Size( int((file.read(4)[::-1]).encode("hex"), 16) )
				
				_content = []
				_numSamples = self.getSubchunk2Size() // (self.getNumChannels() * self.getBitsPerSample() // 8)
				_numChannels = self.getNumChannels()
				_bytesPerSample = self.getBitsPerSample() // 8
				
				for sample in range(_numSamples):
					_channels = []
					for channel in range(_numChannels):
						_value = int((file.read(_bytesPerSample)[::-1]).encode("hex"), 16)
						_channels.append( _value )
					_content.append( _channels )
				
				self.setData( _content )
				state = True
			
			file.close()
			return state
	
	def applyFilter(self, typeFilter='median', value=2 ):
		_content = self.getData()
		_nSamples  = len(_content)
		_nChannels = self.getNumChannels()
		
		for i in range(_nSamples):
			
			if typeFilter=='median':
				_median = 0
				sample = _content[i]
			
				for channel in sample:
					_median = _median + channel
			
				_median = _median // _nChannels
		
				for j in range(_nChannels):
					_content[i][j] = _median
			
			elif typeFilter=='onlyFirstChannel':
				for j in range(1, len(_content[i])):
					_content[i][j] = 0
			
			elif typeFilter=='onlyLastChannel':
				for j in range(0, len(_content[i])-1):
					_content[i][j] = 0
			
			elif typeFilter=='scale':
				for j in range(len(_content[i])):
					_content[i][j] = int(value * _content[i][j]) & (2**self.getBitsPerSample() - 1)
		
		return _content
	
	def toWaveFile(self, filename):
		
		def writeFile( file, value, number_bytes ):
			bytes = hex(value)[2:]
			bytes = (2 * number_bytes - len(bytes)) * '0' + bytes
			for i in range(len(bytes)-1, 0, -2):
				file.write( chr( int(bytes[i-1:i+1],16) ) )
		
		file = open( filename, 'wb' )
		file.write( self.getChunkID() )
		writeFile( file, self.getChunkSize(), 4 )
		file.write( self.getFormat() )
		file.write( self.getSubchunk1ID() )
		writeFile( file, self.getSubchunk1Size(), 4 )
		writeFile( file, self.getAudioFormat(), 2 )
		writeFile( file, self.getNumChannels(), 2 )
		writeFile( file, self.getSampleRate(), 4 )
		writeFile( file, self.getByteRate(), 4 )
		writeFile( file, self.getBlockAlign(), 2 )
		writeFile( file, self.getBitsPerSample(), 2 )
		#self.extraParamSize = 0	# address = 36 (2 bytes) if PCM, then doesn't exist 
		#self.extraParams = ''		# address = 38 (x bytes) x space for extra parameters
		file.write( self.getSubchunk2ID() )
		writeFile( file, self.getSubchunk2Size(), 4 )
		
		_content = self.getData()
		_nSamples = len(_content)
		_bytesPerSample = self.getBitsPerSample() // 8
		
		for sample in _content:
			for channel in sample:
				writeFile( file, channel, _bytesPerSample )
		
		file.close()