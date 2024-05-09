"""
Alumnos: Victor Pallas i Pol Raich 
"""

import struct as st

def estereo2mono(ficEste, ficMono, canal=2): 
    """
    
    """
    with open(ficEste, "rb") as file:
        format =  '<4sI4s'
        buffer = file.read(st.calcsize(format))
        chunk_id, chunk_size, riff_format = st.unpack(format, buffer)
        if chunk_id != b"RIFF" or riff_format != b"WAVE":
            raise TypeError(f"File {ficEste} is not a WAVE file")
        else: 
            print(f"{ficEste}: {chunk_id = }\t{chunk_size = }\t{riff_format = }")
            
        format = '<4sI2H2I2H'
        buffer = file.read(st.calcsize(format))
        subchunk1_id, shubchunk1_size, audio_format, num_channels, smp_rate, byte_rate, block_align, Bits_sample = st.unpack(format, buffer)
        
        format = '<4sI'
        buffer = file.read(st.calcsize(format))
        subchunk2_id, subchunk2_size = st.unpack(format, buffer)

        sample_num = subchunk2_size // 2   
        
        format = f"{sample_num}h"
        buffer = file.read(st.calcsize(format))     
        data = st.unpack(format, buffer)
        
        if canal == 0:
            """
            """
            
        elif canal == 1:
            """
            """
            
        elif canal == 2:
            """
            """
            
        elif canal == 3:
            """
            """             
   