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
			
			#self.setChunkID( str(file.read(4), 'utf-8') ) # https://docs.python.org/3.1/library/functions.html#str
			# or
			self.setChunkID( file.read(4).decode() ) # https://docs.python.org/3/library/stdtypes.html#bytes.decode
			
			if self.getChunkID() != 'RIFF':
				state = False
			else:
				#tmp = file.read(4)[::-1]
				#self.setChunkSize( tmp[0]*16**6 + tmp[1]*16**4 + tmp[2]*16**2 + tmp[3]*16**0 )
				# or
				#tmp = file.read(4)
				#self.setChunkSize( tmp[0]*16**0 + tmp[1]*16**2 + tmp[2]*16**4 + tmp[3]*16**6 )
				# or
				#self.setChunkSize( int(file.read(4)[::-1].hex(), 16) ) # https://docs.python.org/3/library/stdtypes.html#bytes.hex
				# or
				self.setChunkSize( int.from_bytes(file.read(4), byteorder='little') ) # https://docs.python.org/3/library/stdtypes.html#int.from_bytes
				self.setFormat( file.read(4).decode() )
				self.setSubchunk1ID( file.read(4).decode() )
				self.setSubchunk1Size( int.from_bytes(file.read(4), byteorder='little') )
				self.setAudioFormat( int.from_bytes(file.read(2), byteorder='little') )
				self.setNumChannels( int.from_bytes(file.read(2), byteorder='little') )
				self.setSampleRate( int.from_bytes(file.read(4), byteorder='little') )
				self.setByteRate( int.from_bytes(file.read(4), byteorder='little') )
				self.setBlockAlign( int.from_bytes(file.read(2), byteorder='little') )
				self.setBitsPerSample( int.from_bytes(file.read(2), byteorder='little') )
				#sself.extraParamSize = 0	# address = 36 (2 bytes) if PCM, then doesn't exist 
				#sself.extraParams = ''		# address = 38 (x bytes) x space for extra parameters
				self.setSubchunk2ID( file.read(4).decode() )
				self.setSubchunk2Size( int.from_bytes(file.read(4), byteorder='little') )
				
				_content = []
				_numSamples = self.getSubchunk2Size() // (self.getNumChannels() * self.getBitsPerSample() // 8)
				_numChannels = self.getNumChannels()
				_bytesPerSample = self.getBitsPerSample() // 8
				
				for sample in range(_numSamples):
					_channels = []
					for channel in range(_numChannels):
						_value = int(file.read(_bytesPerSample)[::-1].hex(), 16)
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
		
		file = open( filename, 'wb' )
		#file.write( bytes(self.getChunkID(), 'utf-8') ) # https://docs.python.org/3/library/stdtypes.html#bytes
		# or
		#file.write( bytearray(self.getChunkID(), 'utf-8') )# https://docs.python.org/3/library/stdtypes.html#bytearray
		# or
		file.write( str.encode(self.getChunkID()) ) # https://docs.python.org/3/library/stdtypes.html#str.encode
		file.write( self.getChunkSize().to_bytes( 4, byteorder='little' ) ) # https://docs.python.org/3/library/stdtypes.html#int.to_bytes
		
		
		file.write( str.encode(self.getFormat()) )
		file.write( str.encode(self.getSubchunk1ID()) )
		file.write( self.getSubchunk1Size().to_bytes( 4, byteorder='little' ) )
		file.write( self.getAudioFormat().to_bytes( 2, byteorder='little' ) )
		file.write( self.getNumChannels().to_bytes( 2, byteorder='little' ) )
		file.write( self.getSampleRate().to_bytes( 4, byteorder='little' ) )
		file.write( self.getByteRate().to_bytes( 4, byteorder='little' ) )
		file.write( self.getBlockAlign().to_bytes( 2, byteorder='little' ) )
		file.write( self.getBitsPerSample().to_bytes( 2, byteorder='little' ) )
		##self.extraParamSize = 0	# address = 36 (2 bytes) if PCM, then doesn't exist 
		##self.extraParams = ''		# address = 38 (x bytes) x space for extra parameters
		file.write( str.encode(self.getSubchunk2ID()) )
		file.write( self.getSubchunk2Size().to_bytes( 4, byteorder='little' ) )
		
		_content = self.getData()
		_nSamples = len(_content)
		_bytesPerSample = self.getBitsPerSample() // 8
		
		for sample in _content:
			for channel in sample:
				file.write( channel.to_bytes( _bytesPerSample, byteorder='little' ) )
		
		file.close()