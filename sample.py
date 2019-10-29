##########################################
#  Developed by Everton Pereira da Cruz  #
##########################################

import sys

if sys.version_info[0] == 2:
	from WAVE_Python_2_7 import WAVE
elif sys.version_info[0] == 3:
	from WAVE_Python_3_7 import WAVE

if __name__ == "__main__":
	audio = WAVE()
	audio.setFilename( 'M1F1-int16-AFsp.wav' )
	audio.loadContent()
	
	print( 'Filename: '        + audio.getFilename() )
	print( 'ChunkID: '         + audio.getChunkID() )
	print( 'ChunkSize: '       + str(audio.getChunkSize()) )
	print( 'Format: '          + audio.getFormat() )
	print( 'Subchunk1ID: '     + audio.getSubchunk1ID() )
	print( 'Subchunk1Size: '   + str(audio.getSubchunk1Size()) )
	print( 'AudioFormat: '     + str(audio.getAudioFormat()) )
	print( 'NumChannels: '     + str(audio.getNumChannels()) )
	print( 'SampleRate: '      + str(audio.getSampleRate()) )
	print( 'ByteRate: '        + str(audio.getByteRate()) )
	print( 'BlockAlign: '      + str(audio.getBlockAlign()) )
	print( 'BitsPerSample: '   + str(audio.getBitsPerSample()) )
	print( 'Subchunk2ID: '     + str(audio.getSubchunk2ID()) )
	print( 'Subchunk2Size: '   + str(audio.getSubchunk2Size()) )
	#print( 'Data: '            + str(audio.getData()) )
	#print( 'Filter (median): ' + str(audio.applyFilter('median')) )
	
	#audio.toWaveFile( 'audio_mod.wav' )
	#audio.setData( audio.applyFilter('median') )
	#audio.setData( audio.applyFilter('onlyFirstChannel') )
	#audio.setData( audio.applyFilter('onlyLastChannel') )
	audio.setData( audio.applyFilter('scale', 5) )
	audio.toWaveFile( 'audio_mod.wav' )